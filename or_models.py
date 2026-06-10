#!/usr/bin/env python3
"""
or_models.py — OpenRouter モデルカタログ取得 / 詳細レポート / 差分追跡ツール

依存ゼロ（Python 3 標準ライブラリのみ）。OpenRouter の公開 API
（https://openrouter.ai/api/v1/models, 認証不要）からモデル一覧を取得し、
タイムスタンプ付きスナップショットとして保存。スナップショット間の差分
（新規追加 / 削除 / 変更）を検出し、詳細な Markdown レポートを生成する。

サブコマンド:
  fetch          最新のモデル一覧を取得してスナップショット保存 + 直前との差分表示
  report         最新スナップショットから全モデルの詳細 Markdown レポート生成
  new            直近2スナップショットの差分（新規/削除/変更）を Markdown 出力
  diff A B       任意の2スナップショット間の差分を表示
  list           保存済みスナップショット一覧
  show <id>      指定モデルIDの詳細を表示

使い方の例:
  python3 or_models.py fetch          # 初回 & 以降の定期取得（これだけで差分が出る）
  python3 or_models.py report         # 全モデル詳細レポート -> reports/
  python3 or_models.py new            # 前回からの新規モデルだけ -> reports/
"""

import argparse
import datetime as dt
import json
import os
import sys
import urllib.request
import urllib.error

FE_URL = "https://openrouter.ai/api/frontend/v1/catalog/models"  # サイトと同じ全モデル(画像/音声/embeddings/動画/rerank等を含む)。旧 /api/frontend/models は2026-06頃廃止(404)
V1_URL = "https://openrouter.ai/api/v1/models"         # 公開API(テキスト出力中心のサブセット)。フォールバック用
API_URL = FE_URL  # 後方互換
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SNAP_DIR = os.path.join(BASE_DIR, "snapshots")
REPORT_DIR = os.path.join(BASE_DIR, "reports")

# 差分検出で「変更」とみなして比較するフィールド
WATCH_FIELDS = {
    "name": lambda m: m.get("name"),
    "context_length": lambda m: m.get("context_length"),
    "modality": lambda m: (m.get("architecture") or {}).get("modality"),
    "price_prompt": lambda m: (m.get("pricing") or {}).get("prompt"),
    "price_completion": lambda m: (m.get("pricing") or {}).get("completion"),
    "price_cache_read": lambda m: (m.get("pricing") or {}).get("input_cache_read"),
    "price_cache_write": lambda m: (m.get("pricing") or {}).get("input_cache_write"),
    "supported_parameters": lambda m: sorted(m.get("supported_parameters") or []),
    # price_ プレフィックスを避ける（diff表示で per_million 変換されるのはトークン単価のみ）
    "unit_pricing": lambda m: [(u.get("label"), u.get("price"),
                                tuple((t.get("label"), t.get("price")) for t in u.get("tiers") or []))
                               for u in (m.get("pricing") or {}).get("units") or []],
}

# supported_parameters -> 人間向けケイパビリティ表記
CAP_MAP = [
    ("tools", "Function calling"),
    ("tool_choice", "Tool choice"),
    ("structured_outputs", "Structured outputs(JSONスキーマ)"),
    ("response_format", "JSON mode"),
    ("reasoning", "Reasoning(思考)"),
    ("include_reasoning", "Reasoning出力"),
    ("web_search_options", "Web検索"),
    ("logprobs", "logprobs"),
    ("seed", "Seed固定"),
]


# ----------------------------------------------------------------------------
# 取得 / 保存 / 読み込み
# ----------------------------------------------------------------------------
# モダリティ表示の正規化順 / 取り込む価格キー
MOD_ORDER = {"text": 0, "image": 1, "file": 2, "audio": 3, "video": 4}
PRICE_KEYS = ("prompt", "completion", "input_cache_read", "input_cache_write",
              "web_search", "image", "audio", "internal_reasoning", "request")


def _sortmods(lst):
    return sorted(set(lst or []), key=lambda x: (MOD_ORDER.get(x, 9), x))


def _iso_to_unix(s):
    if not s:
        return None
    try:
        return int(dt.datetime.fromisoformat(str(s).replace("Z", "+00:00")).timestamp())
    except (ValueError, TypeError):
        return None


def _norm_units(dp):
    """display_pricing（画像/動画/検索等の単位課金SKU）を簡約化して保持。
    2026-06頃からトークン価格0＋単位課金のみのモデルが増えた（無料と誤判定しないため必須）"""
    out = []
    for d in dp or []:
        price = _f(d.get("price"))
        if d.get("kind") != "unit" or price is None:
            continue
        ent = {"label": d.get("sku_label"), "price": price, "unit": d.get("unitLabel")}
        tiers = [{"label": t.get("sku_label"), "price": _f(t.get("price"))}
                 for t in (d.get("tiers") or []) if _f(t.get("price")) is not None]
        if tiers:
            ent["tiers"] = tiers
        out.append(ent)
    return out


def normalize_frontend(m):
    """frontend API の1エントリを v1相当の内部スキーマに変換（以降の処理を共通化）"""
    e = m.get("endpoint") or {}
    p = e.get("pricing") or {}
    pricing = {k: p[k] for k in PRICE_KEYS if k in p}
    units = _norm_units(p.get("display_pricing"))
    if units:
        pricing["units"] = units
    ins = _sortmods(m.get("input_modalities"))
    outs = _sortmods(m.get("output_modalities"))
    params = list(e.get("supported_parameters") or [])
    if m.get("supports_reasoning") and "reasoning" not in params:
        params.append("reasoning")
    # v1 と同じ ID 規約: 非standardバリアントは :free / :thinking 等を付与
    slug = m.get("slug")
    variant = e.get("variant") or "standard"
    mid = slug if variant == "standard" else f"{slug}:{variant}"
    return {
        "id": mid,
        "slug": slug,
        "variant": variant,
        "provider_name": e.get("provider_name") or e.get("provider_display_name"),
        "canonical_slug": m.get("permaslug"),
        "hugging_face_id": m.get("hf_slug"),
        "name": m.get("name") or m.get("slug"),
        "created": _iso_to_unix(m.get("created_at")),
        "created_at": m.get("created_at"),
        "updated_at": m.get("updated_at"),
        "description": (m.get("description") or "").strip(),
        "context_length": m.get("context_length") or e.get("context_length"),
        "architecture": {
            "modality": ("+".join(ins) + "->" + "+".join(outs)) if (ins or outs) else None,
            "input_modalities": ins,
            "output_modalities": outs,
            "tokenizer": m.get("group"),
            "instruct_type": m.get("instruct_type"),
        },
        "pricing": pricing,
        "top_provider": {
            "context_length": e.get("context_length"),
            "max_completion_tokens": e.get("max_completion_tokens"),
            "is_moderated": e.get("moderation_required"),
        },
        "supported_parameters": params,
        "knowledge_cutoff": m.get("knowledge_cutoff"),
        "supports_reasoning": bool(m.get("supports_reasoning")),
    }


def fetch_models_frontend():
    req = urllib.request.Request(FE_URL, headers={"User-Agent": "or-models-tracker/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        data = json.loads(r.read().decode("utf-8"))
    arr = data.get("data", data) if isinstance(data, dict) else data
    # 提供エンドポイントを持ち、無効化/非公開でない = 現在使用可能なモデル
    servable = [m for m in arr
                if m.get("slug") and m.get("endpoint")
                and not (m.get("endpoint") or {}).get("is_disabled")
                and not m.get("is_private")]
    out = [normalize_frontend(m) for m in servable]
    if not out:
        raise RuntimeError("frontend APIから0件。形式変更の可能性。")
    return out


def fetch_models_v1():
    req = urllib.request.Request(V1_URL, headers={"User-Agent": "or-models-tracker/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    models = data.get("data", [])
    if not models:
        raise RuntimeError("v1 APIから0件。")
    return models


def fetch_models():
    try:
        return fetch_models_frontend()
    except (urllib.error.URLError, RuntimeError, ValueError, KeyError) as ex:
        print(f"[警告] frontend API取得に失敗 ({ex})。v1 APIにフォールバックします。", file=sys.stderr)
        return fetch_models_v1()


def save_snapshot(models):
    os.makedirs(SNAP_DIR, exist_ok=True)
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = os.path.join(SNAP_DIR, f"models-{ts}.json")
    payload = {"fetched_at": dt.datetime.now().isoformat(timespec="seconds"),
               "count": len(models), "data": models}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return path


def list_snapshots():
    if not os.path.isdir(SNAP_DIR):
        return []
    return sorted(os.path.join(SNAP_DIR, f) for f in os.listdir(SNAP_DIR)
                  if f.startswith("models-") and f.endswith(".json"))


def load_snapshot(path):
    with open(path, encoding="utf-8") as f:
        payload = json.load(f)
    return payload.get("data", payload)  # 生配列でも受ける


def index_by_id(models):
    return {m["id"]: m for m in models}


# ----------------------------------------------------------------------------
# 価格 / 表示ヘルパ
# ----------------------------------------------------------------------------
def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def per_million(val):
    """per-token 文字列 -> $/1M tok の見やすい文字列"""
    v = _f(val)
    if v is None:
        return "—"
    if v < 0:
        return "変動(動的)"
    if v == 0:
        return "無料"
    m = v * 1_000_000
    if m >= 1:
        return f"${m:,.2f}"
    return f"${m:,.4f}".rstrip("0").rstrip(".")


def price_num(val):
    """per-token 文字列 -> $/1M tok の数値（-1=変動, None=不明）"""
    v = _f(val)
    if v is None:
        return None
    if v < 0:
        return -1.0
    return round(v * 1_000_000, 6)


def raw_usd(val):
    v = _f(val)
    if v is None:
        return None
    if v == 0:
        return "無料"
    return f"${v:g}"


def provider_of(model):
    return model["id"].split("/")[0]


def is_free(model):
    if model["id"].endswith(":free"):
        return True
    p = model.get("pricing") or {}
    # トークン単価が0でも単位課金(units: /枚・/秒等)があれば有料
    vals = [_f(v) for k, v in p.items() if k != "units"]
    vals += [u.get("price") for u in p.get("units") or []]
    vals = [v for v in vals if v is not None]
    return bool(vals) and all(v == 0 for v in vals)


def fmt_ctx(n):
    if not n:
        return "—"
    if n >= 1_000_000:
        return f"{n/1_000_000:g}M ({n:,})"
    if n >= 1000:
        return f"{n//1000}K ({n:,})"
    return f"{n:,}"


def capabilities(model):
    sp = set(model.get("supported_parameters") or [])
    caps = [label for key, label in CAP_MAP if key in sp]
    # 重複ラベルの整理（reasoning と include_reasoning は1つに）
    out = []
    for c in caps:
        if c not in out:
            out.append(c)
    return out


def created_date(model):
    ts = model.get("created")
    if not ts:
        return "—"
    try:
        return dt.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except (OverflowError, OSError, ValueError):
        return "—"


# ----------------------------------------------------------------------------
# 差分
# ----------------------------------------------------------------------------
def diff_snapshots(old_models, new_models):
    old, new = index_by_id(old_models), index_by_id(new_models)
    old_ids, new_ids = set(old), set(new)

    added = [new[i] for i in sorted(new_ids - old_ids)]
    removed = [old[i] for i in sorted(old_ids - new_ids)]

    changed = []
    for i in sorted(old_ids & new_ids):
        deltas = {}
        for field, getter in WATCH_FIELDS.items():
            a, b = getter(old[i]), getter(new[i])
            if a != b:
                deltas[field] = (a, b)
        if deltas:
            changed.append((new[i], deltas))
    return {"added": added, "removed": removed, "changed": changed}


# ----------------------------------------------------------------------------
# Markdown 生成
# ----------------------------------------------------------------------------
def model_detail_md(m, level=3):
    h = "#" * level
    lines = [f"{h} {m.get('name', m['id'])}", ""]
    arch = m.get("architecture") or {}
    p = m.get("pricing") or {}

    lines.append(f"- **ID**: `{m['id']}`")
    lines.append(f"- **Provider**: {provider_of(m)}")
    lines.append(f"- **Context**: {fmt_ctx(m.get('context_length'))} tok"
                 + (f" / max出力 {(m.get('top_provider') or {}).get('max_completion_tokens'):,} tok"
                    if (m.get('top_provider') or {}).get('max_completion_tokens') else ""))
    lines.append(f"- **Modality**: {arch.get('modality', '—')}"
                 f"  (in: {','.join(arch.get('input_modalities') or [])} →"
                 f" out: {','.join(arch.get('output_modalities') or [])})")

    # 価格行
    price_bits = [f"入力 {per_million(p.get('prompt'))}/1M",
                  f"出力 {per_million(p.get('completion'))}/1M"]
    if p.get("input_cache_read"):
        price_bits.append(f"キャッシュ読 {per_million(p['input_cache_read'])}/1M")
    if p.get("input_cache_write"):
        price_bits.append(f"キャッシュ書 {per_million(p['input_cache_write'])}/1M")
    if p.get("internal_reasoning"):
        price_bits.append(f"推論 {per_million(p['internal_reasoning'])}/1M")
    if p.get("image") and _f(p.get("image")):
        price_bits.append(f"画像 {raw_usd(p['image'])}/枚")
    if p.get("audio") and _f(p.get("audio")):
        price_bits.append(f"音声 {per_million(p['audio'])}/1M")
    if p.get("web_search") and _f(p.get("web_search")):
        price_bits.append(f"Web検索 {raw_usd(p['web_search'])}")
    for u in p.get("units") or []:
        if not u.get("price"):
            continue
        tiers = u.get("tiers") or []
        if tiers:
            lo = min(t["price"] for t in tiers)
            hi = max(t["price"] for t in tiers)
            val = f"${lo:g}" + (f"〜${hi:g}" if hi > lo else "")
        else:
            val = f"${u['price']:g}"
        price_bits.append(f"{u.get('label')} {val}{u.get('unit') or ''}")
    lines.append(f"- **Pricing**: {' · '.join(price_bits)}"
                 + ("  🆓" if is_free(m) else ""))

    caps = capabilities(m)
    if caps:
        lines.append(f"- **Capabilities**: {', '.join(caps)}")
    if m.get("knowledge_cutoff"):
        lines.append(f"- **Knowledge cutoff**: {m['knowledge_cutoff']}")
    lines.append(f"- **登録日**: {created_date(m)}")
    if m.get("hugging_face_id"):
        lines.append(f"- **HF**: `{m['hugging_face_id']}`")
    if m.get("supported_parameters"):
        lines.append(f"- **対応パラメータ**: {', '.join(m['supported_parameters'])}")

    desc = (m.get("description") or "").strip()
    if desc:
        if len(desc) > 700:
            desc = desc[:700].rsplit(" ", 1)[0] + " …"
        lines += ["", desc]
    lines.append("")
    return "\n".join(lines)


def full_report_md(models, fetched_at=""):
    total = len(models)
    free_n = sum(1 for m in models if is_free(m))
    providers = {}
    for m in models:
        providers.setdefault(provider_of(m), []).append(m)

    out = [f"# OpenRouter モデルカタログ（全{total}モデル）", ""]
    out.append(f"- 取得日時: {fetched_at or '—'}")
    out.append(f"- プロバイダ数: {len(providers)} / 無料枠あり: {free_n}")
    out.append("")

    # サマリ表（プロバイダ別）
    out.append("## プロバイダ別サマリ")
    out.append("")
    out.append("| Provider | モデル数 | 最安入力($/1M) | 最高入力($/1M) | 最大Context |")
    out.append("|---|--:|--:|--:|--:|")
    for prov in sorted(providers, key=lambda p: -len(providers[p])):
        ms = providers[prov]
        prices = [_f((m.get("pricing") or {}).get("prompt")) for m in ms]
        prices = [x for x in prices if x is not None and x >= 0]
        cmin = f"{min(prices)*1e6:,.2f}" if prices else "—"
        cmax = f"{max(prices)*1e6:,.2f}" if prices else "—"
        ctxmax = max((m.get("context_length") or 0) for m in ms)
        out.append(f"| {prov} | {len(ms)} | {cmin} | {cmax} | {ctxmax:,} |")
    out.append("")

    # 詳細（プロバイダ別、モデル名順）
    out.append("## モデル詳細")
    out.append("")
    for prov in sorted(providers):
        out.append(f"### ▎{prov}（{len(providers[prov])}）")
        out.append("")
        for m in sorted(providers[prov], key=lambda x: x["id"]):
            out.append(model_detail_md(m, level=4))
    return "\n".join(out)


def diff_report_md(d, old_label="", new_label=""):
    out = ["# OpenRouter モデル差分レポート", ""]
    out.append(f"- 比較元: {old_label}")
    out.append(f"- 比較先: {new_label}")
    out.append(f"- ➕ 新規: {len(d['added'])} / ➖ 削除: {len(d['removed'])} / 🔧 変更: {len(d['changed'])}")
    out.append("")

    if d["added"]:
        out.append(f"## ➕ 新規追加モデル（{len(d['added'])}）")
        out.append("")
        for m in d["added"]:
            out.append(model_detail_md(m, level=3))
    if d["removed"]:
        out.append(f"## ➖ 削除されたモデル（{len(d['removed'])}）")
        out.append("")
        for m in d["removed"]:
            out.append(f"- `{m['id']}` — {m.get('name','')}")
        out.append("")
    if d["changed"]:
        out.append(f"## 🔧 変更されたモデル（{len(d['changed'])}）")
        out.append("")
        for m, deltas in d["changed"]:
            out.append(f"### `{m['id']}`")
            for field, (a, b) in deltas.items():
                if field.startswith("price_"):
                    a, b = per_million(a), per_million(b)
                out.append(f"- **{field}**: `{a}` → `{b}`")
            out.append("")
    return "\n".join(out)


def export_site_data(models, fetched_at=""):
    """静的サイト用の整形済みJSON（リリース日=created 降順）を返す"""
    rows = []
    for m in models:
        arch = m.get("architecture") or {}
        p = m.get("pricing") or {}
        rows.append({
            "id": m["id"],
            "name": m.get("name", m["id"]),
            "provider": provider_of(m),
            "created": m.get("created"),
            "created_date": created_date(m),
            "context_length": m.get("context_length"),
            "max_output": (m.get("top_provider") or {}).get("max_completion_tokens"),
            "modality": arch.get("modality"),
            "input_modalities": arch.get("input_modalities") or [],
            "output_modalities": arch.get("output_modalities") or [],
            "price_in": price_num(p.get("prompt")),
            "price_out": price_num(p.get("completion")),
            "price_cache_read": price_num(p.get("input_cache_read")),
            "price_cache_write": price_num(p.get("input_cache_write")),
            "price_image": _f(p.get("image")) or None,
            "price_web_search": _f(p.get("web_search")) or None,
            "price_units": p.get("units") or None,
            "free": is_free(m),
            "caps": capabilities(m),
            "supported_parameters": m.get("supported_parameters") or [],
            "knowledge_cutoff": m.get("knowledge_cutoff"),
            "hugging_face_id": m.get("hugging_face_id"),
            "description": (m.get("description") or "").strip(),
        })
    rows.sort(key=lambda x: (x.get("created") or 0), reverse=True)  # 最新リリース順
    return {"fetched_at": fetched_at, "count": len(rows), "models": rows}


def write_report(md, name):
    os.makedirs(REPORT_DIR, exist_ok=True)
    ts = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = os.path.join(REPORT_DIR, f"{name}-{ts}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(md)
    return path


# ----------------------------------------------------------------------------
# 端末向けサマリ
# ----------------------------------------------------------------------------
def print_diff_summary(d):
    print(f"\n➕ 新規 {len(d['added'])} / ➖ 削除 {len(d['removed'])} / 🔧 変更 {len(d['changed'])}")
    for m in d["added"][:50]:
        free = " 🆓" if is_free(m) else ""
        print(f"  ➕ {m['id']}  ({per_million((m.get('pricing') or {}).get('prompt'))}"
              f"/{per_million((m.get('pricing') or {}).get('completion'))} per 1M){free}")
    if len(d["added"]) > 50:
        print(f"     … 他 {len(d['added'])-50} 件")
    for m in d["removed"][:50]:
        print(f"  ➖ {m['id']}")
    for m, deltas in d["changed"][:50]:
        fields = ", ".join(deltas.keys())
        print(f"  🔧 {m['id']}  [{fields}]")


# ----------------------------------------------------------------------------
# コマンド
# ----------------------------------------------------------------------------
def cmd_fetch(args):
    snaps = list_snapshots()
    prev = load_snapshot(snaps[-1]) if snaps else None
    print(f"取得中: {API_URL}")
    models = fetch_models()
    # 急減ガード: API変更やv1フォールバック時に縮小カタログを正として保存・コミットしない
    if prev is not None and not args.force and len(models) < len(prev) * 0.85:
        sys.exit(f"[異常] モデル数が {len(prev)} → {len(models)} に急減（15%超の減少）。"
                 f"API変更/フォールバックの可能性が高いため保存しません。--force で強制保存。")
    path = save_snapshot(models)
    print(f"保存: {os.path.relpath(path, BASE_DIR)}  ({len(models)} モデル)")
    if prev is None:
        print("（初回スナップショット。次回 fetch 時から差分を表示します）")
        return
    d = diff_snapshots(prev, models)
    n = len(d["added"]) + len(d["removed"]) + len(d["changed"])
    if n == 0:
        os.remove(path)  # 重複スナップショットは破棄（差分追跡を意味あるものに保つ／CIの無駄コミット防止）
        print("変更なし（スナップショットは破棄しました）")
        return
    print_diff_summary(d)
    if not args.no_report:
        rp = write_report(diff_report_md(d, os.path.basename(snaps[-1]),
                                         os.path.basename(path)), "diff")
        print(f"\n差分レポート: {os.path.relpath(rp, BASE_DIR)}")


def cmd_report(args):
    snaps = list_snapshots()
    if not snaps:
        sys.exit("スナップショットがありません。先に `fetch` を実行してください。")
    with open(snaps[-1], encoding="utf-8") as f:
        payload = json.load(f)
    models = payload.get("data", [])
    md = full_report_md(models, payload.get("fetched_at", ""))
    rp = write_report(md, "catalog")
    print(f"全{len(models)}モデルの詳細レポート: {os.path.relpath(rp, BASE_DIR)}")


def cmd_new(args):
    snaps = list_snapshots()
    if len(snaps) < 2:
        sys.exit("スナップショットが2つ以上必要です。`fetch` を2回以上実行してください。")
    d = diff_snapshots(load_snapshot(snaps[-2]), load_snapshot(snaps[-1]))
    print_diff_summary(d)
    rp = write_report(diff_report_md(d, os.path.basename(snaps[-2]),
                                     os.path.basename(snaps[-1])), "diff")
    print(f"\n差分レポート: {os.path.relpath(rp, BASE_DIR)}")


def cmd_diff(args):
    snaps = list_snapshots()
    if len(snaps) < 2:
        sys.exit("スナップショットが2つ以上必要です。")
    old = next((s for s in snaps if args.old in s), None)
    new = next((s for s in snaps if args.new in s), None)
    if not old or not new:
        sys.exit("指定スナップショットが見つかりません。`list` で確認してください。")
    d = diff_snapshots(load_snapshot(old), load_snapshot(new))
    print_diff_summary(d)
    rp = write_report(diff_report_md(d, os.path.basename(old), os.path.basename(new)), "diff")
    print(f"\n差分レポート: {os.path.relpath(rp, BASE_DIR)}")


def cmd_export(args):
    """最新スナップショットから site/models.json と catalog.md を書き出す"""
    snaps = list_snapshots()
    if not snaps:
        sys.exit("スナップショットがありません。先に `fetch` を実行してください。")
    with open(snaps[-1], encoding="utf-8") as f:
        payload = json.load(f)
    models = payload.get("data", [])
    data = export_site_data(models, payload.get("fetched_at", ""))
    with open(os.path.join(BASE_DIR, "models.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(BASE_DIR, "catalog.md"), "w", encoding="utf-8") as f:
        f.write(full_report_md(models, payload.get("fetched_at", "")))
    print(f"models.json 書き出し: {data['count']} モデル（リリース日降順, サイトルート）")
    print("catalog.md 書き出し完了")


def cmd_untranslated(args):
    """translations.json に未登録のモデルを抽出（差分翻訳用）。untranslated.json に翻訳用データを書き出す。"""
    snaps = list_snapshots()
    if not snaps:
        sys.exit("スナップショットがありません。先に `fetch` を実行してください。")
    models = load_snapshot(snaps[-1])
    tx_path = os.path.join(BASE_DIR, "translations.json")
    tx = {}
    if os.path.exists(tx_path):
        with open(tx_path, encoding="utf-8") as f:
            tx = json.load(f)
    missing = [m for m in models if m["id"] not in tx]
    print(f"未翻訳: {len(missing)} / {len(models)}")
    for m in missing[:60]:
        print(f"  {m['id']}")
    if missing:
        arch = lambda m: m.get("architecture") or {}
        out = [{
            "id": m["id"], "name": m.get("name"), "provider": provider_of(m),
            "io": "+".join(arch(m).get("input_modalities") or []) + " -> "
                  + "+".join(arch(m).get("output_modalities") or []),
            "ctx": m.get("context_length"),
            "price_in": price_num((m.get("pricing") or {}).get("prompt")),
            "price_out": price_num((m.get("pricing") or {}).get("completion")),
            "caps": capabilities(m),
            "desc": (m.get("description") or "")[:1100],
        } for m in missing]
        p = os.path.join(BASE_DIR, "untranslated.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        print(f"\n翻訳用データ: {os.path.relpath(p, BASE_DIR)}（このファイルを翻訳して translations.json にマージ）")


def cmd_list(args):
    snaps = list_snapshots()
    if not snaps:
        print("スナップショットなし。")
        return
    for s in snaps:
        try:
            with open(s, encoding="utf-8") as f:
                payload = json.load(f)
            print(f"  {os.path.basename(s)}  —  {payload.get('count','?')} モデル  "
                  f"({payload.get('fetched_at','')})")
        except (OSError, ValueError):
            print(f"  {os.path.basename(s)}  (読み込み失敗)")


def cmd_show(args):
    snaps = list_snapshots()
    if not snaps:
        sys.exit("スナップショットがありません。")
    models = load_snapshot(snaps[-1])
    hits = [m for m in models if args.id.lower() in m["id"].lower()]
    if not hits:
        sys.exit(f"'{args.id}' に一致するモデルなし。")
    for m in hits[:10]:
        print(model_detail_md(m, level=2))
    if len(hits) > 10:
        print(f"… 他 {len(hits)-10} 件（IDを具体的に）")


def main():
    ap = argparse.ArgumentParser(description="OpenRouter モデル取得/詳細/差分追跡ツール")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("fetch", help="最新取得 + 差分表示")
    p.add_argument("--no-report", action="store_true", help="差分レポートmdを生成しない")
    p.add_argument("--force", action="store_true", help="モデル数が急減していても保存する")
    p.set_defaults(func=cmd_fetch)

    sub.add_parser("report", help="全モデル詳細レポート生成").set_defaults(func=cmd_report)
    sub.add_parser("new", help="直近2スナップショットの差分").set_defaults(func=cmd_new)
    sub.add_parser("export", help="静的サイト用データ(site/)を書き出し").set_defaults(func=cmd_export)
    sub.add_parser("untranslated", help="未翻訳モデルを抽出(差分翻訳用)").set_defaults(func=cmd_untranslated)
    sub.add_parser("list", help="スナップショット一覧").set_defaults(func=cmd_list)

    p = sub.add_parser("diff", help="2スナップショット間の差分")
    p.add_argument("old"); p.add_argument("new")
    p.set_defaults(func=cmd_diff)

    p = sub.add_parser("show", help="モデルIDで詳細表示")
    p.add_argument("id")
    p.set_defaults(func=cmd_show)

    args = ap.parse_args()
    try:
        args.func(args)
    except urllib.error.URLError as e:
        sys.exit(f"ネットワークエラー: {e}")


if __name__ == "__main__":
    main()

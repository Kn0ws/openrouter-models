# OpenRouter Models カタログ

[OpenRouter](https://openrouter.ai/) で **現在使用可能な全モデル**（チャットだけでなく画像生成・音声・動画・埋め込み・rerank も含む）を **検索・ソート・絞り込みできる静的サイト**。
データは OpenRouter のフロントエンドAPI（`/api/frontend/v1/catalog/models`、認証不要）から取得し、提供エンドポイントを持つモデルのみを **リリース日（新しい順）** で並べています。※公開APIの `/api/v1/models` はテキスト出力中心のサブセットで画像生成系等が欠落するため、こちらを採用（v1へのフォールバック付き）。

🔗 **サイト**: https://kn0ws.github.io/openrouter-models/  ←（公開後にここで閲覧）

## 機能

- 🔎 フリーワード検索（モデル名 / ID / 提供元 / 英語説明 / 日本語解説）
- ↕️ 並び替え：リリース日↓↑ / 入力単価↑↓ / コンテキスト長↓ / 名前
- 🎛️ **入力→出力モダリティで絞り込み**（例「入力：テキスト × 出力：画像」。複数モダリティ対応モデルも該当すれば含む）
- 🏷️ 絞り込み：プロバイダ、🆓無料のみ、🔧ツール、🧠推論
- 🇯🇵 詳細クリックで **日本語の解説 ＋「得意なこと・特徴」** を表示（原文も展開可）
- 各モデルの価格（$/100万トークン 入力/出力・キャッシュ）、コンテキスト長、モダリティ、対応パラメータ

## ファイル

| ファイル | 内容 |
|---|---|
| `index.html` | 検索可能な静的サイト本体（依存ライブラリなし） |
| `models.json` | 整形済みモデルデータ（リリース日降順） |
| `translations.json` | モデルIDごとの日本語解説（`desc_ja`）と得意分野（`good_at`） |
| `catalog.md` | 全モデルの詳細を1枚にまとめた Markdown 版 |
| `or_models.py` | 取得・差分追跡・書き出しを行う CLI（Python標準ライブラリのみ） |
| `snapshots/` | 取得時点ごとの生データ（差分追跡用の履歴） |
| `.github/workflows/update.yml` | 毎日自動で再取得し、変更があればコミット |

## 更新のしかた

```bash
python3 or_models.py fetch         # 最新取得＋前回スナップショットとの差分を表示（変更が無ければ破棄）
python3 or_models.py translate     # 未翻訳だけを安全な構造化出力で日本語化
python3 or_models.py export        # index.html 用に models.json / catalog.md を再生成
python3 or_models.py untranslated  # 日本語訳が無いモデルを抽出（→ untranslated.json）
git add -A -- snapshots models.json catalog.md translations.json && git commit -m "update models" && git push
```

`fetch` は取得のたびにスナップショットを保存し、**新規 / 削除 / 価格・コンテキスト・対応パラメータの変更** を差分検出します（毎日 GitHub Action でも自動実行）。

新しく増えたモデルは、GitHub Actions の定期取得で未訳分だけを自動翻訳してから公開します。ローカルで候補だけ確認する場合は `python3 or_models.py translate --dry-run` を使えます。

### 自動翻訳の安全設定

自動翻訳は OpenRouter の `openai/gpt-4o-mini` を固定で使います。入力として送るのは、公開済みカタログのモデルID・名称・モダリティ・対応機能・英語説明だけです。リポジトリの設定、環境変数、利用者データは送信しません。

有効化前に、次の**翻訳専用の通常APIキー**を作成し、GitHub Actions の Repository secret `OPENROUTER_TRANSLATION_API_KEY` に設定してください。

- 管理キー・プロビジョニングキーは不可。推論専用キーにする。
- `limit` は **1 USD 以下**、`limit_reset` は **monthly** にする。可能なら有効期限も設定する。
- OpenRouter の Guardrail を使える場合は、同じキーに `openai/gpt-4o-mini` だけを許可し、データ収集を拒否する。
- Secret は Actions Secret にだけ保存し、リポジトリ・Issue・ログ・環境変数ファイルへ書かない。

ワークフローは新規・保留中を含む未訳を毎回最大20モデル、1モデルあたり1リクエスト（自動再試行なし）で処理します。20件を超える場合は訳文バッチとスナップショットだけを保存し、次回実行で続きから処理します。`models.json` と `catalog.md` は未訳がゼロになった時だけ更新するため、英語だけの新モデルを公開しません。モデル・送信先・スキーマ・出力長はコードで固定し、構造化出力をローカルでも検証します。キーが未設定・管理キー・上限超過・API失敗・不正な応答のいずれでも、そのバッチの `translations.json` を変更せず公開を停止します（fail-closed）。

手動実行・再実行はリポジトリ所有者だけに制限しています。Secret 設定後は Actions の **Run workflow** で `verify_translation_key` を有効にすると、推論や公開をせずキーの種類・利用上限だけを確認できます。

このワークフローの条件は、`main` を直接変更できる人がワークフロー自体を書き換えることまでは防げません。Repository settings では `main` への書き込み権限を最小化し、利用可能なら GitHub Actions の **Policies / Workflow execution protections** で所有者だけを許可してください。

## ローカルプレビュー

`fetch('models.json')` を使うため、`file://` ではなく HTTP で開いてください。

```bash
python3 -m http.server 8799
# → http://localhost:8799/
```

---
データ出典: OpenRouter（価格・仕様は各モデルの提供元に準拠）。本リポジトリはミラー/閲覧用です。

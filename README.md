# OpenRouter Models カタログ

[OpenRouter](https://openrouter.ai/) で利用可能な全モデルを **検索・ソートできる静的サイト**。
データは OpenRouter 公開API（`/api/v1/models`、認証不要）から取得し、**リリース日（新しい順）** で並べています。

🔗 **サイト**: https://kn0ws.github.io/  ←（公開後にここで閲覧）

## 機能

- 🔎 フリーワード検索（モデル名 / ID / 提供元 / 説明文）
- ↕️ 並び替え：リリース日↓↑ / 入力単価↑↓ / コンテキスト長↓ / 名前
- 🏷️ 絞り込み：プロバイダ、🆓無料のみ、🖼️画像入力、🔧ツール、🧠推論
- 各モデルの価格（$/100万トークン 入力/出力・キャッシュ）、コンテキスト長、モダリティ、対応パラメータ、説明

## ファイル

| ファイル | 内容 |
|---|---|
| `index.html` | 検索可能な静的サイト本体（依存ライブラリなし） |
| `models.json` | 整形済みモデルデータ（リリース日降順） |
| `catalog.md` | 全モデルの詳細を1枚にまとめた Markdown 版 |
| `or_models.py` | 取得・差分追跡・書き出しを行う CLI（Python標準ライブラリのみ） |
| `snapshots/` | 取得時点ごとの生データ（差分追跡用の履歴） |

## 更新のしかた

```bash
python3 or_models.py fetch     # 最新取得＋前回スナップショットとの差分を表示
python3 or_models.py export    # index.html 用に models.json / catalog.md を再生成
git add -A && git commit -m "update models" && git push
```

`fetch` は取得のたびにスナップショットを保存し、**新規 / 削除 / 価格・コンテキスト・対応パラメータの変更** を差分検出します。

## ローカルプレビュー

`fetch('models.json')` を使うため、`file://` ではなく HTTP で開いてください。

```bash
python3 -m http.server 8799
# → http://localhost:8799/
```

---
データ出典: OpenRouter（価格・仕様は各モデルの提供元に準拠）。本リポジトリはミラー/閲覧用です。

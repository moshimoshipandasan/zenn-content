title: "自然言語だけでプログラミング！Vibecodingをはじめよう②"
emoji: "🛠️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics:
  - "ai"
  - "zenn"
  - "github"
  - "codex"
  - "vibecoding"
published: false
---

## ゴール
Codex CLI の環境設定を「安全・再現可能」に整える。以後はこの設定で記事やコード編集を進める。

## 必要条件
- Node.js/npm が利用可能（`node -v`, `npm -v` で確認）
- 本リポジトリを手元にクローン済み（前章から継続）

## 手順（Step by step）
1) 依存を入れる

```bash
npm install
```

2) Codex CLI を起動（通常モード）

```bash
codex
```

ブラウザで OpenAI 認証を完了する案内に従う。

![](/images/2024-10-12vibecoding/image24.png)

3) Approvals を設定（自動操作の安全ガード）

```text
/approvals
```

- 推奨: `on-failure` もしくは `on-request`
- 読み取りは許可、書き込み系はレビュー必須
- 削除やリセット等の破壊的操作は常に手動確認

![](/images/2024-10-12vibecoding/image25.png)

4) 作業ブランチを用意

```bash
git switch -c docs/article-edit-YYYY-MM-DD
```

5) Zenn プレビューで動作確認

```bash
npx zenn preview   # http://localhost:8000
```

チェック: レンダリング、リンク、画像パス、Front Matter（`published: false`）。

![](/images/2024-10-12vibecoding/image26.png)

## 補足コマンド
- `/status` 現在のセッション構成を表示
- `/model` モデル/Reasoning の切替
- `/review` 変更点レビュー

## よくあるつまずき
- 権限エラー: `/approvals` で必要最小限のみ許可
- 画像が出ない: `/images/<記事フォルダ>/...` へのパスを再確認
- 文字化け: ファイルのエンコーディングを UTF-8 に統一

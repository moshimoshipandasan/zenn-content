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

## この章のゴール
Codex CLI の環境設定を完了し、「安全に編集できる状態」で記事やドキュメントを進められるようにします。

![](/images/2024-10-12vibecoding/image24.png)

## 前提
- Node.js と npm がインストール済み
- GitHub リポジトリを用意（前章の続き）
- Zenn 環境は `npm install` 済み

## Codex CLI を起動
通常は YOLO を使わず、安全モードで起動します（全消し事故を防ぐ）。

```bash
codex
```

起動後、ターミナルに案内される URL で OpenAI にログインします（未認証の場合）。

## Approvals（権限）を設定
Codex が自動実行できる操作範囲を絞ります。おすすめは「on-failure」または「on-request」。

```text
/approvals
```

- `read` は許可、書き込みはレビューありにする
- 破壊的操作（`rm -rf` 等）は常に手動確認

![](/images/2024-10-12vibecoding/image25.png)

## 作業ブランチを運用
編集は必ずトピックブランチで行います。

```bash
git switch -c docs/article-edit-YYYY-MM-DD
```

## プロジェクトの下準備（Zenn）
リポジトリ直下で必要なコマンドを確認します。

```bash
npm install
npx zenn preview   # http://localhost:8000
```

チェックリスト：レンダリング、内部/外部リンク、画像パス、Front Matter（`published: false` で下書き管理）。

![](/images/2024-10-12vibecoding/image26.png)

## 推奨ワークフロー
1. ブランチ作成 → `articles/` を編集
2. `npx zenn preview` で確認（崩れ・リンク切れ）
3. 小さくコミット（Conventional Commits）
4. PR を作成しレビュー依頼 → Squash merge

## トラブルシューティング
- Codex の権限で失敗する: `/approvals` を開き、必要な操作だけを一時的に許可
- 画像が表示されない: パスは `/images/<記事用フォルダ>/...` になっているか確認
- 文字化け: Markdown を UTF-8 で保存

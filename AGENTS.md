# Repository Guidelines

## Project Structure & Module Organization
- `articles/` Zenn記事。命名は `YYYY-MM-DDslug.md`（例: `2024-10-11vibecoding.md`）。
- `books/` Zenn本用。開始時にサブディレクトリ＋`config.yml` と `chapters/` を作成。
- `images/` 画像資産。記事ごとにサブフォルダ（例: `images/vibecoding-intro/`）を作成し、`topic-01.png` のように連番で管理。
- `node_modules/` は依存物（手動で編集しない）。
- ルート: `package.json`, `README.md`, `.gitignore`, `AGENTS.md`。

## Build, Test, and Development Commands
- `npm install` 依存をインストール（`zenn-cli` をセットアップ）。
- `npx zenn new:article` 新規記事のひな型を作成（例: `vibecoding-intro`）。
- `npx zenn new:book` 本のディレクトリ構成を作成。
- `npx zenn preview` ローカルプレビュー（http://localhost:8000）。表示崩れ・リンク切れを確認。

## Coding Style & Naming Conventions
- MarkdownはUTF-8、見出しは文頭のみ大文字のSentence case、1行120文字目安。
- Front Matter: 2スペースインデント、絵文字は引用符で囲む、`topics` は小文字。`published: false` で下書き管理。
- ファイル/ブランチ/スラッグは `lowercase-with-hyphens`。画像は意味ある接頭辞＋2桁連番（例: `setup-01.png`）。
- 画像参照は `/images/...` もしくは記事相対（例: `![](/images/vibecoding-intro/setup-01.png)`）。

## Testing Guidelines
- 自動テストは未設定。動作確認はプレビュー中心。
- チェックリスト: レンダリング、内部/外部リンク、画像パス、Front Matter（不要な`publication_name`は入れない）。
- レイアウト修正を伴うPRはスクリーンショットを添付。

## Commit & Pull Request Guidelines
- Conventional Commits を採用（`feat:`, `fix:`, `docs:`, `chore:` など）。小さく頻繁に。
- PRには目的、主な変更点、確認手順（`npx zenn preview`）、必要に応じてスクショ/関連Issueリンクを記載。
- 原則Squash merge。履歴を読みやすく保つ。

## Security & Configuration Tips
- 秘密情報（トークン・鍵）をコミットしない。大容量バイナリは避け、画像はWeb最適化（目安 < 1MB）。
- `node_modules/` は追跡しない（`.gitignore`維持）。行末や改行差分が多い場合は`.gitattributes`で正規化を検討。

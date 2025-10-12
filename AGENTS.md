# Repository Guidelines

## Project Structure & Module Organization
- `articles/` Zenn記事。命名は `YYYY-MM-DDslug.md`（例: `2024-10-11vibecoding.md`）。
- `books/` Zenn本用ディレクトリ（`<book-slug>/config.yml` と `chapters/`）。
- `images/` 画像資産。記事ごとにサブフォルダ（例: `images/vibecoding-intro/`）を作成し、`topic-01.png` のように連番管理。
- ルート: `package.json`, `README.md`, `.gitignore`, `AGENTS.md`。`node_modules/` は依存物（手動編集しない）。

## Build, Test, and Development Commands
- `npm install` 依存をインストール（`zenn-cli` をセットアップ）。
- `npx zenn new:article` 記事の雛形を作成（例: `--slug vibecoding-intro`）。
- `npx zenn new:book` 本のディレクトリ構成を作成。
- `npx zenn preview` ローカルプレビュー（http://localhost:8000）。レイアウト/リンク/画像を確認。

## Coding Style & Naming Conventions
- Markdown: UTF-8、見出しは Sentence case、1行120文字目安。
- Front Matter: 2スペース、絵文字は引用符で囲む、`topics` は小文字、下書きは `published: false`。
- 命名: スラッグ/ブランチ/ファイルは `lowercase-with-hyphens`。画像は意味ある接頭辞＋2桁連番（例: `setup-01.png`）。
- 画像参照は `/images/...` または記事相対（例: `![](/images/vibecoding-intro/setup-01.png)`）。

## Testing Guidelines
- 自動テストは未設定。プレビュー中心の目視確認。
- チェックリスト: レンダリング、内部/外部リンク、画像パス、Front Matter（`publication_name` は入れない）。

## Commit & Pull Request Guidelines
- Conventional Commits（例: `feat:`, `fix:`, `docs:`, `chore:`）。小さく頻繁に。
- ブランチ例: `docs/article-edit-YYYY-MM-DD`。PR には目的、主要変更点、確認手順（`npx zenn preview`）、必要に応じてスクリーンショットと関連Issue。
- マージは原則 Squash merge。履歴を読みやすく保つ。

## Security & Configuration Tips
- 秘密情報（トークン/鍵）をコミットしない。大容量バイナリは避け、画像は Web 最適化（目安 < 1MB）。
- `node_modules/` は追跡しない（`.gitignore` を維持）。改行差分が多い場合は `.gitattributes` で正規化を検討。

## Agent-Specific Instructions
- Codex CLI 利用時は `/approvals` で権限を制御（通常は `on-failure` か `on-request`）。
- 生成物の配置は本ガイドの構成に従う。破壊的操作は事前に合意を得る。
- レイアウト変更を含む PR にはスクリーンショットを添付し、確認手順を明記。

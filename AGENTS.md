# Repository Guidelines

## Project Structure & Module Organization
- `articles/` Zenn記事（`YYYY-MM-DDslug.md` 例: `2024-10-11vibecoding.md`）。
- `books/` Zenn本。作成時に `<book-slug>/config.yml` と `chapters/` を用意。
- `images/` 画像資産。記事ごとにサブフォルダ（例: `images/vibecoding-intro/`）を作成し、`topic-01.png` のように連番管理。
- ルート: `package.json`, `README.md`, `.gitignore`, `AGENTS.md`。`node_modules/` は依存物（手動編集しない）。

## Build, Test, and Development Commands
- `npm install` 依存をインストール（`zenn-cli` をセットアップ）。
- `npx zenn new:article` 新規記事のひな型作成（例: `vibecoding-intro`）。
- `npx zenn new:book` 本のディレクトリ構成を作成。
- `npx zenn preview` ローカルプレビュー（http://localhost:8000）。表示崩れ・リンク切れを確認。

## Coding Style & Naming Conventions
- MarkdownはUTF‑8、見出しはSentence case（文頭のみ大文字）、1行120文字目安。
- Front Matter: 2スペースインデント、絵文字は引用符で囲む、`topics` は小文字、下書きは `published: false`。
- スラッグ/ファイル名は `lowercase-with-hyphens`。画像は意味ある接頭辞＋2桁連番（例: `setup-01.png`）。
- 画像参照は `/images/...` もしくは記事相対（例: `![](/images/vibecoding-intro/setup-01.png)`）。

## Testing Guidelines
- 自動テストは未設定。動作確認は `npx zenn preview` を用いた目視確認。
- チェックリスト: レンダリング、内部/外部リンク、画像パス、Front Matter（`publication_name` は入れない）。

## Commit & Pull Request Guidelines
- Conventional Commits（例: `feat:`, `fix:`, `docs:`, `chore:`）。小さく頻繁に。
- PRには目的、主な変更点、確認手順（`npx zenn preview`）、必要に応じてスクリーンショット/関連Issueリンク。
- マージは原則Squash mergeで履歴を簡潔に。

## Security & Configuration Tips
- 秘密情報（トークン/鍵）をコミットしない。大容量バイナリは避け、画像はWeb最適化（目安 < 1MB）。
- `node_modules/` は追跡しない（`.gitignore` を維持）。行末/改行差分が多い場合は `.gitattributes` で正規化を検討。

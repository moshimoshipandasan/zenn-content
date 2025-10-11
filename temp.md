# GitHub CodespacesでCodexを起動する手順

## 前提条件
- GitHub アカウント（Codespaces 対応のサブスクリプション）
- 対象の GitHub リポジトリ（このリポジトリを想定）
- ブラウザで [Codex Redirect URL ジェネレーター](https://bazaarjapan.github.io/codex-redirect-url/) にアクセスできること

## 1. GitHub リポジトリから Codespaces を起動
1. GitHub 上で対象リポジトリを開く。
2. 緑色の `Code` ボタン → `Codespaces` タブを選択。
3. `Create codespace on main` などのボタンを押して、Codespace を新規作成。
4. ブラウザ上で Codespaces 環境が立ち上がるのを待つ。

## 2. ターミナルの準備
1. Codespaces 画面下部の `Terminal` パネルを開く（表示されない場合は `Terminal > New Terminal`）。
2. プロンプトが `/workspaces/<リポジトリ名>` であることを確認。

## 3. Codex CLI のインストール
ターミナルで以下を実行して Codex CLI をグローバルインストールする：

```bash
npm install -g @openai/codex
```

インストールが完了すると `codex` コマンドが利用できるようになる。

## 4. Codex の起動と認証
1. Codex を YOLO モードで起動：

   ```bash
   codex --yolo
   ```

2. ターミナルに OpenAI ログイン用の OAuth 認証 URL が表示される。
3. 表示された URL をコピーし、ブラウザで [Codex Redirect URL ジェネレーター](https://bazaarjapan.github.io/codex-redirect-url/) を開く。
4. フォームにコピーした URL を貼り付け、「Generate」ボタンを押す。
5. 生成されたリダイレクト URL をコピーして、ターミナルに貼り付け、Enter キーを押す。
6. ブラウザで OpenAI ログイン → 認証を完了する。

## 5. Codex 利用開始
- 認証が成功すると、ターミナルの Codex CLI がアクティブになり、プロンプトが Codex 用に切り替わる。
- 必要なコマンド（例：`help` で概要を確認）を実行して開発を継続。

## トラブルシューティング
- インストール時に `permission denied` が出る場合は、`npm` コマンドに `--unsafe-perm` を付与するか、`nvm` などで適切な Node.js 環境を再構築する。
- Codespaces のセッションがタイムアウトすると認証トークンも無効化されるため、再認証が必要になることがある。
- `codex --yolo` が途中で終了した場合は、もう一度コマンドを実行して認証ステップからやり直す。
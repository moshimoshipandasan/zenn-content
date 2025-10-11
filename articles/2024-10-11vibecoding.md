---
title: "はじめてのVibecoding"
emoji: "🌊"
type: "idea" # tech: 技術記事 / idea: アイデア
topics: 
  - "ai"
  - "Zenn"
  - "github"
  - "codex"
  - "vibecoding"
published: false
publication_name: "publication"
published_at: "2025-10-11 00:00"
---
## Vibecodingとは
Vibecodingは、完璧さよりも「流れ（バイブ）」を大切にし、短いサイクルで学びとアウトプットを積み重ねていくスタイルのコーディング習慣です。難しい設計より、いま手を動かせる小さな一歩を優先し、記録を残して次の一歩につなげます。

- 小さく始めて、小さく進める（5〜50分の短いセッション）
- 迷ったら記録する（READMEや日次ログ、Issue）
- 完璧さより継続を重視（毎回なにか1つ進める）

### なぜ初心者に向いている？
- つまずいても止まりにくい：小さな成功を積み重ねられる
- 何をやったかが残る：後から復習や質問がしやすい
- モチベーションが保ちやすい：進捗が見える

## 準備 — GitHubアカウントを作成（Google認証）
1. ブラウザで https://github.co.jp を開き、「サインアップ」をクリック。
![](/images/image01.png)
2. 「Continue with Google」をクリックし、Googleアカウントで認証します（2段階認証が有効なら案内に従います）。
![](/images/image02.png)
![](/images/image03.png)
3. ユーザー名を決めます（英数字とハイフン、短く覚えやすく）。
![](/images/image04.png)
4. 届いた確認メールのリンクを開いて登録を完了します。

### 基本設定（推奨）
- 右上アイコン → Settings → Profile：自己紹介とアイコンを設定
- Settings → Emails：「Keep my email addresses private」を有効化
- Settings → SSH and GPG keys：後でローカルからGitを使う場合は公開鍵を登録

## 初めてのリポジトリを作る
1. 右上の「＋」→ New repository。
![](/images/image06.png)
2. Repository name 例：`my-first-code`（Public推奨）。
![](/images/image07.png)
3. 「Add a README file」をOnにする。
4. Create repository で作成。
![](/images/image08.png)


## 次の一歩 — CodespacesでCodex CLIを起動

## 前提条件
- GitHub アカウント（Codespaces 対応のサブスクリプション）
- 対象の GitHub リポジトリ（このリポジトリを想定）
- ブラウザで [Codex Redirect URL ジェネレーター](https://bazaarjapan.github.io/codex-redirect-url/) にアクセスできること

## 1. GitHub リポジトリから Codespaces を起動
1. GitHub 上で対象リポジトリを開く。
2. 緑色の「Code」ボタン → 「Codespaces」タブを選択。
![](/images/image09.png)
3. 「main で Codespaces を作成」（英語UIでは `Create codespace on main`）を押して、Codespaces を新規作成。
4. ブラウザ上で Codespaces 環境が立ち上がるのを待つ。
![](/images/image10.png)

## 2. ターミナルの準備
1. Codespaces 画面下部の「ターミナル」パネルを開く（表示されない場合は、メニュー「ターミナル」→「新しいターミナル」を選択）。
2. プロンプトが `/workspaces/<リポジトリ名>` であることを確認。

## 3. Codex CLI のインストール
ターミナルで以下を実行して Codex CLI をグローバルインストールする：

```bash
npm install -g @openai/codex
```
![](/images/image11.png)
![](/images/image12.png)

インストールが完了すると `codex` コマンドが利用できるようになる。

## 4. Codex の起動と認証
1. Codex を YOLO モードで起動：

   ```bash
   codex --yolo
   ```
![](/images/image13.png)
![](/images/image14.png)
![](/images/image15.png)
![](/images/image16.png)
![](/images/image17.png)

2. ターミナルに OpenAI ログイン用の OAuth 認証 URL が表示される。
![](/images/image18.png)

3. 表示された URL をコピーし、ブラウザで [Codex Redirect URL ジェネレーター](https://bazaarjapan.github.io/codex-redirect-url/) を開く。

4. フォームにコピーした URL を貼り付け、「コードを生成」ボタンを押す。
![](/images/image19.png)
5. 生成されたリダイレクト URL をコピーして、ターミナルに貼り付け、Enter キーを押す。
![](/images/image20.png)
![](/images/image21.png)
![](/images/image22.png)

6. ブラウザで OpenAI ログイン → 認証を完了する。

## 5. Codex 利用開始
- 認証が成功すると、ターミナルの Codex CLI がアクティブになり、プロンプトが Codex 用に切り替わる。
- 必要なコマンド（例：`help` で概要を確認）を実行して開発を継続。

## トラブルシューティング
- インストール時に `permission denied` が出る場合は、`npm` コマンドに `--unsafe-perm` を付与するか、`nvm` などで適切な Node.js 環境を再構築する。
- Codespaces のセッションがタイムアウトすると認証トークンも無効化されるため、再認証が必要になることがある。
- `codex --yolo` が途中で終了した場合は、もう一度コマンドを実行して認証ステップからやり直す。



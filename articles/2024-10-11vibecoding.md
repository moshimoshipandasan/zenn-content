---
title: "自然言語だけでプログラミング！Vibecodingをはじめよう①"
emoji: "📘"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: 
  - "ai"
  - "Zenn"
  - "github"
  - "codex"
  - "vibecoding"
published: true
published_at: "2025-10-11 00:00"
---
## Vibecodingとは
ノリとアイデアでつくる、AI時代のプログラミング。

**楽しさ（Vibe）を感じながらコードを書く（Coding）**という意味、日本語だけである程度高度なプログラミングができます。


### なぜ初心者に向いている？
- つまずいても止まりにくい：小さな成功を積み重ねられる
- 何をやったかが残る：後から復習や質問がしやすい
- モチベーションが保ちやすい：進捗が見える

## 最初の一歩 — GitHubアカウントを作成（Google認証）しよう！
1. ブラウザで https://github.co.jp を開き、「サインアップ」をクリック。
![](/images/2024-10-11vibecoding/image01.png)

2. 「Continue with Google」をクリックし、Googleアカウントで認証します（2段階認証が有効なら案内に従います）。
![](/images/2024-10-11vibecoding/image02.png)
---
![](/images/2024-10-11vibecoding/image03.png)

3. ユーザー名を決めます（英数字とハイフン、短く覚えやすく）。
![](/images/2024-10-11vibecoding/image04.png)

### 基本設定（後でやっておこう！）
- 右上アイコン → Settings → Profile：自己紹介とアイコンを設定
- Settings → Emails：「Keep my email addresses private」を有効化
- Settings → SSH and GPG keys：後でローカルからGitを使う場合は公開鍵を登録

## 初めてのリポジトリを作る
1. 右上の「＋」→ New repository。
![](/images/2024-10-11vibecoding/image06.png)

2. Repository name 例：`my-first-code`（Public推奨）。
![](/images/2024-10-11vibecoding/image07.png)

3. 「Add a README file」をOnにする。

4. Create repository で作成。
![](/images/2024-10-11vibecoding/image08.png)
リポジトリが作成されると上機能ような画面になります。


## 次の一歩 — CodespacesでCodex CLIを起動

## 前提条件
- GitHub アカウント（Codespaces 対応のサブスクリプション）
- 対象の GitHub リポジトリ（このリポジトリを想定）
- ブラウザで [Codex Redirect URL ジェネレーター](https://bazaarjapan.github.io/codex-redirect-url/) にアクセスできること

## 1. GitHub リポジトリから Codespaces を起動
1. GitHub 上で対象リポジトリを開く。

2. 緑色の「Code」ボタン → 「Codespaces」タブを選択。
![](/images/2024-10-11vibecoding/image09.png)

3. 「main で Codespaces を作成」（英語UIでは `Create codespace on main`）を押して、Codespaces を新規作成。

4. ブラウザ上で Codespaces 環境が立ち上がるのを待つ。
![](/images/2024-10-11vibecoding/image10.png)

## 2. ターミナルの準備
1. Codespaces 画面下部の「ターミナル」パネルを開く（表示されない場合は、メニュー「ターミナル」→「新しいターミナル」を選択）。
2. プロンプトが `/workspaces/<リポジトリ名>` であることを確認。

## 3. Codex CLI のインストール
ターミナルで以下を実行して Codex CLI をグローバルインストールする：

```bash
npm install -g @openai/codex@latest
```
![](/images/2024-10-11vibecoding/image11.png)

![](/images/2024-10-11vibecoding/image12.png)

- インストールが完了すると `codex` コマンドが利用できるようになる。

## 4. Codex の起動と認証
1. Codex を YOLO モードで起動：

   ```bash
   codex --yolo
   ```
![](/images/2024-10-11vibecoding/image13.png)
- デスクトップ環境などでCodexを起動する場合は`--yolo`オプションは付けずに`codex`だけで起動しましょう。yoloモードはすべのファイルの編集権限がCodex与えられるので重要なファイルを削除してしまう場合があります。現在のCodespaces環境ではシステムが消えても問題ないのでyoloモードで起動しています。
---
![](/images/2024-10-11vibecoding/image14.png)
- 1. Sign in with ChatGPTを選ぶ
![](/images/2024-10-11vibecoding/image15.png)

![](/images/2024-10-11vibecoding/image16.png)

![](/images/2024-10-11vibecoding/image17.png)

2. ターミナルに OpenAI ログイン用の OAuth 認証 URL が表示される。
![](/images/2024-10-11vibecoding/image18.png)

3. 表示された URL をコピーし、ブラウザで [Codex Redirect URL ジェネレーター](https://bazaarjapan.github.io/codex-redirect-url/) を開く。

4. ジェネレーターのリダイレクトURLの欄にコピーした URL を貼り付け、「コードを生成」ボタンを押す。
![](/images/2024-10-11vibecoding/image19.png)

5. 生成されたリダイレクト URL をコピーして、ターミナルに貼り付け、キーボードの Enter キーを押す。
![](/images/2024-10-11vibecoding/image20.png)
- ①を貼り付けてキーボードの Enter キーを押す。
![](/images/2024-10-11vibecoding/image21.png)
- ②を貼り付けてキーボードの Enter キーを押す。
![](/images/2024-10-11vibecoding/image22.png)

6. ブラウザで OpenAI ログイン → 認証を完了する。
![](/images/2024-10-11vibecoding/image22-1.png)

## 5. Codex 利用開始
- 認証が成功すると、ターミナルの Codex CLI がアクティブになり、プロンプトが Codex 用に切り替わる。
![](/images/2024-10-11vibecoding/image22-1-1.png)
- ゴミ箱のマークをクリックしてbash消す
![](/images/2024-10-11vibecoding/image22-2.png)

| コマンド         | 説明                                                            |
| ------------ | ------------------------------------------------------------- |
| `/init`      | Codexの設定手順が記載された **AGENTS.md** ファイルを新規作成します。初期セットアップ用のコマンドです。 |
| `/status`    | 現在のセッション構成（使用中のモデルや設定など）を表示します。                               |
| `/approvals` | Codexがユーザーの承認なしで実行できる操作を設定・選択します。                             |
| `/model`     | 使用するAIモデルおよび推論の強度（Reasoning Effort）を選択します。                    |
| `/review`    | これまでの変更点をレビューし、問題点や修正箇所を確認します。                                |


## トラブルシューティング
- Codespaces のセッションがタイムアウトすると認証トークンも無効化されるため、再認証が必要になることがあるのでGitHubの右上のアイコンをクリックしSettingから左側メニューのCodespacesよりDefault idle timeoutの時間を30分から120分に変更するとよい。
![](/images/2024-10-11vibecoding/image23.png)

- `codex --yolo` が途中で終了した場合は、もう一度コマンドを実行して認証ステップからやり直す。
- デスクトップ環境などでCodexを起動する場合は`--yolo`オプションは付けずに`codex`だけで起動しましょう。yoloモードはすべのファイルの編集権限がCodex与えられるので重要なファイルを削除してしまう場合があります。

## 次のステップ
https://zenn.dev/noboruando/articles/2024-10-12vibecoding

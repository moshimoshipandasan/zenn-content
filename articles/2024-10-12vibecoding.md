---
title: "自然言語だけでプログラミング！Vibecodingをはじめよう②"
emoji: "🛠️"
type: "tech" # tech: 技術記事 / idea: アイデア
topics:
  - "ai"
  - "zenn"
  - "github"
  - "codex"
  - "vibecoding"
published: true
---

## この章のゴール
Codex CLI の環境設定を完了し、簡単なプログラムを作成します。

## Codex CLI を起動（前回の復習）
通常は`yolo`を使わず起動します（全消し事故を防ぐ）。
Codespaces環境なので全消しでも問題ないのでyoloモードで進めます。
```bash
codex --yolo
```
![](/images/2024-10-12vibecoding/Animation00.gif)
## Approvals（権限）を設定 /approvals
Codex が自動実行できる操作範囲を絞ります。おすすめは「Auto」。

```text
/approvals
```
![](/images/2024-10-12vibecoding/Animation01.gif)

- 今回は`Full Access`としますが、通常は`Auto`が安全です。
- `Full Access`では破壊的操作（`rm -rf フォルダ名` 等）が実行できます。※絶対やってはいけません！
- 謎の文字列`0;rgb:3b3b/3b3b/3b3b11;rgb:f8f8/f8f8/f8f8`が時々入りますが、たぶんバグなので、面倒ですがその度BackSpaceで消しましょう。

## Codexのモデルの設定 /model
Codex CLIの入力欄で/modelと入力し、キーボードの Enterキー を押します。
```text
/model
```
![alt text](/images/2024-10-12vibecoding/Animation02.gif)

gpt-5-codex (current) => › Low (current) を選択

## Vibecoding！簡単なプログラムを作成してみよう
ここでは`Issuesをログとして活用するGithub Pagesで公開できる掲示板を作成`してみましょう。

Codes CLIに下記を入力して実行してみましょう

```
GitHub Issues を読み込む掲示板を作って。GitHub Pages で公開できてる HTML/CSS/JS を生成して。
```

## ローカルでコミットしてリモートへプッシュする

Codex CLI を使う場合は、自然言語で指示してもOK。

```text
ローカルでコミットして、リモートへプッシュして
```

Codex は `git add/commit/push` を提案・実行します（/approvals の設定に従う）。

## GitHub Pagesでデプロイ
デプロイとは、手元で編集したファイルをインターネット上で誰でも見られるように公開することです。GitHub Pages は GitHub が提供する静的サイトの配信サービスで、ブランチ上の HTML/CSS/JS をそのままホスティングします。この章では、最短の公開方法（リポジトリ直下の `index.html`）を説明します。
まずは下記URLからGitHubに移動して対象のリポジトリを開きます。
https://github.com/
![alt text](/images/2024-10-12vibecoding/Animation03.gif)

ルート直下に `index.html` を置く場合（最短ルート）

1. リポジトリ直下に `index.html` を配置し、`main` にコミット/プッシュ。
2. GitHub → 対象リポジトリ → `Settings` → `Pages` を開く。
![alt text](/images/2024-10-12vibecoding/Animation04.gif)
3. Build and deployment → `Source: Deploy from a branch` を選択。
4. Branch: `main`、Folder: `/ (root)` を指定して `Save`。
5. 数分後に公開 URL が表示されるのでアクセスして確認。
![alt text](/images/2024-10-12vibecoding/Animation05.gif)
補足
- プロジェクト Pages の公開 URL は通常 `https://<ユーザー名>.github.io/<リポジトリ名>/`。
- 公開は基本 Public リポジトリで運用（Private は権限に注意）。

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
![alt text](../images/2024-10-12vibecoding/Animation00.gif)
## Approvals（権限）を設定 /approvals
Codex が自動実行できる操作範囲を絞ります。おすすめは「Auto」。

```text
/approvals
```
![alt text](../images/2024-10-12vibecoding/Animation01.gif)

- 今回は`Full Access`としますが、通常は`Auto`が安全です。
- `Full Access`では破壊的操作（`rm -rf フォルダ名` 等）が実行できます。※絶対やってはいけません！
- 謎の文字列`0;rgb:3b3b/3b3b/3b3b11;rgb:f8f8/f8f8/f8f8`が時々入りますが、たぶんバグなのでその都度消しましょう。

## Codexのモデルの設定 /model
Codex CLIの入力欄で/modelと入力し、キーボードの Enterキー を押します。
```text
/approvals
```
![alt text](../images/2024-10-12vibecoding/Animation02.gif)

gpt-5-codex (current) => › Low (current) を選択



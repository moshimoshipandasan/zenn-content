---
title: "Day04：Pydanticで型安全なAPIを作る｜青山学院中等部生のためのフルスタック講座"
emoji: "🧩"
type: "tech"
topics:
  - "fastapi"
  - "python"
  - "pydantic"
  - "api"
  - "青山学院"
published: false
---

# 🎓 はじめに

この連載は、**青山学院中等部生のための「30日でフルスタック開発を学ぶ講座」**です。
Day04 のテーマは、FastAPI を“プロ品質”に近づけるための重要な要素。

📌 **Pydantic（パイダンティック）を使ったデータモデル（型）の扱い方**
です。

Web API では「正しい形のデータを送る」「変な入力を自動チェックする」ことがめちゃくちゃ重要です。
その作業を **完全自動化** してくれるのが Pydantic。

Day04 を理解すると、
**安全で壊れにくい API を作れるエンジニア**になれます。

---

# 🚀 Day04 の目的

* Pydantic BaseModel を使って「データの型」を定義する
* POST API に型安全性を持たせる
* 間違ったデータを送ったときに 422 エラーを返す仕組みを理解する
* FastAPI が自動でデータ検証をしてくれることを体験する

---

# 🟦 Step1：Pydantic モデルを定義する

まず、Day03 で作った `main.py` を開きます。
そして、`BaseModel` を使って **Item モデル** を定義します。

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
```

### 🔍 これが意味すること

* `name` は文字列
* `price` は数字（float）
* 型が違ったら FastAPI が自動チェック → エラーを返す

まさに **「型でAPIを守る壁」** のような存在。

---

# 🟧 Step2：POST API を型で守る

`POST /items` を次のように書き換えます。

```python
@app.post("/items")
def create_item(item: Item):
    return {"status": "created", "item": item}
```

ここで重要なのが

```
item: Item
```

という型アノテーション（Type Hint）。

### ✔ 意味

> 「POST リクエストの Body は、Item 型である」

FastAPI はこの宣言を読み取って **自動でバリデーション（入力チェック）** します。

---

# 🟥 Step3：正しいデータを送ってみる

`http://127.0.0.1:8000/docs` にアクセス
`POST /items` → Try it out

例：

```json
{
  "name": "りんご",
  "price": 250
}
```

すると…

```json
{
  "status": "created",
  "item": {
    "name": "りんご",
    "price": 250.0
  }
}
```

完璧に受け取れます。

---

# 🟨 Step4：わざと間違ったデータを送ってみる（重要）

API の品質を上げるために、**エラー処理の仕組みを理解することは必須**です。

例1：price を文字列にする

```json
{
  "name": "りんご",
  "price": "やすい"
}
```

例2：name を数字にする

```json
{
  "name": 123,
  "price": 300
}
```

どちらも FastAPI が自動で **422 Unprocessable Entity** エラーを返します。

### 📌 422 の意味

「入力されたデータは“形式が間違っている”ので処理できない」

エラーレスポンスには：

* どこが間違っているか
* どの型が要求されていたか
* 実際にはどんなデータが送られたか

が全部載っています。

自分でバリデーションを書く必要はありません。

---

# 🧠 Day04で理解したこと

### ✔ BaseModel を使うと「型で API を守れる」

入力データの整合性が自動で保たれる。

### ✔ 型アノテーション（Type Hint）の意味

`item: Item` は「このデータは Item 型」という宣言。

### ✔ 間違った入力には自動で 422 エラー

エラーJSONも FastAPI/Pydantic が自動生成してくれる。

### ✔ Web API では安全性・信頼性が超重要

雑に作る API は壊れやすい。
型で守る API は頑丈。

---

# ✍️ Day04 まとめ

Day04 は “API品質の根幹” である **型と入力チェック** を習得する日でした。

これにより、

* Next.js（フロント）
* FastAPI（ロジック）
* Supabase（データ）

の三者を安全に繋げられる準備が整いました。

---

# 🎉 次回予告：Day05（Router 分割）

Day05 では API を「大規模アプリ構造」に耐えられるようにするための

* ファイル分割
* Router の整理
* `/users` `/items` などの機能別管理

を行います。

FastAPI を“プロの設計”に近づける重要回です。
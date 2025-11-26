---
title: "Day03：FastAPIで自分のAPIを作る｜青山学院中等部生のためのフルスタック講座"
emoji: "🐍"
type: "tech"
topics:
  - "fastapi"
  - "python"
  - "api"
  - "プログラミング"
  - "青山学院"
published: false
---

# 🎓 はじめに

この連載は、**青山学院中等部生のための「30日でフルスタック開発を学ぶ講座」**です。
Day03 では、いよいよ **Python で自分だけの API サーバーを作る** という重要なステップに進みます。

使用するのは **FastAPI**。
Next.js や Supabase と並び、プロの現場でも使われる本格的なバックエンドフレームワークです。

FastAPI はこんな特徴があります：

* 超高速
* 型安全で使いやすい
* ドキュメント（/docs）が自動生成される
* AI/動画処理との相性が良い

つまり中学生〜高校生の学習にも最適。

---

# 🚀 Day03 の目的

* FastAPI プロジェクトを作る
* API の仕組みを理解する（GET / POST / Path Parameter）
* `/hello` で動作確認
* `/items/{item_id}` で動的ルートを作る
* `POST /items` でデータを送信してみる
* `/docs` で自動生成ドキュメントを確認する

これができると、
**Next.js（フロント） → FastAPI（頭脳） → Supabase（データ）**
の「フルスタック三連携」が成立します。

---

# 🟦 Step1：FastAPI プロジェクトを作る

まず作業用フォルダを作成します。

```bash
mkdir day03
cd day03
```

### ① Python 仮想環境を作成（Windows）

```bash
python -m venv venv
```

### ② 仮想環境を有効化

```bash
venv\Scripts\activate
```

成功すると `(venv)` が表示されます。

### ③ FastAPI と uvicorn をインストール

```bash
pip install fastapi uvicorn
```

これで準備完了！

---

# 🟧 Step2：最初の API `/hello` を作る

`main.py` を作成し、以下を書きます：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello FastAPI!"}
```

### ▶ サーバー起動

```bash
uvicorn main:app --reload
```

ブラウザで：

👉 `http://127.0.0.1:8000/hello`

と入力すると、

```json
{"message":"Hello FastAPI!"}
```

と表示されます。

**これであなたは API を作った！**

---

# 🟨 Step3：動的ルート `/items/{item_id}` を作る

URL の一部を変えると返り値が変わる API を作ります。

`main.py` に追記：

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "message": "これはアイテムです"}
```

ブラウザで：

* `http://127.0.0.1:8000/items/1`
* `http://127.0.0.1:8000/items/123`

のようにアクセスすると、値が変わります。

---

# 🟥 Step4：POST でデータを送る `/items` を作成

`main.py` にさらに追記：

```python
@app.post("/items")
def create_item(item: dict):
    return {"status": "created", "item": item}
```

### ▶ `/docs` から実行できる！

FastAPI 最大の特徴：

👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

にアクセスすると…

* API 一覧
* 入力欄
* 実行ボタン

が自動生成されています。

`POST /items` に次の JSON を送ると：

```json
{
  "name": "ノート",
  "price": 1200
}
```

返り値：

```json
{
  "status": "created",
  "item": {
    "name": "ノート",
    "price": 1200
  }
}
```

**これで「データ送信API」が完成！**

---

# 🧠 Day03 で理解したこと

### ✔ GET と POST の違い

* GET：データを「読む」
* POST：データを「送る」

### ✔ Path Parameter（パスパラメータ）

URL の一部を変えると値として使える仕組み。

例：
`/items/10` → item_id = 10

### ✔ FastAPI が自動生成するドキュメント

* `/docs`（Swagger UI）
* `/redoc`（ReDoc）

### ✔ Python でバックエンドを作れるようになった

これで Fullstack の “バックエンド側” が理解できた。

---

# ✍️ Day03 まとめ

Day03では、
**「自分のAPIを作る」**
というエンジニアとしての基礎力を手に入れました。

Next.js（Day01）
Supabase（Day02）
FastAPI（Day03）

この3つを組み合わせると、
現場レベルの本格アプリを作れるようになります。

---

# 🎉 次回予告：Day04（Pydantic入門）

Day04 のテーマ
👉 **Pydantic で「型安全なAPI」を作る**

* BaseModel
* 自動バリデーション
* 422エラーの仕組み
* 型アノテーション（Type Hint）

明日から API がもっと “プロ品質” に近づきます。
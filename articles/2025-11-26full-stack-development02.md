---
title: "Day02：Supabase と Next.js をつないでデータを表示する｜青山学院中等部生のためのフルスタック講座"
emoji: "🗄️"
type: "tech"
topics:
  - "supabase"
  - "nextjs"
  - "react"
  - "プログラミング"
  - "青山学院"
published: true
---

# 🎓 はじめに

このシリーズは、**青山学院中等部生のための「30日でフルスタック開発を学ぶ講座」**です。
Day02 は Day01 の続きです。昨日は「ページを作る・リンクする」までできたので、
今日は **「データベースとつなぐ」** ところを体験します。
Web アプリで「メモを保存して後で見る」ためには、どこかにデータを置く必要があります。
その役割を Supabase（BaaS：Backend as a Service）が担ってくれます。

Supabase は **認証・データベース・ストレージ** が全部入っているクラウドサービスで、
Next.js との相性が抜群。初心者でも扱いやすく、プロレベルのアプリ構成が作れます。

---

# 🚀 **Day02 の目的**

今日のゴール（Day01の続きとして）：

* Supabase で新しいプロジェクトを作る
* データベース（posts テーブル）を作成
* Next.js から Supabase に接続し、データを一覧表示する

これができると、アプリに「保存する場所（ノート）」ができて、開発の幅が一気に広がります。

---

# 🟦 Step1：Supabase プロジェクトを作ろう

まずは Supabase にアクセス：

👉 [https://supabase.com/](https://supabase.com/)

1. ログイン（Google or GitHub 推奨）
2. 「New Project」をクリック
3. プロジェクト名を入力（例：`my-training-db`）
4. パスワードを設定
5. 数分待つとプロジェクトが作成されます

これで Supabase の準備は完了です。

※ イメージ：プロジェクトは『新しいノート』を買った状態。まだ中は白紙です。次のステップで最初のページ（テーブル）を作ります。

---

# 🟧 Step2：posts テーブルを作る

Supabase のダッシュボード左メニューから
📌 **Table Editor** → **Create a new table**

以下のようなテーブルを作ります：

| 列名         | 型         | 補足                    |
| ---------- | --------- | --------------------- |
| id         | bigint    | Primary Key（identity） |
| title      | text      | 必須（NOT NULL）          |
| created_at | timestamp | default: now()        |

完成イメージ：

```
posts
 ├ id (bigint, PK, identity)
 ├ title (text)
 └ created_at (timestamp, now())
```

---

# 🟨 Step3：Next.js に Supabase を追加する

### ① パッケージをインストール

Next.js プロジェクト（Day01で作ったやつ）で：

```bash
npm install @supabase/supabase-js
```

### ② Supabase クライアントを作る

`lib/supabase.ts` を新規作成：

```ts
import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);
```

### ③ `.env.local` を設定

Supabase の
**Project Settings → API** から取得した URL & anon key をセット：

```
NEXT_PUBLIC_SUPABASE_URL=（あなたのURL）
NEXT_PUBLIC_SUPABASE_ANON_KEY=（あなたのanon key）
```

ポイント：環境変数は『鍵付きロッカー』。リポジトリに直書きせず、`.env.local` に入れることで他人に鍵を渡さずに済みます。

---

# 🟩 Step4：/posts ページで一覧を表示する

`app/posts/page.tsx` を作成し、以下のコードを貼ります：

```tsx
import { supabase } from "@/lib/supabase";

export default async function Page() {
  const { data: posts, error } = await supabase
    .from("posts")
    .select("*")
    .order("id", { ascending: true });

  if (error) {
    return <div>エラーが発生しました：{error.message}</div>;
  }

  return (
    <div>
      <h1>Posts</h1>
      <ul>
        {posts && posts.length > 0 ? (
          posts.map((p) => (
            <li key={p.id}>
              {p.id}: {p.title}
            </li>
          ))
        ) : (
          <li>データがありません</li>
        )}
      </ul>
    </div>
  );
}
```

データの流れイメージ（中学生向け）：
- ブラウザのリクエストが『クラスの代表』として先生（Next.jsのサーバー）に届く。
- 先生が職員室（Supabase DB）にあるノート `posts` を見て、内容をまとめてクラスに配布する。
- だからページを開くたびに最新のノートがみんなに共有される。

### ✔ 動作確認

ブラウザで：

👉 `http://localhost:3000/posts`

すると、Supabase に保存したタイトルが一覧表示されます。

---

# 🧠 Day02 で理解できたこと

* Supabase は「データベース・認証・ストレージ」がセットになった便利な BaaS
* Next.js とは `.env.local` を通して安全に接続する
* `supabase.from("posts").select()` でデータが取得できる
* `/posts` ページとして一覧表示の仕組みを作れた

### 理解度チェック（確認問題）

1. Supabase プロジェクトとテーブルの関係を、ノートやページの例えで説明できますか？
2. 環境変数（.env.local）を使う理由は何ですか？URL やキーをどこに置くべきで、なぜ公開してはいけないのでしょうか？
3. `supabase.from("posts").select()` が実行される場所はどこで、結果はどのようにして `/posts` に表示されますか？

これで **APIなしでも Next.js とDBが直接つながる構成**を理解できました。

---

# ✍️ Day02 まとめ

Day02 では、
**クラウドのデータベース（Supabase）を Next.js とつなげて表示する**
という、アプリの根幹となる部分を体験しました。

明日の Day03 では、いよいよ
**FastAPI を使ってオリジナルのバックエンド/API を自分で作る**
フェーズに入ります。

Next.js・Supabase・FastAPI がつながると、
本格的なフルスタックアプリを作れるようになります。

---

# 🎉 次回予告：Day03（FastAPI入門）

Day03 のテーマ
👉 **Python で「自分のAPI」を作る FastAPI 入門**

* /hello API
* /items/{id}（パスパラメータ）
* POST /items（データを送るAPI）
* /docs で動作確認

を学びます。
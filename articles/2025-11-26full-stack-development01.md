---
title: "Day01：Next.js App Router基礎を徹底理解する｜青山学院中等部生のためのフルスタック講座"
emoji: "🚀"
type: "tech"
topics:
  - "nextjs"
  - "react"
  - "プログラミング"
  - "青山学院"
  - "初心者向け"
published: true
---

# 🎓 はじめに

この連載は、**青山学院中等部生のための「30日でフルスタック開発を学ぶ講座」**です。
実際にプロが使う **Next.js／Supabase／FastAPI** の3つを扱いながら、
1ヶ月で「アプリを自分で作れる力」を身につけることを目指します。

---

# 🚀 **Day01 の目的**

Day1 では、**Next.js App Router の超基礎**に触れながら、

* Webアプリの初期設定
* ページを3つ作る
* 共通レイアウトの仕組みを知る
* ページ遷移の基本
* Server Component / Client Component の違い

を「自分の手で書いて理解する」ことがゴールです。

難しい技術ほど、最初の1日が一番大事です。
ここをクリアすると、Day2 の Supabase 連携にスムーズに進めます。

---

# 🛠️ **Step1：Next.js プロジェクトを作ろう**

以下のコマンドで新しいプロジェクトを作成します：

```bash
npx create-next-app@latest my-training
```

推奨設定：

* TypeScript：Yes
* App Router：Yes
* Tailwind CSS：Yes
* ESLint：Yes

この設定にしておくと、後々の作業がぐっと楽になります。

---

# 🗂️ **Step2：3つのページを作る（/、/about、/settings）**

Next.js（App Router）では
**「フォルダ構造 ＝ ページのURL」**
というルールがあります。

フォルダ構成はこんな感じ：

```
app/
 ├ page.tsx          → /
 ├ about/
 │   └ page.tsx      → /about
 └ settings/
     └ page.tsx      → /settings
```

それぞれの `page.tsx` に簡単なテキストを書けば、もうページとして動作します。

ここでは、それぞれのpage.tsxの中身を下記のようにしてみましょう（App Router / TypeScript）：

```tsx
// app/page.tsx
export default function HomePage() {
  return <h1>Home Page</h1>;
}
```

```tsx
// app/about/page.tsx
export default function AboutPage() {
  return <h1>About Page</h1>;
}
```

```tsx
// app/settings/page.tsx
export default function SettingsPage() {
  return <h1>Settings Page</h1>;
}
```

# 🎨 **Step3：共通レイアウト（layout.tsx）を設定する**

Next.js の App Router では、
**`app/layout.tsx` が全ページ共通のレイアウト**になります。

ヘッダーにページリンクを置いてみましょう。

```tsx
// app/layout.tsx
import Link from "next/link";

export default function RootLayout({ children }) {
  return (
    <html lang="ja">
      <body>
        <header style={{ padding: 10, background: "#eee" }}>
          <Link href="/">Home</Link> |{" "}
          <Link href="/about">About</Link> |{" "}
          <Link href="/settings">Settings</Link>
        </header>
        <main style={{ padding: 20 }}>{children}</main>
      </body>
    </html>
  );
}
```

これで
**どのページでも同じヘッダーが表示される**ようになります。

ここまでできたら、プロジェクト直下で cd my-training → 
npm run dev を実行し、ブラウザで http://localhost:3000 を開いてヘッダーが全ページで共通に出ることを確認してみよう。

---

# 🔗 **Step4：ページ遷移（Link コンポーネント）**

Next.js では `<Link>` を使うことで、
通常の `<a>` よりも高速なページ遷移が可能になります。

### 🔍 Link のメリット

* 画面をリロードしない
* 移動先のページを事前に読み込む（プリフェッチ）
* SPA のような動き

例：

```tsx
<Link href="/about">About</Link>
```

---

# 🖥️ **Step5：Server Component を作ってみよう**

Next.js 13 以降のデフォルトは **Server Component**。
サーバー側で実行されるので、`fetch()` が最適化されます。

### ?? なぜ fetch() を使うのか？（中学生向けのたとえ）
* `fetch()` は「別の部屋にいる友だちへメモを取りに行くお使い役」。インターネット上のサーバーからデータを持ってきてくれる。
* ふつうの関数は「手元のノートだけを見る」けれど、`fetch()` は「図書室に行って本を借りる」みたいに外の情報を取りに行ける。
* Server Component で使うと、先生（サーバー）がまとめてメモを集めてからクラスに配るので、みんなのPCが軽くなる（高速＆効率的）。
* エラーが出たときは「図書室が閉まっている」「本が見つからない」といった状態なので、メッセージを確認してもう一度お願いする（リトライ）イメージ。

例：`app/page.tsx`

```tsx
export default async function Page() {
  const res = await fetch("https://jsonplaceholder.typicode.com/todos/1");
  const data = await res.json();

  return (
    <div>
      <h1>Server Component</h1>
      <p>取得したタイトル：{data.title}</p>
    </div>
  );
}
```

---

# 🧩 **Step6：Client Component を作ってみよう**

ユーザーの操作（クリック、入力など）を扱うには
先頭に `"use client"` を書きます。

例：`app/settings/Counter.tsx`

```tsx
"use client";

import { useState } from "react";

export default function Counter() {
  const [n, setN] = useState(0);

  return <button onClick={() => setN(n + 1)}>count: {n}</button>;
}
```

`settings/page.tsx` で読み込む：

```tsx
import Counter from "./Counter";

export default function Page() {
  return (
    <div>
      <h1>Settings Page</h1>
      <Counter />
    </div>
  );
}
```

---

# 🎉 **Day01まとめ**

Day01では、Next.js の基礎をしっかり固めました。

### 今日できるようになったこと

* Next.js（App Router）の基本構造が理解できた
* ページ作成、フォルダ構造、URLの関係がわかった
* layout.tsx による共通レイアウトが使えた
* `<Link>` による高速ページ遷移ができた
* Server Component / Client Component の違いを実際に体験できた

これで Day2 の Supabase 接続に進む準備が万端です。

---

# ✏️ **次回予告：Day02（Supabase 入門）**

Day2 では、
**Supabase を使って Next.js とデータベースをつなげる**
という、アプリ開発に必須の作業に取り組みます。

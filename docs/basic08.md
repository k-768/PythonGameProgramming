---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編8　tkinter(1) "
  header-date: "最終更新日：2024年10月29日（火）"
---

# 基礎編8　tkinter (1) 

グラフィック（見た目）は、ゲームにおいて非常な重要な部分です。
今回は、Pythonを用いて画面を表示してみましょう。

## もくじ

-  [モジュール](basic08.html#リスモジュールトとは) 
-  [ウィンドウを表示する](basic08.html#ウィンドウを表示する) 

## モジュール

モジュールを`import`することで、簡単に新たな機能を追加することができます。
今回は、`tkinter`モジュールを追加してみましょう。これを使うと、ウィンドウや図形などの**グラフィカルな要素を簡単に作成**することができます。
プログラムの最初の行にこの文を記述するだけで準備完了です。

```
import tkinter as tk
```

**tkinterを利用するたびに、毎回毎回 tkinter.・・・と書くのは面倒なので省略できます**。
`import tkinter`の後ろに`as tk`と記述することで、**`tk`と書くだけで良くなり**コードが簡潔で読みやすくなります。

## ウィンドウを表示する

以下のコードを実行してみてください。

```python{.numberLines startFrom="1" caption="tk.py"}
import tkinter as tk
# ウィンドウを表示する
root = tk.Tk()
root.title("test")
root.geometry("600x400") 

root.mainloop()
```

実行すると、ウィンドウが表示されます。

- `4行目`の`"test"`と書かれた部分を変更することで、ウィンドウの名前を変更できます。
- `5行目`の`"600x400"`はウィンドウのサイズを`"幅x高さ"`で指定しています。書き換えればサイズを変更できます。



#### **charenge8-1** 

- ウィンドウの名前を`tk`に変更してください
- ウィンドウのサイズを`800x600`に変更してください

答えは次のコードを参照して確認してください。


---

## キャンバスを設置する

キャンバスは、**図形や画像を設置するために必要な下地**です。



```python{.numberLines startFrom="1" caption="tk.py"}
import tkinter as tk
# ウィンドウを表示する
root = tk.Tk()
root.title("tk")
root.geometry("800x600") 

# キャンバス設置
canvas = tk.Canvas(root,width = 600,height = 400,bg = "skyblue")
canvas.pack()

root.mainloop()
```

`8行目`でキャンバスの大きさや色を指定しています。
`width`が**幅**、`height`が**高さ**、`bg`が**背景色**に対応しています。






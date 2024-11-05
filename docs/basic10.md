---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編10　tkinter(1) "
  header-date: "最終更新日：2024年11月05日（火）"
---

# 基礎編10　tkinter (1) 

グラフィック（見た目）は、ゲームにおいて非常な重要な部分です。
今回は、Pythonを用いて画面を表示してみましょう。

## もくじ

-  [モジュール](basic10.html#リスモジュールトとは) 
-  [ウィンドウを表示する](basic10.html#ウィンドウを表示する) 

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


#### **Challenge8-1** 

- ウィンドウの名前を`tk`に変更してください
- ウィンドウのサイズを`800x600`に変更してください

答えは次のコードの該当部分を参照して確認してください。


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


#### **Challenge8-2** 

- キャンバスのサイズをウィンドウと同じ`800x600`に設定してください。
- キャンバスの色をオレンジ(`orange`)に変更してください。

答えは次のコードの該当部分を参照して確認してください。


---


## 図形を配置する

`create_rectangle`という命令を用いて、四角形を画面上に配置できます。


```python{.numberLines startFrom="1" caption="tk.py"}
import tkinter as tk
# ウィンドウを表示する
root = tk.Tk()
root.title("tk")
root.geometry("800x600") 

# キャンバス設置
canvas = tk.Canvas(root,width = 800,height = 600,bg = "orange")
canvas.pack()

# 四角形を配置
rect_size = 50
x = 10
y = 10
canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")

root.mainloop()
```


以下のように四角形の**左上と右下の座標**、**色**、**名前**を指定しています。

![img](figs/digest/create_rectangle.png)


ただし、プログラミングで用いられる座標軸は、**数学で用いられるものと向きが違う**ので**注意が必要です**。

![img](figs/digest/座標系.png)

モニターの**左上が原点**で、**Y軸が反転**しています。


## キーボードの入力を受け取る

`bind()`命令を用いれば、キーボードの入力も簡単に受け取ることができます。以下のプログラムを実行してみてください。
キーボードを押すと、押したキーが出力されます。

```python{.numberLines startFrom="1" caption="tk.py"}
import tkinter as tk
# ウィンドウを表示する
root = tk.Tk()
root.title("tk")
root.geometry("800x600") 

# キャンバス設置
canvas = tk.Canvas(root,width = 800,height = 600,bg = "orange")
canvas.pack()

# 四角形を配置
rect_size = 50
x = 10
y = 10
canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")

# 何かのキーが押されたときに実行される関数
def on_key_press(event):
    key = event.keysym # 変数keyに「w」や「a」など、押したキーの名前が格納される
    print(key)

# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
```

`23行目`に`bind()`命令があります。今回の場合は**条件＝ボタンが押されたとき**、**実行する関数＝`on_key_press`**になります。

```python{}
root.bind(条件, 実行する関数の名前)
```

`18行目`に記述した、ボタンが押されたときに実行する関数を見てください。
引数`event`に、押されたキーボードの情報が渡されます。そして、`event.keysym`でキーの名前に変更できます。



## キーボードの入力を判定する

`key`の中身をif文で判定します。wキーか↑キーのときは上、aキーか←キーのときは左、...といった具合に場合分けしていきます。

```python{.numberLines startFrom="1" caption="tk.py"}
import tkinter as tk
# ウィンドウを表示する
root = tk.Tk()
root.title("tk")
root.geometry("800x600") 

# キャンバス設置
canvas = tk.Canvas(root,width = 800,height = 600,bg = "orange")
canvas.pack()

# 四角形を配置
rect_size = 50
x = 10
y = 10
canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")

# 何かのキーが押されたときに実行される関数
def on_key_press(event):
    key = event.keysym # 変数keyに「w」や「a」など、押したキーの名前が格納される
    if(key == "w" or key == "Up"):
        print("↑")
    elif(key == "a" or key == "Left"):
        print("←")
    elif(key == "s" or key == "Down"):
        print("↓")
    elif(key == "d" or key == "Right"):
        print("→")

# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
```


## キーボードの入力を判定する

キーボードの入力に合わせて四角形を動かせば、四角形の移動ができるようになります。

```python{.numberLines startFrom="1" caption="tk.py"}
import tkinter as tk
# ウィンドウを表示する
root = tk.Tk()
root.title("tk")
root.geometry("800x600") 

# キャンバス設置
canvas = tk.Canvas(root,width = 800,height = 600,bg = "orange")
canvas.pack()

# 四角形を配置
rect_size = 50
x = 10
y = 10
canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")

# 何かのキーが押されたときに実行される関数
def on_key_press(event):
    global x,y
    speed = 5
    key = event.keysym # 変数keyに「w」や「a」など、押したキーの名前が格納される
    if(key == "w" or key == "Up"):
        print("↑")
        y = y - speed
    elif(key == "a" or key == "Left"):
        print("←")
        x = x - speed
    elif(key == "s" or key == "Down"):
        print("↓")
        y = y + speed
    elif(key == "d" or key == "Right"):
        print("→")
        x = x + speed
    
    # 元の四角形を削除して、再配置する
    canvas.delete("rect")
    canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")

# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
```
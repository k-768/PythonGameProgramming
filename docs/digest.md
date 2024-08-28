---
var:
  header-title: "Pythonで釣りゲームを作ろう プロトタイプ版"
  header-date: "2024年08月28日"
---

# Pythonで釣りゲームを作ろう プロトタイプ版

## 今回の趣旨について

私は卒業研究として、「高専1年生を対象としたゲーム作りを通じてPythonプログラミングを学べる教材づくり」を行っております。今回のデモ講座では、教材の方向性の確認や、教材の有効性の検証を目的としております。今日の最後には、アンケートを実施します。ご協力いただきますよう、よろしくお願いします。

## はじめに

このオンラインテキストでは、**ゲームづくりを通じて、Pythonプログラミングを学ぶことができます**。
本来は**90分x8回**の講義で、テキストを進めると**最終的にゲームが完成する**形式ですが、今回は短い時間のため、**サンプルを改造しながら、Pythonについて学ぶ**形式になっています。

## もくじ　※要編集

-  [環境構築](basic05.html#条件分岐とは) 
-  [プログラムの実行](basic05.html#条件分岐とは) 
-  [キーボードでキャラクターを操作](basic05.html#if文) 
-  [ガチャを作ろう！](basic05.html#関係演算子)


## 環境構築

Pythonでプログラミングをするためには、環境の構築が必要です。レポートを書くためにWordやGoogleDocumentといったテキストエディタが必要であるのと同じように、**プログラミングにはソースコードエディタが必要**です。今回は、**Visual Studio Code**(VSCode)とよばれるソースコードエディタを用います。


### VSCodeのインストール

以下のページから、VSCodeをインストールしてください。

[https://code.visualstudio.com/download](https://code.visualstudio.com/download)

... (インストーラの起動とインスト)
[参考資料](https://note.com/yuuuu_tech/n/nf7d25a6a74d9)

### Pythonのインストール

### VSCodeでPythonを使う設定

### 初めてのプログラミング

（ファイルの作り方、プログラムの記述、実行）

<br>

## キーボードでキャラクターを操作

### まずはサンプルを触ってみる

以下のプログラムをコピー＆ペーストして実行してみてください。すると、画像のような画面が表示されると思います。

![img](figs/sub/move-rect.png)

**矢印キーもしくはWASDで操作**できます。押してみて、四角形が移動することを確認してください。

```python{.numberLines caption="move-rect.py"}
import tkinter as tk

# ウィンドウ設置
root = tk.Tk()
root.title("move-rect")
root.geometry("600x300")

# キャンバス設置
canvas = tk.Canvas(root,width = 600,height = 300,bg = "skyblue")
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
    
    canvas.delete("rect")
    canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")

# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
```

**ウィンドウの×ボタンを押すとプログラムが終了します。**
<br>

### ウィンドウのタイトルを変更する

`3行目`の`"move-rect"`の部分で、**ウィンドウのタイトルを指定**しています。試しに、`"test"`に変更してみてください。

```python{.numberLines startFrom="3" caption="move-rect.py(抜粋)"}
# ウィンドウ設置
root = tk.Tk()
root.title("test")　<-ここを変更
root.geometry("400x600") 
```

プログラムを実行して、タイトルが変わっていることを確認してください。

<br>

### ウィンドウの大きさを変更する

`6行目`の`"600x300"`の部分で、**表示するウィンドウのサイズを指定**しています。試しに、`"600x300"`を`"400x600"`に変更してみてください。

```python{.numberLines startFrom="3" caption="move-rect.py(抜粋)"}
# ウィンドウ設置
root = tk.Tk()
root.title("move-rect")
root.geometry("400x600") <-ここを変更
```

実行すると、ウィンドウが縦長に変わります。このように、ウィンドウのサイズを`"幅x高さ"`で指定できます。`600`や`400`といった数字は**ピクセル数**を表しています。

![img](figs/digest/400x600.png)

<br>

<div class="note type-tips">

**ディスプレイの解像度を調べる**

モニターのピクセル数は設定から調べることができます。

**設定　＞　システム　＞　ディスプレイ　＞　ディスプレイの詳細設定**

![img](figs/digest/ディスプレイサイズ.png)

この場合、`1920x1080`がディスプレイ全体のサイズになります。
</div>
<br>

- **Challenge**　ディスプレイの解像度を参考にして、ウィンドウが**画面に大きく表示されるように**、適当なサイズに変更してください。

<br>

### キャンバスを変更する

キャンバスは、**図形や画像を設置するために必要な下地**です。

`10行目`ではキャンバスの大きさや色を指定しています。
`width`が**幅**、`height`が**高さ**、`bg`が**背景色**に対応しています。
幅と高さを**上で設定したウィンドウと同じ数値に変更**してみてください。

```python{.numberLines startFrom="9" caption="move-rect.py(抜粋)"}
# キャンバス設置
canvas = tk.Canvas(root,width = xxx,height = yyy,bg = "skyblue") <-ここを変更
canvas.pack()
```

以下の画像を参考に、色も変更してみましょう。`skyblue`を好きな色の名前に書き換えることで変更できます。

![img](figs/digest/color.png)

> 出典: https://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix-using-python

例えば`orange`に変更することで、**背景色がオレンジ**になります。

```python{.numberLines startFrom="9" caption="move-rect.py(抜粋)"}
# キャンバス設置
canvas = tk.Canvas(root,width = 800,height = 600,bg = "orange") <-ここを変更
canvas.pack()
```

![img](figs/digest/orange.png)

<br>

### 四角形を配置する

以下の部分で、用意したキャンバスに四角形を配置しています。

`14行目`の数字を変更することで、四角形の大きさを変更できます。試しに`100`に変更して、四角形が大きくなることを確認してください。

```python{.numberLines startFrom="13" caption="move-rect.py(抜粋)"}
# 四角形を配置
rect_size = 100 <-ここを変更
x = 10
y = 10
canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")
```

`15～16行目`の数字を変更することで、四角形の初期位置を変更できます。

ただし、プログラミングで用いられる座標軸は、**数学で用いられるものと向きが違う**ので**注意が必要です**。

![img](figs/digest/座標系.png)

モニターの**左上が原点**で、**Y軸が反転**しています。

**xやyの値を変えて、それぞれが四角形の位置にどのように対応しているか確認してください**。

```python{.numberLines startFrom="13" caption="move-rect.py(抜粋)"}
# 四角形を配置
rect_size = 100 
x = 10　<-ここを変更
y = 10 <-ここを変更
canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")
```

<div class="note type-tips">

**このプログラムのしくみ**

`14行目`から`16行目` では**変数**というものを使用しています。

```python{.numberLines startFrom="13" caption="move-rect.py(抜粋)"}
# 四角形を配置
rect_size = 50
x = 10
y = 10
canvas.create_rectangle(x,y,x+rect_size,y+rect_size,fill="blue",tag="rect")
```

`14行目`の`rect_size = 50`は、**「今後`rect_size`という名前が出てきたらそれを50と読み替えてください」**という意味です。


そして、`canvas.create_rectangle`という命令で四角形を配置しています。
以下のように四角形の**左上と右下の座標**、**色**、**名前**を指定しています。

![img](figs/digest/create_rectangle.png)

</div>



---
var:
  header-title: "Pythonで釣りゲームを作ろう ゲームづくり編1　魚を釣るシステムを作ろう"
  header-date: "2024年10月24日（木）"
---

# ゲームづくり編1　魚を釣るシステムを作ろう


## はじめに

ここからは実際に**ゲームを製作していきましょう！**


## もくじ
- [環境を整える](advance01.html#環境を整える)
- [ゲーム画面を表示する](advance01.html#ゲーム画面を表示する)

## 環境を整える

- 新しいフォルダの作成

ファイル→ファイルを開くを選択

![img](/docs/figs/101/openFolder.png)

<br>

`FishingGame`という名前で新しいフォルダを作成して開く

![img](/docs/figs/101/NewFolder.png)

<br>

![img](/docs/figs/101/MakeFolder.png)

<br>

- 画像フォルダの作成

エクスプローラを右クリックして、`img`フォルダを作成

![img](/docs/figs/101/ImgFolder.png)

<br>

- ファイルの作成

エクスプローラを右クリックして、`game01.py`ファイルを作成

---


## ゲーム画面を表示する

まずはtkinterを用いて、ゲーム画面を表示します。背景として、以下の画像を使用します。[こちらから画像をダウンロードしてください。](https://github.com/k-768/python_game/blob/master/img/fishing_map.png)

![img](/docs/figs/101/fishing_map.png)

ファイルをダウンロードしたら、画像を先ほど作成した`img`フォルダの**中に移動してください**。


### ウィンドウを表示する

以下のプログラムを実行してください。


```python{.numberLines caption="game01.py"}
import os
import tkinter as tk


#>>ディレクトリ>>
cwd = os.getcwd() 


#>>マップ設定>>
MAP_SIZE_X = 384  #マップ画像のxピクセル数
MAP_SIZE_Y = 384  #マップ画像のyピクセル数

MAGNIFICATION_RATE = 2 # 拡大率


#>>ウィンドウ、キャンバス>>
CANVAS_WIDTH = MAP_SIZE_X * MAGNIFICATION_RATE #キャンバス幅
CANVAS_HEIGHT = MAP_SIZE_Y * MAGNIFICATION_RATE #キャンバス高さ
MARGINE_X = 2 #マージン
MARGINE_Y = 2 #マージン
CANVAS_SIZE = f"{CANVAS_WIDTH+MARGINE_X}x{CANVAS_HEIGHT+MARGINE_Y}"#キャンバスサイズ


#ウィンドウ設置
root = tk.Tk()
root.title("game01")
root.geometry(CANVAS_SIZE)


#キャンバス設置
canvas = tk.Canvas(root,width = CANVAS_WIDTH,height = CANVAS_HEIGHT,bg = "skyblue")
canvas.pack()


#マップ画像
MAP_IMAGE = tk.PhotoImage(file = cwd+"/img/fishing_map.png") # 画像を読み込む
MAP_BIG_IMAGE = MAP_IMAGE.zoom(MAGNIFICATION_RATE,MAGNIFICATION_RATE) # 画像を拡大する

canvas.create_image(0,0,image = MAP_BIG_IMAGE ,tag="bgimage",anchor=tk.NW) # 画像を配置する


# メインループ
root.mainloop()
```

実行すると、背景画像が表示されます。

![img](/docs/figs/101/gameWindow.png)


---

画像を表示する流れを見ていきましょう。`35行目`からに注目してください。

```python{.numberLines startFrom="35" caption="game01.py(抜粋)"}
#マップ画像
MAP_IMAGE = tk.PhotoImage(file = cwd+"/img/fishing_map.png") # 画像を読み込む
MAP_BIG_IMAGE = MAP_IMAGE.zoom(MAGNIFICATION_RATE,MAGNIFICATION_RATE) # 画像を拡大する

canvas.create_image(0,0,image = MAP_BIG_IMAGE ,tag="bgimage",anchor=tk.NW) # 画像を配置する

```

<br>

まず、`36行目`で画像を読み込んで`MAP_IMAGE`という変数に格納(データを保存)しています。画像を読み込むには`tk.PhotoImage`命令を用います。

```python{caption="画像の読み込み"}
MAP_IMAGE = tk.PhotoImage(file = ファイルのパス)

```

画像を読み込むには、画像の**パス**が必要になります。**パスとは、PC内の住所のようなもの**です。エクスプローラでは、画面の上部に表示されています。

![img](/docs/figs/101/pass.png)


<div class="note type-tips">

**パスの求め方**

今回のプログラムでは、Pythonのosモジュールを使って、作業ディレクトリ(作業フォルダー)のパスを取得しています。

新しいファイル`cwd.py`を作成して、以下のプログラムを実行してみてください。

```python{.numberLines caption="cwd.py"}
import os

# 現在の作業ディレクトリを取得
cwd = os.getcwd()  # cwdは "current working directory" の略
print(cwd)  # 現在の作業ディレクトリのパスが表示されます
```

実行すると、今開いているフォルダ`FishingGame`までのパスが表示されます。このように、自動でパスを取得して変数`cwd`に格納しています。

フォルダ`FishingGame`までのパスは取得できたので、あとはフォルダ`FishingGame`から画像までのパスをつなげれば画像のパスがわかります。

```python{.numberLines startFrom="36" caption="画像の読み込み"}
MAP_IMAGE = tk.PhotoImage(file = cwd+"/img/fishing_map.png") # 画像を読み込む
```

少し難しい話ですが「そういうもんなんだ」と思ってさらっといきましょう。

</div>

<br>

次に、`zoom`命令を用いて取得した画像を拡大しています。拡大率は整数である必要があります。今回は2倍です。

```python{caption="画像の拡大"}
画像を格納した変数.zoom(X方向の拡大率,Y方向の拡大率)
```

<br>

最後に、拡大した画像を配置します。`create_image`命令を用います。使い方は以下の通りです。

```python{caption="画像の配置"}
canvas.create_image(x座標,y座標,image = 画像を格納した変数 ,tag=画像の識別用の名前,anchor=基準点)

```

- **tag**は、画像を後で消したりする際に必要になります。識別用なので、ほかの画像とかぶっていない必要があります。

- **anchor**は、**指定したx座標、y座標を画像のどこに合わせるか**というものです。`tk.NW`はN=北、W=西という意味で北西、つまり**画像の左上を基準にしてください**という意味になります。


### キーボード入力を判定する

[基礎編10](basic10.html#キーボードの入力を判定する)で学んだキーボード入力の判定を組み合わせましょう。




x---
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

`Fishing game`という名前で新しいフォルダを作成して開く

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
root.title("Sample Game ver0.92")
root.geometry(CANVAS_SIZE)

#キャンバス設置
canvas = tk.Canvas(root,width = CANVAS_WIDTH,height = CANVAS_HEIGHT,bg = "skyblue")
canvas.pack()



#マップ画像
MAP_IMAGE = tk.PhotoImage(file = cwd+"/img/fishing_map.png")
MAP_BIG_IMAGE = MAP_IMAGE.zoom(MAGNIFICATION_RATE,MAGNIFICATION_RATE)

canvas.create_image(0,0,image = MAP_BIG_IMAGE ,tag="bgi",anchor=tk.NW)

root.mainloop()
```

実行すると、背景画像が表示されます。

![img](/docs/figs/101/gameWindow.png)

`13行目`、`14行目`では、読み込む画像のサイズを指定しています。今回の画像は縦横384pxです。そのままでは小さくなるので、`16行目`で倍率を指定しています。

画像の配置は、`create_image`を用いて、`41行目`で行っています。

```python{}

canvas.create_image(x座標,y座標,image = 画像のパス（PC内のどこにあるか） ,tag=画像の識別用の名前,anchor=基準点)

```


---
var:
  header-title: "Pythonで釣りゲームを作ろう ゲームづくり編3　マップを表示しよう"
  header-date: "2024年12月6日（金）"
---

# ゲームづくり編3　マップを表示しよう

## ゲームのマップ

マップ画面は、RPG（ロールプレイングゲーム）やシミュレーションゲームなど、多くのゲームで欠かせない要素です。今回は、**マップチップ**と呼ばれるものを使って、マップを描写してみましょう。

<br>

## もくじ
- [](advance03.html#)

<br>

## マップチップとは

ゲームには、プレイヤーが探索するフィールド、都市、ダンジョンなど、さまざまな場所が登場します。しかし、一枚一枚のマップを手作業で描いていくとなると、膨大な時間と労力が必要になります。そこで登場するのが**マップチップ**です。マップチップとは、草地や水辺、道路など、**地形やオブジェクト(チェストやタンスなどの「もの」)を表す小さな画像パーツ**のことです。これらを組み合わせることで、効率的にマップを構築することができます。

画像の用意や処理がシンプルなため、容量制限の厳しかった昔はほとんどのゲームでマップチップが採用されていました。マップチップを用いれば、初心者でも簡単に取り組めます。

<br>

今回は、`grass.png` `sand.png` `water.png`の3枚の画像を用います。ダウンロードして`img`フォルダに入れておいてください。

![img](./figs/103/grass.png)![img](./figs/103/sand.png)![img](./figs/103/water.png)

これらの画像は、基本的に同じサイズでそろえることをおすすめします。今回は`64x64px`で統一しています。

## Tkinterでウィンドウを表示する

新しいファイル`map01.py`を作成して、ウィンドウを表示するプログラムを制作していきましょう。

```python{.numberLines startFrom=1 caption="map01.py"}
import os
import tkinter as tk

#>>ディレクトリ>>
cwd = os.getcwd()

#>>マップ設定>>
CHIP_SIZE = 64 #マップチップの大きさ
X_MAPSIZE = 20 #マップのx方向タイル数
Y_MAPSIZE = 10 #マップのy方向タイル数

#>>ウィンドウ、キャンバス>>
CANVAS_WIDTH = CHIP_SIZE * X_MAPSIZE #キャンバス幅
CANVAS_HEIGHT = CHIP_SIZE * Y_MAPSIZE #キャンバス高さ
MARGINE_X = 2 #マージン
MARGINE_Y = 2 #マージン
CANVAS_SIZE = f"{CANVAS_WIDTH+MARGINE_X}x{CANVAS_HEIGHT+MARGINE_Y}"#キャンバスサイズ

#ウィンドウ設置
root = tk.Tk()
root.title("マップ表示")
root.geometry(CANVAS_SIZE)

#キャンバス設置
canvas = tk.Canvas(root,width = CANVAS_WIDTH,height = CANVAS_HEIGHT,bg = "skyblue")
canvas.pack()


#>>マップチップ>>
MAP_CHIP = [
    tk.PhotoImage(file = cwd+"/img/grass.png"),
    tk.PhotoImage(file = cwd+"/img/sand.png"),
    tk.PhotoImage(file = cwd+"/img/water.png")
    ]

root.mainloop()
```

最初の方で多くの数字を設定しています。マップチップの大きさや、マップのサイズなどです。このように、様々な値を変数で置いておくことで、あとからの修正が楽になります。

そして、用意した画像は最後の方で**リスト**に格納されています。

---

- **ChallengeA3-1**　草の画像を呼び出したいとき、どのように記述したら良いですか。

**<i class="fa-solid fa-check"></i>解答**

<span class="masked">`MAP_CHIP[0]`</span>


## マップチップを表示する

以下の一文を`root.mainloop()`の前に追加してみてください。

```python{.numberLines startFrom=36 caption="map01.py（続き）"}
canvas.create_image(0,0,image =MAP_CHIP[0] ,tag="chip1",anchor=tk.NW)
```

実行すると、マップチップが表示されます。

![img](./figs/103/putGrass.png)

<br>

これを並べていけばマップが作れます。一つ右に砂地を配置してみましょう。

```python{.numberLines startFrom=37 caption="map01.py（続き）"}
canvas.create_image(CHIP_SIZE,0,image =MAP_CHIP[1] ,tag="chip2",anchor=tk.NW)
```

これを繰り返し行えばよいので、繰り返し文を用いてみましょう。**先ほどの画像を配置する2文を消して、以下のプログラムを追加してください。**

```python{.numberLines startFrom=36 caption="map01.py（続き）"}
for y in range(Y_MAPSIZE):
    for x in range(X_MAPSIZE):
        canvas.create_image(x*CHIP_SIZE,y*CHIP_SIZE,image =MAP_CHIP[0] ,tag=f"chip{x},{y}",anchor=tk.NW)
```

ウィンドウが草地で埋め尽くされたら成功です。

![img](./figs/103/allgreen.png)

<br>

## 1枚の画像からマップチップを取得する


## データをもとにマップを配置する

```python{.numberLines startFrom=36 caption="map01.py（続き）"}
#>>マップデータ>>
MAP_DATA = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3],
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [2, 2, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
]
```


## さらに豪華なマップを作ろう

「マップチップ　フリー」などで検索すると、マップチップのフリー素材を入手できます。それを活用すればさらに豪華なマップを作れます。
おすすめのサイトを紹介します。

- [マップチップ　16×16 -ぴぽや倉庫](https://pipoya.net/sozai/assets/map-chip_tileset16/#マップセット１)

使う際は入手した画像が何px四方なのかよく確認して、プログラムの`CHIP_SIZE`を変更してください。また、**ゲームを公開したり配布する際は、使用する素材の規約をよく確認してください。**ぜひ、楽しく自分でマップを作りこんでみてください！
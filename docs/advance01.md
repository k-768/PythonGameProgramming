---
var:
  header-title: "Pythonで釣りゲームを作ろう ゲームづくり編1　魚を釣るシステムを作ろう"
  header-date: "2024年10月24日（木）"
---

# ゲームづくり編1　魚を釣るシステムを作ろう


## はじめに

ここからは実際に**ゲームを製作していきましょう！**

<br>

## もくじ
- [環境を整える](advance01.html#環境を整える)
- [ゲーム画面を表示する](advance01.html#ゲーム画面を表示する)

<br>

## 環境を整える

- 新しいフォルダの作成

ファイル→ファイルを開くを選択

![img](./figs/101/openFolder.png)

<br>

`FishingGame`という名前で新しいフォルダを作成して開く

![img](./figs/101/NewFolder.png)

<br>

![img](./figs/101/MakeFolder.png)

<br>

- 画像フォルダの作成

エクスプローラを右クリックして、`img`フォルダを作成

![img](./figs/101/ImgFolder.png)

<br>

- ファイルの作成

エクスプローラを右クリックして、`game01.py`ファイルを作成


<br>
<br>

## ゲーム画面を表示する

まずはtkinterを用いて、ゲーム画面を表示します。背景として、以下の画像を使用します。[こちらから画像をダウンロードしてください。](https://github.com/k-768/python_game/blob/master/img/fishing_map.png)

![img](./figs/101/fishing_map.png)

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

![img](./figs/101/gameWindow.png)


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

![img](./figs/101/pass.png)


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

<br>
<br>


### キーボード入力を判定する

[基礎編10](basic10.html#キーボードの入力を判定する)で学んだキーボード入力の判定を組み合わせましょう。ただし、今後アニメーションをするにあたって少し工夫しなければいけません。以下のプログラムをコピペして実行してください。


```python{.numberLines caption="game01.py"}
import copy
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


#ゲームの基本となる1ティック時間(ms)
TICK_TIME = 50  


#>>ゲームのメインループ関数>>
def gameLoop():
    global key,currentKey,prevKey
    
    prevKey = copy.deepcopy(key)
    key = copy.deepcopy(currentKey)
    root.after(TICK_TIME,gameLoop)


#>>キー監視>>
currentKey = []#現在押されているキー
key = []       #前回の処理から押されたキー
prevKey = [] #前回の処理までに押されたキー

#何かのキーが押されたときに呼び出される関数
def press(e):
    keysym = e.keysym
    if(keysym not in currentKey):#始めて押されたならば
        currentKey.append(keysym)
        print(f"pressed:{keysym}")
    if(keysym not in key):#前回の処理から始めて押されたならば
        key.append(keysym)

#何かのキーが離されたときに呼び出される関数
def release(e):
    keysym = e.keysym
    currentKey.remove(keysym)
    print(f"released:{keysym}")

#キー入力をトリガーに関数を呼び出すよう設定する
root.bind("<KeyPress>", press)
root.bind("<KeyRelease>", release)


#>>メインループ>>>
gameLoop()
print("start!")
root.mainloop()
```

このプログラムでは、**押しているキーがリスト**`key`**に格納されています**。そのため、配列の中身をチェックすることでキーボード入力を判定します。

このプログラムをもとにして、改造を進めましょう。

<br>
<br>

## スペースキーが押されたか調べる

`50行目`の`gameloop`内に、スペースキーが押されたか判定するプログラムを作成しましょう。

リストの中に目当てのものが含まれているかを調べるには、`in`を用います。

```python{caption="リストの中身を調べる"}
# もしリストの中にキーワードがあれば
if キーワード in リスト:
```

<br>

これを使って、以下のように判定できます。

```python{.numberLines startFrom=47 caption="game01.py（抜粋）"}
#>>ゲームのメインループ関数>>
def gameLoop():
    global key,currentKey,prevKey
    
    if("space" in key):
        print("スペースキーが押された！")
    
    prevKey = copy.deepcopy(key)
    key = copy.deepcopy(currentKey)
    root.after(TICK_TIME,gameLoop)
```

実行してスペースキーを押してみてください。スペースキーを**一度押しただけで数回コメントが出力される**ことがあると思います。

---

これを防ぐには、以下のように、少し前のキーボードの状態も考慮する必要があります。

リスト`prevKey`には、**前回のループのときに押されたキー**（少し前に押されていたキー）が格納されています。

```python{caption="押された瞬間だけ判定する方法"}
# もしスペースキーが押されたなら
if(("space" in key) and ("space" not in prevKey)):
```

まず、**①**`"space" in key`の部分で**現在の入力（今押されているか）の確認**を行います。

そして、**②**`"space" not in prevKey`の部分で**前回の入力(前は押されていなかったか)を確認**します。

**③**両方の条件を満たすとき、プレイヤーは**今回新たにスペースキーを押した**、ということになります。

<br><br>

<div class="note type-tips">

**判定の使い分け**

ゲームにおけるキーボード入力には、**連続入力（＝長押し）を受け付ける場合と受け付けない場合があります**。ここでは、キャラクターの移動とメニュー操作を例に説明します。

<br>


#### 1: キャラクターの移動

![img](./figs/101/walk.gif)

- **例:** ゲーム中に、キャラクターを前に移動させたいとき、プレイヤーは「W」キーを押し続けます。
- **求める動作:** 「W」キーを押し続けると、キャラクターがどんどん前に移動します。つまり、長押しを受け付けたいということです。


**処理の流れ**

1. プレイヤーが「W」キーを押したとき、キャラクターは移動を始めます。
2. プレイヤーが「W」キーを押し続けている限り、キャラクターはそのまま移動し続けます。
3. プレイヤーが「W」キーを離したら、キャラクターの移動を止めます。

<br>


#### 2: メニュー操作

- **例:** メニュー画面で「Space」キーを使って決定をしたいとき、プレイヤーが「Space」キーを押し続けると、メニューが毎回選択されてしまいます。
- **求める動作:** 「Space」キーは一度だけ押されたときだけ決定をするようにしたい。つまり、長押しは受け付けないということです。


**処理の流れ**

1. プレイヤーが「Space」キーを押したとき、決定の処理を行います。
2. しかし、次に「Space」キーが押されるまでは、再度決定処理が行われないようにします。これにより、連続してメニューが選択されることを防ぎます。


#### まとめ

- キャラクター移動の場合:

連続入力を**許可します**。キーボードを長押しすると、キャラクターが**移動し続ける**ようにします。

- メニュー操作の場合:

連続入力を**許可しません**。キーボードを長押ししても、**一度しか処理を行いません**。

---

このように、場面によってキーボード入力の扱いが異なることを理解し、連続入力が必要なケースとそうでないケースを明確に分けて考えることが大切です！

</div>

<br>
<br>

## 釣りをする

[基礎編6](basic06.html)で作った`randomfish.py`を組み合わせて、スペースキーを押したときに釣りができるようにしましょう。

まず、`random`モジュールをインポートしてください。

```python{}
import random
```

<br>

次に、魚のデータを関数`gameLoop`の**前に追加**してください。

```python{.numberLines startFrom=47 caption="game01.py（抜粋）"}
#>>魚のデータ>>
LOW_RARE_FISH = ["アジ","サバ","イワシ"]
MIDDLE_RARE_FISH = ["カワハギ","タチウオ","メバル"]
HIGH_RARE_FISH = ["タイ","スズキ","カサゴ"]

FISH_LIST = []
FISH_LIST.append(LOW_RARE_FISH)
FISH_LIST.append(MIDDLE_RARE_FISH)
FISH_LIST.append(HIGH_RARE_FISH)

FISH_WEIGHT = [75,20,5] #排出率
```

<br>

スペースキーが押されたときに、ランダムで魚を選択するようにしましょう。


```python{.numberLines startFrom=60 caption="game01.py（抜粋）"}
#>>ゲームのメインループ関数>>
def gameLoop():
    global key,currentKey,prevKey
    
    if(("space" in key) and ("space" not in prevKey)):
        selectedFish = random.choice(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0])
        print(selectedFish)
```


**<i class="fa-solid fa-terminal"></i> 実行結果**

```
pressed:space
アジ
released:space
pressed:space
イワシ
released:space
```

これで、**スペースキーを押すとランダムな魚が釣れる**プログラムが完成しました！
ここからは**魚の重さや売値**の概念を追加したり、**リザルト画面**を表示させたり、**キャラクターにアニメーション**をさせたりと、ゲームのクオリティを上げる作業に入っていきましょう。


## 魚の重さや売値を決める

「同じ種類の魚でも、大物が釣れたりすると面白いかも？」と、いうことで、魚のデータを辞書型に変更して、平均の重さやkg単価といったデータを持たせました。

魚のデータを**更新**してください。

```python{.numberLines startFrom=47 caption="game01.py（抜粋）"}
#>>魚のデータ>>
LOW_RARE_FISH = [
        {
        "name":"イワシ",
        "aveWeight":0.12, #平均重量
        "price":60 #kg単価
        },
        {
        "name":"アジ",
        "aveWeight":0.17,
        "price":100
        },
        {
        "name":"サバ",
        "aveWeight":0.35,
        "price":50
        },
    ]
MIDDLE_RARE_FISH = [
        {
        "name":"タチウオ",
        "aveWeight":3,
        "price":12
        },
        {
        "name":"カワハギ",
        "aveWeight":0.4,
        "price":80
        },
        {
        "name":"メバル",
        "aveWeight":0.43,
        "price":100
        },
    ]
HIGH_RARE_FISH = [
        {
        "name":"タイ",
        "aveWeight":5.4,
        "price":20
        },
        {
        "name":"スズキ",
        "aveWeight":5.5,
        "price":19
        },
        {
        "name":"カサゴ",
        "aveWeight":1.65,
        "price":65
        },
    ]

FISH_LIST = []
FISH_LIST.append(LOW_RARE_FISH)
FISH_LIST.append(MIDDLE_RARE_FISH)
FISH_LIST.append(HIGH_RARE_FISH)

FISH_WEIGHT = [75,20,5] #排出率
```

データを更新してプログラムを実行してみると、ランダムな辞書型が出力されます。
`print(selectedFish["name"])`で**名前**を、`print(selectedFish["aveWeight"])`
で平均の重さを取得できます。以下のようにすれば、重さや売価もランダムになります。



```python{.numberLines startFrom=107 caption="game01.py（抜粋）"}
#>>ゲームのメインループ関数>>
def gameLoop():
    global key,currentKey,prevKey
    
    if(("space" in key) and ("space" not in prevKey)):
        selectedFish = random.choice(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0])
        #魚の重さを決定(ランダム 0.5~1.5)
        fishWeight = selectedFish["aveWeight"]*random.uniform(0.5, 1.5)
        fishWeight = round(fishWeight,2) #少数第3位で四捨五入
        #重さから売却価格を決定
        fishPrice = fishWeight * selectedFish["price"]
        print(selectedFish["name"])
        print(fishWeight)
        print(fishPrice)
```


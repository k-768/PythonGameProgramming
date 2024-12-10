---
var:
  header-title: "Pythonで釣りゲームを作ろう ゲームづくり編4　マップ上を移動しよう"
  header-date: "2024年12月10日（火）"
---

# ゲームづくり編4　マップ上を移動しよう

## キャラクタを動かす

マップ画面を表示するプログラムが完成したので、次はキャラクタを操作してマップ上を移動できるようにしましょう。
今回は、**キャラチップ**と呼ばれる画像を用いてキャラクタの歩行を行います。

<br>

## もくじ
- [](advance04.html#)


## キャラチップとは

**キャラチップ**とは、ゲーム制作においてキャラクターのアニメーションを表現するための、複数のキャラクター画像が並べられた画像です。キャラクターチップとも呼ばれることがあります。

![img](./figs/104/character.png)


ゲーム内では、プログラムでキャラチップの一部を切り出し、画面上に描画します。今回は、「どの方向を向いているか」に応じてキャラチップの行を、「移動の状態」に応じてキャラチップの列を選択して表示します。

上の画像をダウンロードして`character.png`という名前で`img`フォルダに入れておいてください。

## キャラクターを表示させて移動する

新しいpythonファイル`move01.py`を作成してください。[ここから](https://github.com/k-768/PythonGameProgramming/blob/main/programs/move01.py
)プログラムをコピー＆ペーストして実行してみてください。**WASDでキャラクターが移動します**。このプログラムの要点について解説します。

![img](./figs/104/walk.gif)

<br>


```python{.numberLines startFrom=76 caption="move01.py"}
#>>キャラクター>>
CHARA_WIDTH = 64  #キャラの幅
CHARA_HEIGHT = 96 #キャラの高さ

#キャラクターのマップ座標
charaX = 2 
charaY = 2 
charaD = 1  #キャラの向き
flag = "default"
'''
default:通常状態
move:移動中
'''
```

`charaX`と`charaY`は、キャラクターの座標を示す変数です。しかしこれは普通のxy座標ではなく、マップ座標、つまり左上から**何マス目**かを示しています。
`charaD`はキャラクタの方向を示す変数です。下向きが0、左向きが1、右向きが2、上向きが3と、キャラチップの並びと同じ順番になっています。

![img](./figs/104/charaD.png)

`flag`は、魚を釣るプログラムでも登場した、場面を管理するためのものです。今回は待機中は`default`、移動中は`move`です。**キーボードの入力は待機中のみ受け付け、移動中は受け付けません**。

<br>

```python{.numberLines startFrom=95 caption="move01.py"}
#移動方向
moveX = 0
moveY = 0
```
`moveX`、`moveY`は移動するマス目を示しています。たとえば、`moveX = -1`なら、**1マス左に移動する**ということになります。

<br>


```python{.numberLines startFrom=99 caption="move01.py"}
#キャラチップを1毎の画像に並べたキャラシートを読み込む
CHARA_SHEET = Image.open(cwd+"/img/character.png")

#読み込んだ画像から縦横何枚ずつチップがあるか求める
CHARA_X = CHARA_SHEET.width // CHARA_WIDTH
CHARA_Y = CHARA_SHEET.height // CHARA_HEIGHT


#キャラチップに分割し2次元配列に格納する
CHARA_CHIP = []
#キャラシートの列数だけ繰り返す
for j in range(CHARA_Y): 
    #新しい行を作成
    row = []
    
    #キャラシートの行数だけ繰り返す
    for i in range(CHARA_X): 
        # キャラクターのチップを切り出して画像を作成
        image = ImageTk.PhotoImage(CHARA_SHEET.crop((
            CHARA_WIDTH * i,               # 左上のX座標
            CHARA_HEIGHT * j,              # 左上のY座標
            CHARA_WIDTH * (i + 1),         # 右下のX座標
            CHARA_HEIGHT * (j + 1)         # 右下のY座標
        )))
        
        # 作成した画像を行に追加
        row.append(image)
    
    # 行をCHARA_CHIPに追加
    CHARA_CHIP.append(row)
```

`99行目`からはキャラチップの画像を、マップチップとほとんど同じ方法で取得しています。
ただし、マップチップはリストに格納していましたが、**キャラチップは2次元リストに格納しています**。


---

- **ChallengeA4-1**　`CHARA_CHIP[1][2]`はどこの部分を指しますか。

![img](./figs/104/character.png)


回答はコラムの後にあります。

<div class="note type-tips">

**リストの内包表記**

Pythonの便利な文法の一つに**内包表記**というものがあります。**「リストを簡単に作れる書き方」**です。

```python{.numberLines startFrom=1 caption="リストの内包表記"}
CHARA_CHIP = [
    [
        ImageTk.PhotoImage(CHARA_SHEET.crop((
            CHARA_WIDTH * i,
            CHARA_HEIGHT * j,
            CHARA_WIDTH * (i + 1),
            CHARA_HEIGHT * (j + 1)
            ))) for i in range(CHARA_X)
        ]for j in range(CHARA_Y)
    ]
```

```python{.numberLines startFrom=1 caption="リストの内包表記を使わない場合"}
CHARA_CHIP = []
#キャラシートの列数だけ繰り返す
for j in range(CHARA_Y): 
    #新しい行を作成
    row = []
    
    #キャラシートの行数だけ繰り返す
    for i in range(CHARA_X): 
        # キャラクターのチップを切り出して画像を作成
        image = ImageTk.PhotoImage(CHARA_SHEET.crop((
            CHARA_WIDTH * i,               # 左上のX座標
            CHARA_HEIGHT * j,              # 左上のY座標
            CHARA_WIDTH * (i + 1),         # 右下のX座標
            CHARA_HEIGHT * (j + 1)         # 右下のY座標
        )))
        
        # 作成した画像を行に追加
        row.append(image)
    
    # 行をCHARA_CHIPに追加
    CHARA_CHIP.append(row)
```

このように、同じ処理でも簡単に記述できます。リストの内包表記をざっくり説明すると、ループを使ってリストを作るコードを1行にまとめる方法です。しかし、少し理解が難しいので今回は扱いません。気になった方は自分で調べてみてください。

</div>

**<i class="fa-solid fa-check"></i>解答**

![img](./figs/104/ans.png)

<br>

---

プログラムの解説に戻ります。



しかし、直立不動で移動していたり、水の上を歩いていたりと、このままではおかしなところがたくさんあります。

![img](./figs/104/walk.gif)



## キャラクターをアニメーションさせる


![img](./figs/104/walk.png)



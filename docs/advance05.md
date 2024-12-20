---
var:
  header-title: "Pythonで釣りゲームを作ろう ゲームづくり編5　ゲームを完成させよう"
  header-date: "2024年12月15日（日）"
---

# ゲームづくり編5　ゲームを完成させよう

今回は、ゲームにとって欠かせないセーブ機能を実装しましょう。そして、釣りのシステムと移動のシステムを組み合わせて、釣りゲームを完成させましょう。

<br>

## もくじ
- [](advance05.html#)





## JSONとは

今回は、ゲームの進行状況を保存するために JSON（JavaScript Object Notation） を用います。釣った魚の情報やキャラクターの位置、レベルなどを保存するのに使います。JSONはPythonで簡単に操作できるため、初心者にも扱いやすいのが特徴です。**リストや辞書型に似た形式で、Pythonのリストや辞書型と相互変換が可能**です。

## JSONを書く

**これがJSONファイルです**。Pythonと同じような感覚で記述することができます。
それぞれのデータの意味は以下のようになっています。本来は、イワシの後にサバやアジ、...、タイと続きますが、長くなるので省略します。

```json{.numberLines startFrom=1 caption="savedata.json（解説付き）"}
{
    "イワシ": {
        "count": 0, //イワシを釣った回数
        "maxWeight": 0, //釣ったイワシの最大重量
        "bronze": false, //ブロンズランクのイワシを釣ったことがあるか
        "silver": false, //シルバーランクのイワシを釣ったことがあるか
        "gold": false, //ゴールドランクのイワシを釣ったことがあるか
        "totalWeight": 0 //釣ったイワシの累計重量
    },
    "money": 0,//所持金
    "x": 3,//キャラクターのマップx座標
    "y": 3,//キャラクターのマップy座標
    "d": 0,//キャラクターの向き
    "lv": 0//キャラクターのレベル
}
```

## JSONを読み込む

`save_load.py`という名前で新しいファイルを作成してください。

```python{.numberLines startFrom=1 caption="save_load.py"}
import json
import os

cwd = os.getcwd()  # カレントディレクトリ取得

try:
    with open(cwd + "/savedata.json") as f:
        saveData = json.load(f)
    print("セーブデータを読み込みました:", saveData)
except:
    saveData = {
        "イワシ": {
            "count": 0,
            "maxWeight": 0,
            "bronze": False,
            "silver": False,
            "gold": False,
            "totalWeight": 0
        },
        "money": 0,
        "x": 3,
        "y": 3,
        "d": 0,
        "lv": 0
    }
    print("新しいセーブデータを作成しました。")
```

ここで、新しい構文、`try-except構文`について説明します。

Pythonの`try-except構文`は、プログラム実行中に発生する**エラーに対処するための仕組み**です。この構文を使うことで、**プログラムがエラーで突然終了するのを防ぎ、エラー時に適切な処理を実行でき**ます。

```python{.numberLines startFrom=1 caption="try-except構文"}
try:
    # エラーが発生する可能性がある処理
except エラーの種類:
    # エラーが発生した場合の処理
```

今回の場合は、`try:`で`savedata.json`を**開きます**。これにより、もしセーブデータがあれば**セーブデータを読み込み（コンティニュー）**ます。もしセーブデータがなければ、`savedata.json`ファイルを開くことができず、エラーが発生します。そのとき、ファイルを開くのをやめ、**新しいファイルを作成（ニューゲーム）**します。

<br>

## 釣りができるかどうか判定する

そのまま釣りのシステムと移動のシステムを組み合わせると、想定外の動作が発生することがあります。 **キャラクターがどこでも釣りをできる状態となり、陸地でも釣りが可能になってしまいます**。

そこで、キャラクターの**目の前が水である場合のみ**釣りができるようにしましょう。そのために、**釣りができるか判定する関数**を作成します。

新しいpythonファイル`move_check.py`を作成してください。[ここから](https://github.com/k-768/PythonGameProgramming/blob/main/programs/move_check.py
)プログラムをコピー＆ペーストして実行してみてください。

水辺に到達すると頭上に**釣りアイコン**が表示されます。

![img](./figs/105/check.png)

<br>

---

まず、このプログラムにおいて釣りが可能なマップチップを指定するリスト`FISHING_PERMIT`を用意します。このリストは、各マップチップが釣り可能かどうかを判定するために使用されます。

```python{.numberLines startFrom=72 caption="move_check.py（抜粋）"}
#釣り可能設定
#0:不可
#1:可能
FISHING_PERMIT = [0,0,0,1]
```

リストのインデックスは、`MAP_DATA` の値に対応しています。
各インデックスの値が0なら、**このマップチップでは釣りができない**、1なら**このマップチップで釣りが可能**であることを示しています。今回は、`FISHING_PERMIT[3]`のみ**1**、つまりマップチップIDが3の**水**タイルでのみ釣りが可能だということになります。

---

`110行目`からの関数で、**キャラクターの目の前のタイルが釣り可能かどうかを判定し、釣りアイコンを表示**します。

```python{.numberLines startFrom=110 caption="move_check.py（抜粋）"}
#前のタイルが釣り可能ならば釣りアイコンを表示する関数
def setFishingIcon(x,y,d):
    """
    x:キャラのx座標
    y:キャラのy座標
    d:キャラの向き
    """
    global fishFlag
    
    if d == 0:#下向き
        moveX = 0
        moveY = 1
    elif d == 1:#左向き
        moveX = -1
        moveY = 0
    elif d == 2:#右向き
        moveX = 1
        moveY = 0
    elif d == 3:#上向き
        moveX = 0
        moveY = -1
    
    
    # 移動先がマップ範囲内ならば
    if 0 <= y+moveY < len(MAP_DATA) and 0 <= x+moveX < len(MAP_DATA[0]):
        #前のマスが釣り可能ならば
        if FISHING_PERMIT[MAP_DATA[y+moveY][x+moveX]]:
            setIcon(x,y,"fishing")
            print(f"you can fishing @({x+moveX},{y+moveY})")
            fishFlag = True
        else:
            fishFlag = False
    else:
        # 移動先がマップ範囲外
        fishFlag = False
```

## 全体の組み立て

![img](./figs/105/main.svg)

新しいpythonファイル`game.py`を作成してください。[ここから](https://github.com/k-768/PythonGameProgramming/blob/main/programs/game.py
)プログラムをコピー＆ペーストして実行してみてください。
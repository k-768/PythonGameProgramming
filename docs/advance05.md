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

## 全体の組み立て

![img](./figs/105/main.svg)

新しいpythonファイル`game.py`を作成してください。[ここから](https://github.com/k-768/PythonGameProgramming/blob/main/programs/game.py
)プログラムをコピー＆ペーストして実行してみてください。
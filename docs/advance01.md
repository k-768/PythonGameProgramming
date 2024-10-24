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

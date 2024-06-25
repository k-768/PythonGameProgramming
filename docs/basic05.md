---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編5　if文"
  header-date: "2024年04月23日（月)"
---

# 基礎編5　if文 

## もくじ

-  [if文](basic05.html#if文) 
-  [関係演算子](basic05.html#関係演算子)
-  [if-else文](basic05.html#if-else文) 
-  [if-elif文](basic05.html#if-elif文) 

## 条件分岐とは

![img](figs/05/walk.png)

RPGのマップ移動を例に考えてみましょう。キーボード入力によって進む方向が変わります。


- Wキー　→　上に進む
- Aキー　→　左に進む
- Sキー　→　下に進む
- Dキー　→　右に進む

このようにゲームでは様々な条件によって処理を変更しています。Pythonでは、`if文`を用いて条件分岐を記述します。

## if文
`if文`の構造を見ていきましょう。

```python{.numberLines caption="if文の構造"}
if a > 0:
  print("aは正の値です")
```

1行目`if`と`:`に囲まれた部分が**条件を示す部分**です。この例では、「aが0以上」になります。

そして、2行目は、**1行目の条件を満たした時実行される部分**です。**インデント**([参照](basic04.html#インデント))する必要があります。

インデントした部分を**ブロック**と言い、条件を満たした時、すぐ後ろのブロックが**全て実行されます**。

```python{.numberLines caption="ブロック"}
if 条件:
  処理A
  処理B
  処理C
  ...
```
以下のプログラムを実行してみましょう。

```python{.numberLines caption="test5-1.py"}
a = 1
b = -1
if a > 0:
  print("aは正の値です")
  print("a:"+str(a))

if b > 0:
  print("bは正の値です")
  print("b:"+str(b))
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
aは正の値です
a:1
```

3行目

## 関係演算子



リストは、**変数をセットで管理できる便利なもの**です。
例えば、以下のようにキャラクターの持ち物を表すことを考えましょう。
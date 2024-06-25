---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編5　if文"
  header-date: "2024年04月23日（月)"
---

# 基礎編5　if文 

## もくじ

-  [条件分岐とは](basic05.html#条件分岐とは) 
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
if a > 0: # a>0なのでここは実行される
  print("aは正の値です")
  print("a:"+str(a))

if b > 0: # b>0でないのでここは実行されない
  print("bは正の値です")
  print("b:"+str(b))
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
aは正の値です
a:1
```



## 関係演算子

関係演算子は以下のような種類があります。

-----------------------
演算子 記述例 意味 
---- ------ --------------
==   a==b   aとbが等しい 

!=   a!=b   aとbが等しくない(≠) 

>    a>b    aがbより大きい 

<    a<b    aがbより小さい 

>=   a>=b   aがb以上 

<=   a<=b   aがb以下
----------------------- 

## if-else文

`else`を用いて、**条件が満たされなかったときの処理を設定する**ことができます。

```python{.numberLines caption="if-else文の構造"}
if a > 0:
  print("aは正の値です")
else:
  print("aは正の値ではありません")
```

- `a`が0より大きいとき、条件を満たすので、「aは正の値です」と出力されます。
- `a`が0以下のとき、条件を満たさないので、「aは正の値ではありません」と出力されます。

## if-elif文

`elif`を用いて、**細かく条件を設定する**ことができます。

```python{.numberLines caption="if-elif文の構造"}
if a > 0:
  print("aは正の値です")
elif a == 0:
  print("aは0です")
else:
  print("aは負の値です")
```
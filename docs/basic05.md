---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編5　if文"
  header-date: "2024年04月23日（月)"
---

# 基礎編5　if文 

if文を使えば、条件分岐をつくることができます。条件分岐なしにはゲームはつくれません。
たとえば、RPGでは押したボタンによって攻撃したり、技を使ったり、逃げたりと、様々な分岐があります。
プレイヤーが行動を選択できなければ、ただのアニメーションですからね。

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
if a > 0: # a>0であれば
  print("aは正の値です")
  print("a:"+str(a))

if b > 0: # b>0であれば
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
import random
weight = random.randint(50,150) #50から150までの乱数
if weight > 100: # weight>100であれば
  print(str(weight)+"gの大物が釣れた！")
else: # weight>100でなければ
  print(str(weight)+"gの魚が釣れた！")
```

- `weight`が100より大きいとき、条件を満たすので、「XXgの大物が釣れた！」と出力されます。
- `weight`が0以下のとき、条件を満たさないので、「XXgの魚が釣れた！」と出力されます。

## if-elif文

`elif`を用いて、**細かく条件を設定する**ことができます。

```python{.numberLines caption="if-elif文の構造"}
if a > 0:　#a>0であれば
  print("aは正の値です")
elif a == 0: #a>0でなく、a==0であれば
  print("aは0です")
else: #どちらでもなければ
  print("aは負の値です")
```

`if-elif文`が用いられる代表的な例としては、**キーボードによるキャラクター移動**が挙げられます。

```python{.numberLines caption="move.py"}
key = "w"
if key == "w":　
  print("奥に進みます")
elif key == "a":
  print("左に進みます")
elif key == "s":
  print("手前に進みます")
elif key == "d":
  print("右に進みます")
else: 
  print("不正な入力です")
```

<div class="note type-tips">

**if文とif-elif文の違い**

下の二つのプログラムを実行して、違いを確認しましょう。

</div>
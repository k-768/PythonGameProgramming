---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編3　変数"
  header-date: "最終更新日：2024年10月29日（火）"
---

# 基礎編3　変数 

変数は、ゲームを作るうえで欠かせない存在です。変数を用いることで、**プレイヤー名や所持金、レベルや持ち物**といった、**状況に応じて変化するもの**を扱うことができます。
ここでは、変数の使い方や命名規則について学ぶことができます。

## もくじ

-  [変数とは](basic03.html#変数とは) 
-  [変数の値を変更する](basic03.html#変数の値を変更する) 
-  [変数の命名](basic03.html#変数の命名) 


## 変数とは

![img](figs/03/var.png)

変数とは、**データを入れておく箱**のようなもので、箱の中身は**いつでも確認したり変更することができます**。
変数`a`に値`10`を入れるときは、以下のように書きます。


```python
a = 10
```
この変数に値を入れる`=`は、**代入演算子**と呼ばれます。

</br>

---

変数に入れた値は、**簡単に**取り出すことができます。print文の`()`の中に変数名を記述するだけです。

```python{.numberLines caption="test3-1.py"}
a = 10
print(a)
```
**<i class="fa-solid fa-terminal"></i> 実行結果**

```
10
```

1行目で変数`a`に10を代入しています。そのため、2行目のprint文の`()`の中の`a`は10と読み替えられました。

<br>
<div class="note type-tips">

**「=」の使い方に注意!!**

代入演算子`=`は、**数学で使うものとは意味が異なり、左の変数に右の値を代入するはたらき**を持ちます。
そのため、以下のプログラムを実行するとエラーが起きます。

```python{.numberLines caption="test.py"}
10 = a
print(a)
```
**<i class="fa-solid fa-terminal"></i> 実行結果**

```
PS C:\******> & C:/******/python.exe c:/******/test.py
  File "c:\******\test.py", line 1
    10 = a
    ^^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```

「`10`は**変数ではないので代入できません**」と言われてしまいます。

--- 

ここで、エラーの読み方について簡単に説明します。

```
  File "c:\******\test.py", line 1
```
2行目では、**エラーが起きた場所**を示しています。今回は`test.py`というファイルの`1行目`です。

```
    10 = a
    ^^
```
3~4行目では、**エラーが起きた場所の詳細**を`^`で示しています。今回は`10`が強調されています。

```
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
```
5行目では、**エラーの内容**を示しています。今回は**文字列に代入することはできません**と表示されました。

エラーコードはプログラムの誤っている箇所を特定、修正するためにとても重要です。

</div>

---

![img](figs/03/str.png)

もちろん、変数には**文字列も代入できます**。文字列の場合は、**`"`で囲う**のでしたね。
これは「hello」と書くと**変数とみなされてしまう**ので、**変数と区別するため**だったわけです。


</br>

```python{.numberLines caption="test3-2.py"}
b = "hello!"
print(b)
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
hello!
```

</br>

## 変数の値を変更する

変数に代入し直せば、変数の値を変更することができます。

```python{.numberLines caption="test3-3.py"}
a = 10
print(a)
a = 20
print(a)
```
**<i class="fa-solid fa-terminal"></i> 実行結果**

```
10
20
```

<br>

---

**`a = a + 2`と書けば、`a`の値を2だけ増やすことができます**。


```python{.numberLines caption="test3-4.py"}
a = 10
print(a)
a = a + 2
print(a)
```
**<i class="fa-solid fa-terminal"></i> 実行結果**

```
10
12
```

---

- **Challenge3-1**　上のプログラムの1行目を書き換えて、`a`の値を`123`に変更しましょう。
- **Challenge3-2**　3行目を書き換えて、`a`の値を**2倍**にするよう変更しましょう。

**<i class="fa-solid fa-check"></i>解答**

Challenge3-1: <span class="masked">`a = 123`</span>

Challenge3-2: <span class="masked">`a = a * 2`</span>

</br>

---

**複数の文字列も、`+`を用いてつなぐことができます**。
```python{.numberLines caption="test3-5.py"}
name = "Kosen Taro"
print(name)
print("Hello! "+name+"!")
```
**<i class="fa-solid fa-terminal"></i> 実行結果**

```
Kosen Taro
Hello! Kosen Taro!
```
---

<br>
<div class="note type-tips">

**数値と文字列の結合**

数値同士、文字列同士は`+`を用いて結合できますが、数値と文字列はそのまま結合できません。
そのため、以下のプログラムを実行するとエラーが起きます。

```python{.numberLines caption="test.py"}
score = 100
print("あなたのスコア:" + score)
```
**<i class="fa-solid fa-terminal"></i> 実行結果**

```
PS C:\******> & C:/******/python.exe c:/******/test.py
  File "c:\******\test.py", line 2 in <module>  
    print("あなたのスコア:" + score)
          ~~~~~~~~~~~^~~~~~~
TypeError: can only concatenate str (not "int") to str
```

「**文字列には文字列しか結合できません**」と言われてしまいます。
そのため、数値を文字列に変換する操作が必要です。`str()`を用いて変換できます。

```python{.numberLines caption="test.py"}
score = 100
print("あなたのスコア:" + str(score))
```
**<i class="fa-solid fa-terminal"></i> 実行結果**

```
あなたのスコア:100
```

</div>


## 変数の命名規則

変数名のつけ方には以下の決まりがあります。

### 半角のアルファベット、数字、`_`(アンダースコア)を組み合わせる

日本語やその他の記号は使わないようにしましょう。

```python{.numberLines caption="⭕良い例"}
a = 10
player1 = "Taro"
stage_name = "Island"
```
```python{.numberLines caption="❌悪い例"}
ｓｃｏｒｅ = 99    <-全角
曜日 = "sunday"    <-変数名が日本語
stage2-1 = "Ocean" <-「-」は引き算の記号として認識される
```

### 最初の文字には数字を使わない

2文字目以降は自由に使えます。

```python{.numberLines caption="⭕良い例"}
player1 = "Taro"
```
```python{.numberLines caption="❌悪い例"}
1st_player = "Tom"
```

### 予約語を使わない

たとえば`print`のような、Pythonへの命令として決まっている単語をそのまま使うことはできません。

```python{.numberLines caption="❌悪い例"}
print = 5
print(print)
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
PS C:\******> & C:/******/python.exe c:/******/test.py
  File "c:\******\test.py", line 2, in <module>
    print(print)
TypeError: 'int' object is not callable
```

1行目でprintに値が上書きされてしまったので、その後ろではprint文が使えなくなってしまいます。

---

ここからは読みやすいコードにするためのマナーです。(絶対に守る必要はありませんが、一般的な規則です)


### 大文字は使わない

変数の名前は**全て小文字**にするのが一般的です。

```python{.numberLines caption="⭕良い例"}
player1 = "Taro"
```
```python{.numberLines caption="❌悪い例"}
Player1 = "Taro"
```

### 単語間は`_`でつなぐ

```python{.numberLines caption="⭕良い例"}
player_name = "Taro"
max_size = 12
```

### 極端に長い・短い名前は避ける

長すぎると読みにくく、短すぎると何を示す変数かわからなくなるので避けましょう。

```python{.numberLines caption="⭕良い例"}
max_mapsize_x = 64
score = 1100
```
```python{.numberLines caption="❌悪い例"}
maximum_value_in_the_x_direction_on_the_map_screen = 64
s = 1100

```

#### **Challenge3-3** 次の変数名は適切か判断しましょう。

- `tmp` ・・・ <span class="masked">⭕　　　　　　　　　　　　　　</span>
- `Name` ・・・ <span class="masked">❌全て小文字にするべきです</span>
- `24th_anniversary` ・・・ <span class="masked">❌最初の文字は数字ではいけません</span>
- `g20` ・・・ <span class="masked">⭕　　　　　　　　　　　　　　</span>
- `ともだち` ・・・ <span class="masked">❌変数名を日本語にすることは避けましょう</span>
- `high-school` ・・・ <span class="masked">❌`-`(ハイフン)は引き算として認識されてしまいます</span>

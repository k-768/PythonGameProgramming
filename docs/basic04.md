---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編4　構文"
  header-date: "2024年04月23日（月)"
---

# 基礎編4　構文 

## もくじ

-  [コメント文](basic04.html#コメント文) 
-  [式の構造](basic04.html#式の構造) 

## コメント文
文頭に`#`をつけることで、**コードに注釈をつける**ことができます。
これを**コメント文**と言い、プログラムには**全く影響しません**が、見やすいコードにすることができます。

</br>

```python{.numberLines}
#挨拶をする
print("Hello World!!")
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
Hello World!!
```

</br>
1行の途中からコメント文を始めることもできます。
</br>

```python{.numberLines}
name = "Kosen Taro" #プレイヤー名
print("Hello!"+name+"!")
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
Hello!Kosen Taro!
```

</br>

このように、プログラムを実行したときに`#`より後ろは**すべて無視**されます。
そのため、以下のようにいらなくなった行を**一時的に無効化**することができます。

</br>

```python{.numberLines}
name = "Kosen Taro"
#print("Hello!"+name+"!")
print("Hey!"+name+"!")
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
Hey!Kosen Taro!
```

</br>

これを**コメントアウト**と言います。

<div class="note type-tips">

**コメントアウトの使い過ぎに注意!!**

大きなプログラムを書く時など、命令を消すことなく残しておけるのでついつい多用しがちですが、可読性が下がるので使い過ぎには注意しましょう。

</div>

複数行にわたってコメントを書きたい場合は、以下のように`"`(ダブルクォーテーション)3つの間に書きます。

```python{.numberLines}
"""
これはnameに入っている名前を取得し、
挨拶をするプログラムです。
"""
name = "Kosen Taro"
print("Hey!"+name+"!")
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
Hey!Kosen Taro!
```
<br>

<div class="note type-tips">

**コメントアウトのショートカット**

コメントアウトしたい部分を選択し、`Ctrl-/`で一度にコメントアウトすることができます。
もう一度`Ctrl-/`を押すとコメントアウトを解除できます。**非常によく使うので覚えておきましょう**。

</div>
<br>

## 式の構造

プログラムの書き方にはいくつかの決まりがあります。

### 改行

プログラムに記載されたそれぞれの命令は、**改行ごとに1文とみなされます**。そのため、正しくない改行をするとエラーになります。

```python{.numberLines caption="⭕良い例"}
print("OK")
print("GOOD")
```
```python{.numberLines caption="❌悪い例1"}
print("NG")print("BAD")
```
```python{.numberLines caption="❌悪い例2"}
pri
nt("NG")
```

### インデント

Pythonでは、**インデント**(行頭のスペース)は大きな意味を持ちます。
基礎編6、7で紹介する`for文`や`if文`では、インデントが必要になります。
逆に、今までのプログラムの行頭に空白を入れると、エラーになります。

```python{.numberLines caption="⭕良い例"}
print("OK")
```
```python{.numberLines caption="❌悪い例"}
 print("NG")
```

### 文中のスペース

変数の宣言や命令の()内のスペースは、**あってもなくてもかまいません**。

```python{.numberLines caption="⭕良い例"}
print("OK")
print( "OK" )
n=1
n = 1
```


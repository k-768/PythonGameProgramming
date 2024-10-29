---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編2　文字の出力"
  header-date: "最終更新日：2024年10月29日（火）"
---

# 基礎編2　文字の出力 

## もくじ

-  [Print文](basic02.html#Print文) 
-  [文字列](basic02.html#文字列) 
-  [四則演算](basic02.html#四則演算) 
-  [その他の演算](basic02.html#その他の演算) 
-  [演算の順序](basic02.html#演算の順序) 

## print文
`print()`を用いて、コマンドプロンプトに文字を表示することが出来ます。
`()`の中に表示したいものを記述します。試しに、`1`と表示させてみましょう。
**注：カッコは半角です！**

</br>

```python{.numberLines}
print( 1 )
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
1
```

</br>


## 文字列
`print()`を用いて、コマンドプロンプトに文字を表示することが出来ます。
`()`の中に表示したいものを記述するのですが、日本語や英語など、**文字列を表示する時には`"(ダブルクォーテーション)`で囲み**ます。`Shift + 2`で入力できます。試しに、「Hello World!!」と表示させてみましょう。

</br>

```python{.numberLines caption="HelloWorld.py"}
print("Hello World!!")
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
Hello World!!
```

</br>

## 四則演算

Pythonを用いて、簡単な計算をしてみましょう。

</br>

```python{.numberLines caption="sum.py"}
print(2+3)
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
5
```

</br>

カッコの中に`2+3`と記述すれば、それを計算して結果が出力されます。
四則演算を行う際には以下の**演算記号**を用います。

| 演算　 | 記号 |
--------+-------
| 足し算 | 　+   |
| 引き算 | 　-   |
| 掛け算 | 　*   |
| 割り算 | 　/   |

<div class="note type-tips">

**記号は半角!**

掛け算や割り算は、普段使用する「×」「÷」とは**異なる記号を使用**するため要注意です。
いずれも、**全角ではなく半角**であることに注意してください。

| 全角 | 　半角 |
--------+-------
| ＋ | 　+   |
| ー | 　-   |

</div>


#### **charenge2-1** 次の計算をPythonでしてみましょう。

- 4+6 ・・・ <span class="masked">`4+6`</span>
- 5-2 ・・・ <span class="masked">`5-2`</span>
- 6×3 ・・・ <span class="masked">`6*3`</span>
- 12÷4 ・・・ <span class="masked">`12/4`</span>

## その他の演算

| 演算　 | 記号 |
--------+-------
| 商の整数値 | 　//   |
| 余り | 　%   |
| べき乗 | 　**   |

例えば7÷3=2あまり1を計算したいとき、`//`を用いて割り切れた数を、`%`を用いてあまりを求めることができます。

#### **charenge2-2** 次の計算をPythonでしてみましょう。

- 7÷3の商の整数値 ・・・ <span class="masked">`7//3`</span>
- 7÷3の余り ・・・ <span class="masked">`7%3`</span>
- 2の8乗 ・・・ <span class="masked">`2**8`</span>

<br>

## 演算の順序

計算の順序は数学と同じです。

- 基本的に**前から**計算される
- 加減算より**乗除算**が優先される
- **()**を用いて優先順位をつけることができる

```python{.numberLines caption="sum.py"}
print(2+3*4)
print((2+3)*4)
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
14
20
```
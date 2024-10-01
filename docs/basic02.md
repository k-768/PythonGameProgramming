---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編2　文字の出力"
  header-date: "2024年04月23日（月)"
---

# 基礎編2　文字の出力 

## もくじ

-  [Print文](basic02.html#Print文) 
-  [文字列](basic02.html#文字列) 
-  [整数と小数](basic02.html#整数と小数) 
-  [四則演算](basic02.html#四則演算) 

## print文
`print()`を用いて、コマンドプロンプトに文字を表示することが出来ます。
`()`の中に表示したいものを記述します。試しに、`1`と表示させてみましょう。

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
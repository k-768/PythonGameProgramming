---
var:
  header-title: "Pythonで釣りゲームを作ろう 第01回"
  header-date: "2024年04月23日（月)"
---

# 第1回 

## 乱数
`random`モジュールを用いると、ランダムな数を生成したり、リストからランダムに抽出することができます。

### random.randint()
`random.randint(a,b)`を使って**a~b**までの整数を生成します。

以下のコードを実行してみてください。さいころと同じふるまいをします。

```python
import random

print(random.randint(1,6))
```


**<i class="fa-solid fa-terminal"></i> 実行結果**

```
3
```

</br>

---

- **Challenge1**　上のプログラムを改造して、1~50までの乱数を表示するプログラムを作成しましょう。
- **Challenge2**　さらに改造して、2~100までのランダムな**偶数**を表示するプログラムを作成しましょう。

ヒント: <span class="masked">`2から100までの偶数を数学的に書くと`2n (1 <= n <= 50)`となります。`</span>


**<i class="fa-solid fa-check"></i>解答**

Challenge1: <span class="masked">`print(random.randint(1,50))`</span>

Challenge2: <span class="masked">`print(random.randint(1,50) * 2)`</span>

</br>

### random.choice()
`random.choice(list)`を使って`list`からランダムに要素を選択します。

以下のコードを実行してみてください。魚の名前が入ったリストからランダムに選択して表示します。

```python
import random

fishes = ["アジ","サバ","イワシ","タイ","サメ"]
print(random.choice(fishes))
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
アジ
```
</br>

### random.choices()
`random.choices(list,k,weights)`を使って`list`からランダムに複数の要素を選択します。

`random.choices()`で選択された要素は**重複することがあります。**重複させたくない場合は`random.sample()`が用意されています。

以下のコードを実行してみてください。魚の名前が入ったリストからランダムに3つ選択して表示します。

```python
import random

fishes = ["アジ","サバ","イワシ","タイ","サメ"]
print(random.choices(fishes,k=3))
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
['タイ', 'イワシ', 'イワシ']
```
</br>

さらには重みをつけることもできます。引数`weights`で確率を指定します。

```python
import random

fishes = ["アジ","サバ","イワシ","タイ","サメ"]
fish_weights =[30,30,30,8,2] #アジ,サバ,イワシ30%、タイ8%、サメ2%
print(random.choices(fishes,k=10,weights = fish_weights))
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
['サバ', 'イワシ', 'アジ', 'サメ', 'アジ', 'サバ', 'イワシ', 'アジ', 'イワシ', 'イワシ']
```
</br>

`random.choices(・・・)[0]`と指定することで、配列からランダムな要素を重み付きで取り出せます。
```python
import random

fishes = ["アジ","サバ","イワシ","タイ","サメ"]
fish_weights =[30,30,30,8,2] #アジ,サバ,イワシ30%、タイ8%、サメ2%
print(random.choices(fishes,k=1,weights = fish_weights)[0])
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
イワシ
```
</br>

これを使えばガチャやおみくじなども作ることができます。
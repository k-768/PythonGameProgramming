---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編5"
  header-date: "2024年04月23日（月)"
---

# Pythonで釣りゲームを作ろう 基礎編5

## もくじ

-  [モジュール](basic02.html#モジュール) 
-  [乱数](basic02.html#乱数) 

## モジュール

複雑なプログラムを作成するとき、1から自分で作成するのは大変です。そこで、

## 乱数
`random`モジュールを用いると、ランダムな数を生成したり、リストからランダムに抽出することができます。

### random.randint()

![img](figs/05/dice.png)

`random.randint(a,b)`を使って**a~b**までの整数を生成します。

以下のコードを実行してみてください。さいころと同じふるまいをします。

```python{.numberLines}
import random

print(random.randint(1,6))
```


**<i class="fa-solid fa-terminal"></i> 実行結果**

```
3
```

</br>

---

- **Challenge1-1**　上のプログラムを改造して、1~50までの乱数を表示するプログラムを作成しましょう。
- **Challenge1-2**　さらに改造して、2~100までのランダムな**偶数**を表示するプログラムを作成しましょう。

ヒント: <span class="masked">`2から100までの偶数を数学的に書くと`2n (1 <= n <= 50)`となります。`</span>


**<i class="fa-solid fa-check"></i>解答**

Challenge1-1: <span class="masked">`print(random.randint(1,50))`</span>

Challenge1-2: <span class="masked">`print(random.randint(1,50) * 2)`</span>

</br>

### random.choice()
`random.choice(list)`を使って`list`からランダムに要素を選択します。

以下のコードを実行してみてください。魚の名前が入ったリストからランダムに選択して表示します。

```python{.numberLines}
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

```python{.numberLines}
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

```python{.numberLines}
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

<div class="note type-tips">

**配列からランダムな要素を重み付きで取り出す**

`random.choices()`を使えば、`random.choice()`ではできなかった、重みをつけて要素を取り出す操作ができました。
では、**魚の名前のリストではなく魚の名前そのものが欲しいとき、どうすれば良い**でしょうか。

まずは、先ほどのコードを`k=1`と書き換えて実行してみましょう。

```python{.numberLines}
import random

fishes = ["アジ","サバ","イワシ","タイ","サメ"]
fish_weights =[30,30,30,8,2] #アジ,サバ,イワシ30%、タイ8%、サメ2%
print(random.choices(fishes,k=1,weights = fish_weights))
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
['イワシ']
```

</br>

ここで注意したいのは、**`k=1`と指定しても、要素数1の配列が返ってくる**ことです。配列の要素を取り出すには、`list[0]`のように**インデックスで指定**します。

`random.choices(・・・)[0]`と指定することで、配列からランダムな要素を重み付きで取り出せます。
```python{.numberLines}
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

</div>



### 応用

![img](figs/05/sample.gif)

以下の要件を満たすプログラムを作成していきましょう。

- レア度は★1~★3まであり、排出率は以下の通りです。

    **★1**: 75%
    **★2**: 20%
    **★3**: 5%

- それぞれのレア度には3種類の魚があり、以下のリストの通りです。同じレア度の中で何が選ばれるかはランダムです。

```python{.numberLines caption="魚のランク"}
STAR_1 = ["アジ","サバ","イワシ"]
STAR_2 = ["カワハギ","タチウオ","メバル"]
STAR_3 = ["タイ","スズキ","カサゴ"]
```

</br>

先ほどの例をそのまま使えば以下のようになりますが、これではあまりよくありません。

```python{.numberLines caption="良くない例"}
import random

FISH_LIST = ["アジ","サバ","イワシ","カワハギ","タチウオ","メバル","タイ","スズキ","カサゴ"]
FISH_WEIGHT = [25,25,25,20/3,20/3,20/3,5/3,5/3,5/3] #それぞれの排出率
print(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0])
```

要件通りには動くのですが、他人や未来の自分にとって読みにくく、何か改良しようとすると大変なコードです。具体的には以下の欠点が挙げられます。

- どの魚がどのランクなのかわかりにくい
- それぞれのランクの排出率がわかりにくい
- 魚の種類を追加したとき、`FISH_WEIGHT`を何か所も変更する必要がある。

</br>

これらを解決するためにはどうすれば良いでしょうか。

今回は**初めにレア度を排出率に従って決定し、次にその中からランダムに魚を選ぶ方法**を取りましょう。まずは排出率に従って「★n」と表示するプログラムを作成します。

```python{.numberLines caption="レア度を排出率に従って決定する"}
import random

FISH_LIST = ["★1","★2","★3"] 
FISH_WEIGHT = [75,20,5] #★1～3の排出率
print(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0])
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
★1
```
</br>

次に、「★n」の部分をそれぞれの魚のリストに置き換えます。

```python{.numberLines caption="レア度を排出率に従って決定する"}
import random

STAR_1 = ["アジ","サバ","イワシ"]
STAR_2 = ["カワハギ","タチウオ","メバル"]
STAR_3 = ["タイ","スズキ","カサゴ"]

FISH_LIST = [STAR_1,STAR_2,STAR_3] #2次元配列であることに注意！
FISH_WEIGHT = [75,20,5] #★1～3の排出率
print(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0])
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
['アジ', 'サバ', 'イワシ']
```

</br>

リストが出力されているので、さらにこれを`random.choice()`で選択すれば良いですね。

```python{.numberLines caption="randomfish.py"}
import random

STAR_1 = ["アジ","サバ","イワシ"]
STAR_2 = ["カワハギ","タチウオ","メバル"]
STAR_3 = ["タイ","スズキ","カサゴ"]

FISH_LIST = [STAR_1,STAR_2,STAR_3] #2次元配列であることに注意！
FISH_WEIGHT = [75,20,5] #★1～3の排出率

print(random.choice(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0]))
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
サバ
```

</br>


**うまくいきました！これは釣りゲームの部品になるので、後で再利用できるように適当な名前を付けて保存しておきましょう。**
これはよくない例と比較して格段に修正、改造しやすくなっています。次のChallengeで確認してください。

---
- **Challenge2-1**　上のプログラムを改造して、★2に「コイ」を追加しましょう。
- **Challenge2-2**　**★4**の魚を追加してみましょう。排出率も適当に調節してください。

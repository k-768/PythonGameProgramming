---
var:
  header-title: "Pythonで釣りゲームを作ろう 基礎編11　辞書型"
  header-date: "最終更新日：2024年11月15日（金）"
---

# 基礎編11　辞書型 

## もくじ

-  [辞書型とは](basic11.html#辞書型とは) 
-  [2次元リスト](basic05.html#2次元リスト) 

## 辞書型とは

複数のデータを扱う方法として[第6回](basic06.html)ではリストを学びました。リストでは**複数のデータを順序付けて**扱います。

一方で、今回学ぶ辞書型は**キーとバリューのペア**で扱います。
以下のプログラムでは、`name`や`aveWeight`、`price`が**キー**、`タイ`や`5.4`、`20`がそれらに対応する**バリュー**です。

```python{.numberLines}
fish = {
"name":"タイ",
"aveWeight":5.4,
"price":20
}
```
<br>


辞書型では、**キーとバリューをコロンで区切って**ペアを作り、それぞれの**ペアをカンマで区切って**記述します。

---

データを取り出すには**キー**を用います。

<br>

```python{.numberLines}
fish = {
"name":"タイ",
"aveWeight":5.4,
"price":20
}

print(fish["name"])
print(fish["aveWeight"])
print(fish["price"])
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
タイ
5.4
20
```

<br>

---

RPGを想定して、次の課題に挑戦してください。

- **Challenge11-1**　

プレイヤーのステータスを作ってみましょう。`job`(職業)、`HP`、`MP`、`ATK`(攻撃力)、`DEF`(防御力)のデータを持つ辞書型`player`を作成して下さい。
値は自由に設定してください。

<br>

- **Challenge11-2**　

プレイヤーのHPを出力してください。

<br>

- **Challenge11-3**　

プレイヤーのHP20減らすプログラムを作成してください。HPを出力して減っていることを確認してください。

<br><br><br><br>


**<i class="fa-solid fa-check"></i>解答例**


```python{.numberLines caption="Challenge11"}
# 11-1 解答
player = {
"job":"剣士",
"HP":100,
"MP":30,
"ATK":20,
"DEF":10
}

# 11-2 解答
print(player["HP"])


# 11-3 解答
player["HP"] -= 20
print(player["HP"])
```

<br>


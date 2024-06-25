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

```python{.numberLines　caption="i文の構造"}
if a > 0:
  print(a + "は正の値です")
```

## 関係演算子



リストは、**変数をセットで管理できる便利なもの**です。
例えば、以下のようにキャラクターの持ち物を表すことを考えましょう。
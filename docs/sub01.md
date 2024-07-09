---
var:
  header-title: "Pythonで釣りゲームを作ろう キーボード操作"
  header-date: "2024年04月23日（月)"
---

# 基礎編2　Tkinter2 キーボード操作 

## もくじ

-  [キーボードの入力を判定する](basic02.html#キーボードの入力を判定する) 

</br>

## キーボードの入力を判定する

Tkinterでは、キーボードの入力を判定することができます。以下の**プログラムを実行し、適当なキーボードを押してみてください**。

</br>

```python{.numberLines caption="move-0.py"}
import tkinter as tk
import os

# ディレクトリ
cwd = os.getcwd()

# ウィンドウ設置
root = tk.Tk()
root.title("move-0")
root.geometry("600x300")

# キャンバス設置
canvas = tk.Canvas(root,width = 600,height = 300,bg = "skyblue")
canvas.pack()

# 四角形を配置
canvas.create_rectangle(10,10,60,60,fill="blue",tag="rect")

# 押されたキーを出力する
def on_key_press(event):
    print(f"Key pressed: {event.keysym}")
    
# キーが押されたときにon_key_pressを実行する
root.bind("<KeyPress>", on_key_press)
# メインループ
root.mainloop()
```

**<i class="fa-solid fa-terminal"></i> 実行結果**

```
Key pressed: Right
Key pressed: Left
Key pressed: s
Key pressed: s
Key pressed: d
Key pressed: d
Key pressed: d
```

`20行目`から`24行目`に注目してください。

```python{.numberLines startFrom="19" caption="move-0.py(抜粋)"}
# 押されたキーを出力する
def on_key_press(event):
    print(f"Key pressed: {event.keysym}")
    
# キーが押されたときにon_key_pressを実行する
root.bind("<KeyPress>", on_key_press)
```

`20行目`では、**キーボードが押されたときに実行される関数**を設定しています。今回は、print文で押されたキーを出力します。

`24行目`では、**キーボードが押されたとき先ほどの関数が実行されるように**設定しています。bindメゾットによるトリガーを使えば、今回のようにキーを押したときだけでなく、キーを離したとき、マウスを動かしたときなど、様々なことを検出できます。[この記事](https://denno-sekai.com/tkinter-bind/)に詳しく説明があります。

</br>

## if文を使って上下左右を判定する

先ほどのプログラムに手を加えて、移動方向を判定するプログラムを作成してみましょう。
WASDキーに対応して、以下のような出力を出せたら完成です。

```
→
→
↓
↓
↓
↓
←
```
関数`on_key_press`の**中身だけを改造して**作成できます。以下のヒントをもとに自分で考えて、書いてみてください。
新しいファイル`move-1.py`を作成して、そこに`move-0.py`の中身をコピーしてから作業してください。

```python{.numberLines startFrom="19" caption="ヒント"}
# 押されたキーを出力する
def on_key_press(event):
    key = event.keysym # 変数keyに「w」や「a」など、押したキーの名前が格納される
    if(key == "w"): # 「w」が押されたとき
        print("↑")
    elif(...   #以下省略
```
---

完成したら、以下の答えと照らし合わせて確認してください。

---

**<i class="fa-solid fa-terminal"></i> 答え**

```python{.numberLines caption="move-1.py"}
import tkinter as tk
import os

# ディレクトリ
cwd = os.getcwd()

# ウィンドウ設置
root = tk.Tk()
root.title("move-1")
root.geometry("600x300")

# キャンバス設置
canvas = tk.Canvas(root,width = 600,height = 300,bg = "skyblue")
canvas.pack()

# 四角形を配置
canvas.create_rectangle(10,10,60,60,fill="blue",tag="rect")

def on_key_press(event):
    key = event.keysym # 変数keyに「w」や「a」など、押したキーの名前が格納される
    if(key == "w"):
        print("↑")
    elif(key == "a"):
        print("←")
    elif(key == "s"):
        print("↓")
    elif(key == "d"):
        print("→")

# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
```

- **ChallengeX-1**　wasdだけでなく、矢印キーにも対応させてみましょう。

ヒント:<span class="masked">`key == "A" or key == "B"`を使えば、「`key`が`A`または`B`のとき」という条件になります。</span>

---

**<i class="fa-solid fa-check"></i>解答例**

<br><br><br><br>

```python{.numberLines startFrom="19" caption="解答"}
# 押されたキーを出力する
def on_key_press(event):
    key = event.keysym # 変数keyに「w」や「a」など、押したキーの名前が格納される
    if(key == "w" or key == "Up"):
        print("↑")
    elif(key == "a" or key == "Left"):
        print("←")
    elif(key == "s" or key == "Down"):
        print("↓")
    elif(key == "d" or key == "Right"):
        print("→")
```
<br>

---

</br>

## 判定をもとに図形を移動させる

図形を一度消して、少し移動させ再描写することで、動いているように見せることができます。

![img](figs/sub/move-rect.png)

```python{.numberLines caption="move-rect.py"}
import tkinter as tk
import os

# ディレクトリ
cwd = os.getcwd()

# ウィンドウ設置
root = tk.Tk()
root.title("move-rect")
root.geometry("600x300")

# キャンバス設置
canvas = tk.Canvas(root,width = 600,height = 300,bg = "skyblue")
canvas.pack()

# 四角形を配置
canvas.create_rectangle(10,10,60,60,fill="blue",tag="rect")

def on_key_press(event):
    global x,y
    key = event.keysym # 変数keyに「w」や「a」など、押したキーの名前が格納される
    if(key == "w" or key == "Up"):
        print("↑")
        y = y - 5
    elif(key == "a" or key == "Left"):
        x = x - 5
    elif(key == "s" or key == "Down"):
        print("↓")
        y = y + 5
    elif(key == "d" or key == "Right"):
        print("→")
        x = x + 5
    
    canvas.delete("rect")
    canvas.create_rectangle(x,y,x + 50,y + 50,fill="blue",tag="rect")

# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
```
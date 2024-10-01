import tkinter as tk
import os
import copy

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
x = 10
y = 10
canvas.create_rectangle(x,y,x+50,y+50,fill="blue",tag="rect")

#ゲームの基本となる1ティック時間(ms)
TICK_TIME = 50

#>>キー監視>>
currentKey = []#現在押されているキー
key = []       #前回の処理から押されたキー
prevKey = [] #前回の処理までに押されたキー

def gameLoop():
    global key,x,y
    lastKey = len(key) - 1 #最後に押されたキーの配列番号
    speed = 1
    
    if(len(key)): #SHIFT以外の何かのキーが押されているとき
        if(key[lastKey]==40 or key[lastKey]==83):#下入力
            charaD = 0
            y = y + 5
            print("↓")
        elif(key[lastKey]==37 or key[lastKey]==65):#左入力
            charaD = 1
            x = x-5
            print("←")
        elif(key[lastKey]==39 or key[lastKey]==68):#右入力
            charaD = 2
            x = x + 5
            print("→")
        elif(key[lastKey]==38 or key[lastKey]==87):#上入力
            charaD = 3
            y = y -5
            print("↑")
    
    canvas.delete("rect")
    canvas.create_rectangle(x,y,x+50,y+50,fill="blue",tag="rect")
    prevKey = copy.deepcopy(key)
    key = copy.deepcopy(currentKey)
    root.after(round(TICK_TIME/speed),gameLoop)


#何かのキーが押されたときに呼び出される関数
def press(e):
    keycode = e.keycode
    if(not currentKey.count(keycode)):#始めて押されたならば
        currentKey.append(keycode)
        print(f"pressed:{e.keysym}")
    if(not key.count(keycode)):#前回の処理から始めて押されたならば
        key.append(keycode)

#何かのキーが離されたときに呼び出される関数
def release(e):
    keycode = e.keycode
    currentKey.remove(keycode)
    print(f"released:{e.keysym}")

#キー入力をトリガーに関数を呼び出すよう設定する
root.bind("<KeyPress>", press)
root.bind("<KeyRelease>", release)

gameLoop()
# メインループ
root.mainloop()
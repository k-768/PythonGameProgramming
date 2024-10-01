import tkinter as tk

# ウィンドウ設置　#? Tkinterの基礎(これで学ぶ)
root = tk.Tk()
root.title("move-0")
root.geometry("600x300")

# キャンバス設置
canvas_x = 600 #? 変数 ... OK
canvas_y = 300
canvas = tk.Canvas(root,width = canvas_x,height = canvas_y,bg = "yellowGreen")
canvas.pack()

# 四角形を配置
x = 100
y = 100

size_x = 50
size_y = 50
canvas.create_rectangle(x,y,x+size_x,y+size_y,fill="blue",tag="rect") #? 四則演算 ... OK(変数回)


def press(e): #? 関数の定義と実行
    global x,y,size_x,size_y
    key = e.keysym
    dx = 0
    dy = 0
    if(key == "w" or key == "Up"): #? 条件分岐，論理演算子
        dx = 0
        dy = -10
    elif(key == "a"  or key == "Left"):
        dx = -10
        dy = 0
    elif(key == "s" or key == "Down"):
        dx = 0
        dy = 10
    elif(key == "d" or key == "Right"):
        dx = 10
        dy = 0
    
    if(0 <= x+dx <= canvas_x - size_x and 0 <= y+dy  <= canvas_y - size_y ):
        x = x + dx
        y = y + dy
        canvas.delete("rect")
        canvas.create_rectangle(x,y,x+size_x,y+size_y,fill="blue",tag="rect")

#キー入力をトリガーに関数を呼び出すよう設定する
root.bind("<KeyPress>", press)#? キー入力監視(これで学ぶ)

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")
    
# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
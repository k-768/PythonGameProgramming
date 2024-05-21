import tkinter as tk

# ウィンドウ設置　#? Tkinterの基礎(これで学ぶ)
root = tk.Tk()
root.title("tkinter test")
root.geometry("1600x800")

# キャンバス設置
canvas_x = 1600 #? 変数 ... OK
canvas_y = 800
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
    if(size_x/2 <= e.x <= canvas_x - size_x/2 and size_y/2 <= e.y  <= canvas_y - size_y/2 ):
        x = e.x - size_x/2
        y = e.y - size_y/2
        canvas.delete("rect")
        canvas.create_rectangle(x,y,x+size_x,y+size_y,fill="blue",tag="rect")

#キー入力をトリガーに関数を呼び出すよう設定する
root.bind("<Motion>", press)#? キー入力監視(これで学ぶ)

# メインループ
root.mainloop()
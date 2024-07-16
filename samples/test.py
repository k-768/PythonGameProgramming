import tkinter as tk
import os

# ディレクトリ
cwd = os.getcwd()

# ウィンドウ設置
root = tk.Tk()
root.title("tkinter test")
root.geometry("600x300")

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
    
# キャンバス設置
canvas = tk.Canvas(root,width = 600,height = 300,bg = "skyblue")
canvas.pack()

# 四角形を配置
x = 10
y = 10
canvas.create_rectangle(x,y,x+50,y+50,fill="blue",tag="rect")



# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
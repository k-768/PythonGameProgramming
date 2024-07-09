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
    if(key == "w" or key == "Up"):
        print("↑")
    elif(key == "a" or key == "Left"):
        print("←")
    elif(key == "s" or key == "Down"):
        print("↓")
    elif(key == "d" or key == "Right"):
        print("→")

# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
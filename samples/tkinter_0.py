import tkinter as tk
import os

# ディレクトリ
cwd = os.getcwd()

# ウィンドウ設置
root = tk.Tk()
root.title("tkinter test")
root.geometry("600x300")

# キャンバス設置
canvas = tk.Canvas(root,width = 200,height = 100,bg = "skyblue")
canvas.pack()

# 四角形を配置
canvas.create_rectangle(10,10,60,60,fill="blue",tag="rect")

# メインループ
root.mainloop()
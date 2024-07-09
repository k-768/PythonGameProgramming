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

def on_key_press(event):
    print(f"Key pressed: {event.keysym}")
    
# メインループ
root.bind("<KeyPress>", on_key_press)
root.mainloop()
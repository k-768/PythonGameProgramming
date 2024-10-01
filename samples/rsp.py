import os
import tkinter as tk


#>>ディレクトリ>>
cwd = os.getcwd()

#>>ウィンドウの設定>>
root = tk.Tk()
root.title("じゃんけん")
root.geometry("1200x800") 

#>>画像の読み込み>>
gu = tk.PhotoImage(file=cwd + "/figs/sub/gu.png")
choki = tk.PhotoImage(file=cwd + "/figs/sub/choki.png")
pa = tk.PhotoImage(file=cwd + "/figs/sub/pa.png")

def gameloop():
    s

gameloop()
root.mainloop()
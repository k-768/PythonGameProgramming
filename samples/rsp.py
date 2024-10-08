import os
import random
import tkinter as tk


#ディレクトリ
cwd = os.getcwd()

#---ウィンドウの設定---
root = tk.Tk()
root.title("じゃんけん")
root.geometry("800x800") 

#---キャンバスの設置---
canvas = tk.Canvas(root,width = 800,height = 800,bg = "skyblue")
canvas.pack()


#---画像の読み込み---
print(cwd)
gu = tk.PhotoImage(file=cwd + "/samples/gu.png")
choki = tk.PhotoImage(file=cwd + "/samples/choki.png")
pa = tk.PhotoImage(file=cwd + "/samples/pa.png")
small_gu = gu.subsample(6, 6)
small_choki = choki.subsample(6, 6)
small_pa = pa.subsample(6, 6)

#---ボタンの設置---
gu_btn = tk.Button(root,image=small_gu)
gu_btn.place(x=50,y=500)
choki_btn = tk.Button(root,image=small_choki)
choki_btn.place(x=250,y=500)
pa_btn = tk.Button(root,image=small_pa)
pa_btn.place(x=450,y=500)


def gameloop():
    canvas.create_image(50,0,image =small_gu ,tag="chara",anchor=tk.NW)

gameloop()
root.mainloop()
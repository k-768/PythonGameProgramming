import copy
import os
import random
import tkinter as tk


#>>ディレクトリ>>
cwd = os.getcwd()


#>>マップ設定>>
MAP_SIZE_X = 384  #マップ画像のxピクセル数
MAP_SIZE_Y = 384  #マップ画像のyピクセル数

MAGNIFICATION_RATE = 2 # 拡大率


#>>ウィンドウ、キャンバス>>
CANVAS_WIDTH = MAP_SIZE_X * MAGNIFICATION_RATE #キャンバス幅
CANVAS_HEIGHT = MAP_SIZE_Y * MAGNIFICATION_RATE #キャンバス高さ
MARGINE_X = 2 #マージン
MARGINE_Y = 2 #マージン
CANVAS_SIZE = f"{CANVAS_WIDTH+MARGINE_X}x{CANVAS_HEIGHT+MARGINE_Y}"#キャンバスサイズ

#ウィンドウ設置
root = tk.Tk()
root.title("game01")
root.geometry(CANVAS_SIZE)

#キャンバス設置
canvas = tk.Canvas(root,width = CANVAS_WIDTH,height = CANVAS_HEIGHT,bg = "skyblue")
canvas.pack()



#マップ画像
MAP_IMAGE = tk.PhotoImage(file = cwd+"/img/fishing_map.png")
MAP_BIG_IMAGE = MAP_IMAGE.zoom(MAGNIFICATION_RATE,MAGNIFICATION_RATE)

#ゲームの基本となる1ティック時間(ms)
TICK_TIME = 50  

#>>魚>>
fishFlag = False #釣り可能かどうか

LOW_RARE_FISH = [
        {
        "name":"イワシ",
        "aveWeight":0.12, #平均重量
        "price":60 #kg単価
        },
        {
        "name":"アジ",
        "aveWeight":0.17,
        "price":100
        },
        {
        "name":"サバ",
        "aveWeight":0.35,
        "price":50
        },
    ]
MIDDLE_RARE_FISH = [
        {
        "name":"タチウオ",
        "aveWeight":3,
        "price":12
        },
        {
        "name":"カワハギ",
        "aveWeight":0.4,
        "price":80
        },
        {
        "name":"メバル",
        "aveWeight":0.43,
        "price":100
        },
    ]
HIGH_RARE_FISH = [
        {
        "name":"タイ",
        "aveWeight":5.4,
        "price":20
        },
        {
        "name":"スズキ",
        "aveWeight":5.5,
        "price":19
        },
        {
        "name":"サケ",
        "aveWeight":1.65,
        "price":65
        },
    ]

FISH_LIST = []
FISH_LIST.append(LOW_RARE_FISH)
FISH_LIST.append(MIDDLE_RARE_FISH)
FISH_LIST.append(HIGH_RARE_FISH)

FISH_WEIGHT = [75,20,5] #排出率


# >>釣り結果表示>>
def showResult(fish,rank,weight,price):
    if rank == "silver":
        name = "大物の"+fish
    elif rank == "gold":
        name = "超大物の"+fish
    else:
        name = fish
    
    print(str(weight)+"kgの"+name+"を釣り上げた!")
    print(str(price)+"Gで売れそうだ!")



#>>ゲームのメインループ関数>>
def gameLoop():
    global key,currentKey,prevKey
    
    if ("space" in key) and ("space" not in prevKey):
        selectedFish = random.choice((random.choices(FISH_LIST,k=1,weights = FISH_WEIGHT))[0])
        #魚の重さを決定(ランダム 平均の0.5~1.5倍)
        fishWeight = selectedFish["aveWeight"]*random.uniform(0.5, 1.5)
        fishWeight = round(fishWeight,2) #少数第3位で四捨五入
        #重さから売却価格を決定
        fishPrice = fishWeight * selectedFish["price"]
        
        #魚のランクを決定、ランクに応じて価格を上方修正
        if fishWeight > selectedFish["aveWeight"]*1.4:
            fishRank = "gold"
            fishPrice *= 1.4
        elif fishWeight > selectedFish["aveWeight"]*1.2:
            fishRank = "silver"
            fishPrice *= 1.2
        else:
            fishRank = "bronze"
        
        fishPrice = round(fishPrice) #四捨五入
        
        
        showResult(selectedFish["name"],fishRank,fishWeight,fishPrice)
    
    prevKey = copy.deepcopy(key)
    key = copy.deepcopy(currentKey)
    root.after(TICK_TIME,gameLoop)

#>>キー監視>>
currentKey = []#現在押されているキー
key = []       #前回の処理から押されたキー
prevKey = [] #前回の処理までに押されたキー

#何かのキーが押されたときに呼び出される関数
def press(e):
    keysym = e.keysym
    if keysym not in currentKey:#始めて押されたならば
        currentKey.append(keysym)
        print(f"pressed:{keysym}")
    if keysym not in key:#前回の処理から始めて押されたならば
        key.append(keysym)

#何かのキーが離されたときに呼び出される関数
def release(e):
    keysym = e.keysym
    currentKey.remove(keysym)
    print(f"released:{keysym}")

#キー入力をトリガーに関数を呼び出すよう設定する
root.bind("<KeyPress>", press)
root.bind("<KeyRelease>", release)

#>>メインループ>>>
canvas.create_image(0,0,image = MAP_BIG_IMAGE ,tag="bgimage",anchor=tk.NW)

gameLoop()
print("start!")
root.mainloop()
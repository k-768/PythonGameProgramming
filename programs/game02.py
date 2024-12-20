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
root.title("game02")
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

FISH_IMAGE = {
    "イワシ":tk.PhotoImage(file = cwd+"/img/iwashi.png"),
    "アジ":tk.PhotoImage(file = cwd+"/img/aji.png"),
    "サバ":tk.PhotoImage(file = cwd+"/img/saba.png"),
    "タチウオ":tk.PhotoImage(file = cwd+"/img/tachiuo.png"),
    "カワハギ":tk.PhotoImage(file = cwd+"/img/kawahagi.png"),
    "メバル":tk.PhotoImage(file = cwd+"/img/mebaru.png"),
    "タイ":tk.PhotoImage(file = cwd+"/img/iwashi.png"),
    "スズキ":tk.PhotoImage(file = cwd+"/img/iwashi.png"),
    "サケ":tk.PhotoImage(file = cwd+"/img/sake.png"),
}
BIG_FISH_IMAGE = {key :img.zoom(2,2) for key , img in FISH_IMAGE.items()}

LOW_RARE_FISH = [
        {
        "name":"イワシ",
        "img":FISH_IMAGE["イワシ"],
        "aveWeight":0.12, #平均重量
        "price":60 #kg単価
        },
        {
        "name":"アジ",
        "img":FISH_IMAGE["アジ"],
        "aveWeight":0.17,
        "price":100
        },
        {
        "name":"サバ",
        "img":FISH_IMAGE["サバ"],
        "aveWeight":0.35,
        "price":50
        },
    ]
MIDDLE_RARE_FISH = [
        {
        "name":"タチウオ",
        "img":FISH_IMAGE["タチウオ"],
        "aveWeight":3,
        "price":12
        },
        {
        "name":"カワハギ",
        "img":FISH_IMAGE["カワハギ"],
        "aveWeight":0.4,
        "price":80
        },
        {
        "name":"メバル",
        "img":FISH_IMAGE["メバル"],
        "aveWeight":0.43,
        "price":100
        },
    ]
HIGH_RARE_FISH = [
        {
        "name":"タイ",
        "img":FISH_IMAGE["タイ"],
        "aveWeight":5.4,
        "price":20
        },
        {
        "name":"スズキ",
        "img":FISH_IMAGE["スズキ"],
        "aveWeight":5.5,
        "price":19
        },
        {
        "name":"サケ",
        "img":FISH_IMAGE["サケ"],
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
RESULT_X = 300
RESULT_Y = 200
RESULT_SIZE = f"{RESULT_X}x{RESULT_Y}+{int((CANVAS_WIDTH - RESULT_X)/2)}+{int((CANVAS_HEIGHT - RESULT_Y)/2)}"


def showResultWindow(fish,rank,weight,price):
    global resultWindow,FISH_IMAGE
    #ウィンドウ設置
    resultWindow = tk.Toplevel()
    resultWindow.title("Result")
    resultWindow.geometry(RESULT_SIZE)
    resultWindow.resizable(False,False)
    resultWindow.configure(bg="burlywood")
    
    
    # フレームの作成と設置
    nameFrame = tk.Frame(resultWindow , relief=tk.RAISED , bg="burlywood")
    canvasFrame = tk.Frame(resultWindow , relief=tk.RAISED , bg="burlywood")
    infoFrame = tk.Frame(resultWindow , relief=tk.RAISED , bg="burlywood")
    nameFrame.pack(fill = tk.BOTH, pady=10)
    canvasFrame.pack(fill = tk.BOTH, pady=0)
    infoFrame.pack(fill = tk.BOTH, pady=10)
    
    if rank == "silver":
        name = "大物の"+fish
        color = "LightBlue4"
    elif rank == "gold":
        name = "超大物の"+fish
        color = "gold"
    else:
        name = fish
        color = "DarkOrange4"
    
    viewCanvas = tk.Canvas(canvasFrame,width = 96,height = 48,bg = "burlywood",highlightthickness=0)
    viewCanvas.pack()
    viewCanvas.create_image(48,24,image =BIG_FISH_IMAGE[fish],tag="view",anchor=tk.CENTER)
    
    # 各種ウィジェットの作成
    fishName = tk.Label(nameFrame, text=name, font=("MSゴシック", "20", "bold"),fg = color,bg = "burlywood")
    fishWeight = tk.Label(infoFrame, text=str(weight)+" kg", font=("MSゴシック", "16"),bg = "burlywood")
    fishPrice = tk.Label(infoFrame, text=str(price)+" G", font=("MSゴシック", "16"),bg = "burlywood")
    fishName.pack()
    fishWeight.pack()
    fishPrice.pack()



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
        
        
        showResultWindow(selectedFish["name"],fishRank,fishWeight,fishPrice)
    
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
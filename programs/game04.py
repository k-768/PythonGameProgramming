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
root.title("game04")
root.geometry(CANVAS_SIZE)

#キャンバス設置
canvas = tk.Canvas(root,width = CANVAS_WIDTH,height = CANVAS_HEIGHT,bg = "skyblue")
canvas.pack()



#マップ画像
MAP_IMAGE = tk.PhotoImage(file = cwd+"/img/fishing_map.png")
MAP_BIG_IMAGE = MAP_IMAGE.zoom(MAGNIFICATION_RATE,MAGNIFICATION_RATE)

#>>キャラクター>>
CHARA_WIDTH = 64  #キャラの幅
CHARA_HEIGHT = 96 #キャラの高さ

#キャラクターの座標
charaX = 160 * MAGNIFICATION_RATE 
charaY = 128 * MAGNIFICATION_RATE
flag = "default"
'''
default:通常状態
wait:釣り中
hit:ウキが沈む
success:釣り成功
result:釣り結果表示
'''
fishingCount = 0
waitTick = 0

#キャラクターの画像
CHARA_IMAGE = {
    "default":tk.PhotoImage(file = cwd+"/img/character_A.png"),
    "wait":tk.PhotoImage(file = cwd+"/img/character_B.png"),
    "bite":tk.PhotoImage(file = cwd+"/img/character_C.png"),
    "hit":tk.PhotoImage(file = cwd+"/img/character_D1.png"),
    "fight":tk.PhotoImage(file = cwd+"/img/character_D2.png"),
}

BIG_CHARA_IMAGE = {key :img.zoom(MAGNIFICATION_RATE,MAGNIFICATION_RATE) for key , img in CHARA_IMAGE.items()}


#キャラクターを再描写する関数  
def setChara(x,y,state):
    """
    x:キャラのX座標
    y:キャラのY座標
    state:キャラの状態
    """
    #今の画像を消して再描写
    canvas.delete("chara")
    canvas.create_image(x,y,image =BIG_CHARA_IMAGE[state] ,tag="chara",anchor=tk.NW)


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
    
    if(rank == "silver"):
        name = "大物の"+fish
        color = "LightBlue4"
    elif(rank == "gold"):
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
    global charaX,charaY,flag,key,currentKey,prevKey,waitTick,fishingCount,resultWindow
    
    if (flag == "default"): #待機中のとき 
        setChara(charaX,charaY,"default")
        if(("space" in key) and ("space" not in prevKey)):
            canvas.delete("icon")#釣りアイコン削除
            flag = "wait" #魚釣り中に遷移
            waitTick = random.randint(round(3000/TICK_TIME),round(7000/TICK_TIME))#3-7秒
            fishingCount = 0 #待ち時間をランダムに決定
    
    elif (flag == "wait"):#魚釣り中のとき
        if(fishingCount == 0):#初回なら
            #キャラクター再描写
            setChara(charaX,charaY,"wait")
        elif(fishingCount >= waitTick):#待ち時間を終えたとき
            flag = "hit" #「ウキ沈む」に遷移
            waitTick = 10
            fishingCount = 0
        
        if (flag == "wait"):
            fishingCount += 1 #待機カウンタを増やす
    
    elif (flag == "hit"): #魚がかかったとき
        if(("space" in key) and ("space" not in prevKey)):  #スペースキー押下されたとき
            flag = "success"
            fishingCount = 0
        elif(fishingCount == 0):#初回なら
            #キャラクター再描写
            setChara(charaX,charaY,"fight")
            print("ビク！")
        
        if (flag == "hit"):
            fishingCount += 1
    
    elif(flag == "success"): #釣りに成功したとき
        #ランダムな魚を選択
        selectedFish = random.choice((random.choices(FISH_LIST,k=1,weights = (75,20,5)))[0])
        print(selectedFish["name"])
        #魚の重さを決定(ランダム 0.5~1.5)
        fishWeight = selectedFish["aveWeight"]*random.uniform(0.5, 1.5)
        fishWeight = round(fishWeight,2) #少数第3位で四捨五入
        print(fishWeight)
        #重さから売却価格を決定
        fishPrice = fishWeight * selectedFish["price"]
        
        #魚のランクを決定、ランクに応じて価格を上方修正
        if(fishWeight > selectedFish["aveWeight"]*1.4):
            fishRank = "gold"
            fishPrice *= 1.4
        elif (fishWeight > selectedFish["aveWeight"]*1.2):
            fishRank = "silver"
            fishPrice *= 1.2
        else:
            fishRank = "bronze"
        
        fishPrice = round(fishPrice) #四捨五入
        
        #釣りの姿勢から通常状態に戻す
        setChara(charaX,charaY,"default")
        canvas.delete("rod")
        showResultWindow(selectedFish["name"],fishRank,fishWeight,fishPrice)
        flag = "result"
        
    elif(flag == "result"): #結果表示中のとき
        if(("space" in key) and ("space" not in prevKey)):  #スペースキー押下されたとき
            flag = "default"
            resultWindow.destroy()
    
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
    if(keysym not in currentKey):#始めて押されたならば
        currentKey.append(keysym)
        print(f"pressed:{keysym}")
    if(keysym not in key):#前回の処理から始めて押されたならば
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
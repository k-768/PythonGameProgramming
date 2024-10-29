import random
import sys
n = 36

player = 1
cpu = 1
w = "*"
count = 0

while True:
    print("-------------------------")
    dummy = input("Enterでさいころをふる")
    p = random.randint(1,6)
    if(player < cpu):
        p = random.randint(3,6)
    print("さいころの目は"+str(p)+"だ")
    player = player + p
    if(player == cpu):
        player = player - p
        print("同じマス目には進めない！")
    elif(player >= n):
        print("ゴール")
        print("あなたの勝ち")
        sys.exit()
    
    if(player > cpu):
        print(w*(cpu-1)+"C"+w*(player-cpu-1)+"P"+w*(n-player))
    else:
        print(w*(player-1)+"P"+w*(cpu-player-1)+"C"+w*(n-cpu))
    
    print("CPUがさいころをふった")
    p = random.randint(1,6)
    if(player > cpu):
        p = random.randint(3,6)
    print("さいころの目は"+str(p)+"だ")
    cpu = cpu + p
    if(player == cpu):
        cpu = cpu - p
        print("同じマス目には進めない！")
    elif(cpu >= n):
        print("ゴール")
        print("あなたの負け")
        sys.exit()
    
    if(player > cpu):
        print(w*(cpu-1)+"C"+w*(player-cpu-1)+"P"+w*(n-player))
    else:
        print(w*(player-1)+"P"+w*(cpu-player-1)+"C"+w*(n-cpu))
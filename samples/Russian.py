import random
import sys

player_life = 2
cpu_life = 3

arr = [1,1,1,1,0,0,0,0,0,0]

def shot(target,damage = 1):
    global player_life,cpu_life
    if (target == "p"):
        player_life -= damage
        return(player_life)
    else:
        cpu_life -= damage
        return(cpu_life)


print("GAME START")
print("YOUR LIFE:"+("♡"*player_life)+" , DEALER'S LIFE:"+("♡"*cpu_life))
print("実弾:"+str(arr.count(1))+" , 空弾:"+str(arr.count(0)))

random.shuffle(arr)


n = 0
for i,b in enumerate(arr):
    if(not (i+n)%2):
        print("---YOUR TURN---")
        dummy = input("shot? [Y/N]")
        if (dummy == "y" or dummy == "Y"):
            if(b):
                print("YOU SHOT DEALER")
                print("YOUR LIFE:"+("♡"*player_life)+" , DEALER'S LIFE:"+("♡"*(cpu_life-1)))
                if(not shot("c")):
                    print("YOU ARE WINNER")
                    sys.exit()
            else:
                print("MISS")
        else:
            if(b):
                print("YOU SHOT YOURSELF")
                print("YOUR LIFE:"+("♡"*(player_life-1))+" , DEALER'S LIFE:"+("♡"*cpu_life))
                if(not shot("p")):
                    print("YOU ARE LOSER")
                    sys.exit()
            else:
                print("SAFE")
                n += 1
    else:
        print("---DEALER'S TURN---")
        s = random.randint(0,1)
        if(i == len(arr)-1 or i > arr.count(0)):
            s = 0
        if (s):
            print("DEALER PULLS TRIGER TOWARDS HIMSELF...")
            if(b):
                print("DEALER SHOTS HIMSELF")
                print("YOUR LIFE:"+("♡"*player_life)+" , DEALER'S LIFE:"+("♡"*(cpu_life-1)))
                if(not shot("c")):
                    print("YOU ARE WINNER")
                    sys.exit()
            else:
                print("SAFE")
                n += 1
        else:
            print("DEALER PULLS TRIGER TOWARDS YOU")
            if(b):
                print("DEALER SHOT YOU")
                print("YOUR LIFE:"+("♡"*(player_life-1))+" , DEALER'S LIFE:"+("♡"*cpu_life))
                if(not shot("p")):
                    print("YOU ARE LOSER")
                    sys.exit()
            else:
                print("MISS")



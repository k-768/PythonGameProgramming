import random

hands = ["グー","チョキ","パー"]
result = "あいこ"
print("最初はグー")

while (result == "あいこ"):
    my_hands = input("何を出す？  グー/チョキ/パー：")
    
    while(my_hands not in hands):#while(my_hands!="グー" and my_hands!="チョキ" and my_hands!="パー"):
        print("不正な入力です")
        my_hands = input("何を出す？  グー/チョキ/パー：")
    
    cpu_hands = random.choice(hands)
    print ("じゃんけんぽん！")
    print("あなた："+my_hands,"CPU:"+cpu_hands)
    
    if(my_hands == cpu_hands):
        result = "あいこ"
    elif(cpu_hands == hands[(hands.index(my_hands)+1)%3]):#elif((my_hands == "グー" and cpu_hands == "チョキ")or(my_hands == "チョキ" and cpu_hands == "パー")or(my_hands == "パー" and cpu_hands == "グー")):
        result = "あなたの勝ち"
    else:
        result = "CPUの勝ち"
    
    print(result)
import random

#サイコロ
print(random.randint(1,50)*2)

fishes = ["アジ","サバ","イワシ","タイ","サメ"]
fish_weights =[30,30,30,8,2] #アジ,サバ,イワシ30%、タイ8%、サメ2%
print(random.choices(fishes,k=1,weights = fish_weights)[0])
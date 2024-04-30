import random

#? 良い例

STAR_1 = ["アジ","サバ","イワシ"]
STAR_2 = ["カワハギ","タチウオ","メバル"]
STAR_3 = ["タイ","スズキ","カサゴ"]

FISH_LIST = [STAR_1,STAR_2,STAR_3] #2次元配列であることに注意！
FISH_WEIGHT = [75,20,5] #★1～3の排出率

print(random.choice(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0]))


#! 悪い例

FISH_LIST = ["アジ","サバ","イワシ","カワハギ","タチウオ","メバル","タイ","スズキ","カサゴ"]
FISH_WEIGHT = [25,25,25,20/3,20/3,20/3,5/3,5/3,5/3] #それぞれの排出率
print(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0])





#---
print(FISH_LIST)
print(random.choices(FISH_LIST,k=1,weights=FISH_WEIGHT)[0])
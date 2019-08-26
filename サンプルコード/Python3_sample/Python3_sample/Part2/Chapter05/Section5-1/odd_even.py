from random import randint
num = randint(0, 100) # 0〜100の乱数
# 奇数か偶数かを判定する
if num%2 :
     result = "奇数"
else:
     result = "偶数"
print(num, result)
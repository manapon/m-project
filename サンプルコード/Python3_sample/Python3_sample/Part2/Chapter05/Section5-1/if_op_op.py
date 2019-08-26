from random import randint
a = randint(0, 10) # 0〜10の乱数
# 判定
if 5 <= a <= 8   :
    print(a, "合格")
else:
    print(a, "不合格")

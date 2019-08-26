from random import randint

# サイコロを定義する
def dice() :
    num = randint(1, 6)
    return num

# 2個のサイコロを5回振った結果
for i in range(5) :
    dice1 = dice()    # 1個目のサイコロを振る
    dice2 = dice()    # 2個目のサイコロを振る
    sum = dice1 + dice2   # 2個のサイコロの目の合計
    print(f"{dice1}と{dice2}で合計{sum}")

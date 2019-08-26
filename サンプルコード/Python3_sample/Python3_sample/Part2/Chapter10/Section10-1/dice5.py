from random import randint

# 関数を定義する
def dice() :
    num = randint(1, 6)
    return num

# dice()を5回呼び出す
for i in range(5) :
    result =  dice()    # 1個目のサイコロを振る
    print(result)

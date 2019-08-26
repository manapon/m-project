from random import randint
# 値が見つかるまで無限ループする
while True :
    a = randint(1, 13)
    b = randint(1, 13)
    c = randint(1, 13)
    # 合計が21ならばブレイクする
    if (a+b+c) == 21:
        break  # ブレイクする
        
print(a, b, c)

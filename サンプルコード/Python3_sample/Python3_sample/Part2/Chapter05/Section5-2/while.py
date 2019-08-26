from random import randint
tickets = 5
point = 0
fmt = "{:>3}"  # 3桁右詰
# ticketsが正の間は繰り返す
while tickets>0 :
    v = randint(1, 20)
    print(fmt.format(v))
    point += v
    tickets -= 1 # チケットを１枚減らす
# 出力
print("-" * 3)
print(fmt.format(point))
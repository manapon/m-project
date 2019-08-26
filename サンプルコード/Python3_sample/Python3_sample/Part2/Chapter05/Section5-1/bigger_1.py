from random import randint
a = randint(0, 100) # 0〜100の乱数
b = randint(0, 100)
# 大きな方の値を代入する
if a>b :
    bigger = a
else :
    bigger = b
    
# 結果の出力
text = f"{a}と{b}では、{bigger}が大きい"
print(text)
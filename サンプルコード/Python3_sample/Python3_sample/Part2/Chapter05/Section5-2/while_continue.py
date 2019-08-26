from random import randint
numbers = []  # 空のリスト
# numbersの値が10個になるまで繰り返す
while len(numbers)<10 :
    n = randint(0, 100) # 0〜100の乱数
    if n in numbers :
        # nがnumbersに含まれていたらスキップする
        continue
    # numbersにnを追加する
    numbers.append(n)
    
print(numbers)

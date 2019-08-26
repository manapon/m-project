from random import randint
numbers = []  # 空のリスト
# numbersの値が10個になるまで繰り返す
while len(numbers)<10 :
    n = randint(-10, 90) # -10〜90の乱数
    if n<0 :
        # nがマイナスならブレイクする
        print("中断されました")
        break
    if n in numbers :
        # nがnumbersに含まれていたらスキップする
        continue
    # numbersにnを追加する
    numbers.append(n)
else:
    print(numbers)

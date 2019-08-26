numlist = [3, 4.2, 10, "x", 1, 9] # 文字列が含まれている
sum = 0
for num in numlist :
    # numが数値ではないときスキップする
    if not isinstance(num, (int, float)) :
        print(num, "数値ではありません。")
        continue  # スキップする
    sum += num
    print(num, "/", sum)


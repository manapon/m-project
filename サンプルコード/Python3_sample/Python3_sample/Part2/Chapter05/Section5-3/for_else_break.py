numlist = [3, 4.2, 10, "x", 1, 9] # 文字列が含まれている
sum = 0
for num in numlist :
    # numが数値ではないときは処理をブレイクする
    if not isinstance(num, (int, float)) :
        print(num, "数値ではない値が含まれていました。")
        break  # ブレイクする
    sum += num
else :
    # breakされなかったときは合計する
    print("合計", sum)


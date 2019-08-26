numlist = [3, 4.2, 10, 1, 9] # すべて数値
sum = 0
for num in numlist :
    # numが数値ではないときは処理をブレイクする
    if not isinstance(num, (int, float)) :
        print(num, "数値ではない値が含まれていました。")
        break    # ブレイクする
    sum += num
else :
    # breakされなかったときは合計した値を出力する
    print("合計", sum)


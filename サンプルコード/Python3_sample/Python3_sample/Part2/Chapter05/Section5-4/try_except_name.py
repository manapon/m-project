sum = 7600
while True :
    num =  input("何人ですか？（qで終了）")
    if num == "q":
        print("終了しました。")
        break
    # 例外を振り分けて例外処理を行う
    try :
        price = round(sum / int(num))
        if price < 0 :
            # マイナスの場合は無視
            continue
        print("１人当たりの金額", price)
    except ValueError :
        print("数値を入れてください。")
    except ZeroDivisionError :
        print("0以外の数値を入力してください。")


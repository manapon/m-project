def calc(num) :
    unit_price = 180    # 単価
    try :
        num = float(num)    # 数値に変換する
        return num * unit_price
    except :
        return None    # 変換がエラーになったらNoneを返す

# キーボードから引数を入力して試す
while True :
    num = input("個数を入れてください。（qで終了）")
    if num == "" : 
        continue
    elif num == "q" :
        break
        
    # calc()で計算する
    result = calc(num)
    print(result)
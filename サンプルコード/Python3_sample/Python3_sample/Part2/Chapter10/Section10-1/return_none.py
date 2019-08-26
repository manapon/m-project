def calc(num):
    unit_price = 180    # 単価
    if not num.isdigit() :    # 数字かどうかチェックする
        return None    # 数字ではないときは中断する
    price = int(num) * unit_price
    return price

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
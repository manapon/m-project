def calc(size, num = 6) :    # num には初期値がある
    unit_price = {"S": 120, "M":150, "L":180}
    price = unit_price[size] * num
    return (size, num, price)
    
# calc()を試す    
a = calc("S", 2)
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")

b = calc("M")    # 個数を省略（サイズは省略できない）
print(f"{b[0]}サイズ、{b[1]}個、{b[2]}円")
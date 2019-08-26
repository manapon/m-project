fruits = ["apple", "orange", "banana", "peach"] 
# 例外処理に組み込む
try :
    dessert = fruits.pop()
    print("デザートは" + dessert)
    print(fruits)
except :
    print("エラーになりました。")

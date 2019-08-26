def do(func) :
    func()    # 引数で受け取った関数を実行する
    
def thanks() :
    print("ありがとう")
    
def hi() :
    print("やあ！")
  
# do()を実行  
condition = 1
if condition== 1 :
    do(thanks)
else :
    do(hi)
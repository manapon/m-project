import sys
from datetime import datetime
file = "log.txt"

if len(sys.argv)<2 :
    sys.exit()    # プログラムを中断する

now = str(datetime.now())  # 現在の日時データ
memo = sys.argv[1]           # コマンドライン引数から受け取ったメモ
line = "-"*10    # 区切り線
with open(file, "a") as fileobj:    # 追記モードのファイルオブジェクト
    fileobj.write(now + "\n") 
    fileobj.write(memo + "\n") 
    fileobj.write(line + "\n")
    

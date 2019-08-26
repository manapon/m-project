import sys
if len(sys.argv)<2 :
    print("読み込むファイル名を指定してください。")
    sys.exit()    # プログラムを中断する

file  = sys.argv[1]
with open(file) as fileobj:            # ファイルオブジェクトを作る
    text = fileobj.read()              # ファイルを読み込む
    print(text)
    
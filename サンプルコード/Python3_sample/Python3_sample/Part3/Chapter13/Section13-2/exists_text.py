import os
from random import randint

#保存フォルダとファイルパス
folder = "./data/"
file = folder + "sample.txt"
# ファイルを保存する
def filewrite():
    if not os.path.exists(folder) :    # 保存フォルダがなければ作る
        os.makedirs(folder)    # フォルダを作る
    with open(file, "w", encoding="utf_8") as fileobj:
        num = randint(0, 100)
        fileobj.write(f"{num}が出ました。")
        print("ファイルを保存しました。")

# 既存のファイルの有無チェック
if os.path.exists(file) :    # 既存ファイルがある場合
     while True:
        answer = input("上書きしてもよいですが？（y / n）")
        if answer == "y" :
            filewrite()
            break
        elif answer == "n":
            break
else :
    filewrite()
    

file = "./data/tsuretsuregusa.txt"
target = "心"
with open(file, "r", encoding="utf_8") as fileobj:    # ファイルオブジェクトを作る
    while True:
        try :
            line = next(fileobj)    # イテレータから1行取り出す
            if line.find(target)>=0 :    # 文字を検索する
                print(f"「{target}」が見つかりました。")
                print(line, end = "")
                break
        except StopIteration:    # EOF
            print(f"「{target}」は見つかりませんでした。")
            break
            
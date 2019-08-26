id_list = ["a2345", "a1236", "b7656", "f0987"]
while True :
    id = input("idを入力してください（qで終了）：")
    if id == "q":
        print("終了しました。")
        break
# 例外処理に組み込んで検索する
    try :
        pos = id_list.index(id)
        print(str(pos+1) + "番目のメンバーです。")
    except :
        print("メンバーではありません。")


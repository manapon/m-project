file = "./data/fox.txt"
with open(file) as fileobj :
    text = fileobj.read()
    newtext = text.rstrip(".")        # 末尾のピリオドを削除しておく
    wordlist = newtext.split(" ")    # スペースで区切ってリストにする
    print(wordlist)
    
    

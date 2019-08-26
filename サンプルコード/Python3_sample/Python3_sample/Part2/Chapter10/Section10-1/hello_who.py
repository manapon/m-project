def hello(who) :
    if who :     # whoが空やNoneのときFalse
        msg = who + "さん。こんにちは！" 
        print(msg)
    else :
        print("こんにちは！")

# hello()を試す
hello("")
hello("岡崎")

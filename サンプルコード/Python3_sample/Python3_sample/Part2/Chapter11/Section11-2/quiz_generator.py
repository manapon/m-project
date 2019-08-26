def word_quiz(word) :
    hint = ""
    for letter in word :
        hint += letter    # 先に取り出した文字に連結していく
        yield hint    # ヒントを返す

# 出題する
ans = "Python"    # 正解
quiz = word_quiz(ans)    # ジェネレータを作る
while True : 
    try :
        hint = next(quiz)    # ヒントを取り出す
        print(hint) 
        word = input("この単語は？：")
        if ans.lower() == word.lower() :    # 大文字小文字を区別しないで比較
            point = len(ans) - len(hint)
            print( f"正解です！得点：{point}")
            break
        else :
            print("違います。")
    except :
        print("終了です。得点：0")
        break


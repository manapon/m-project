v = 2    # グローバル変数
def calc() :
    v_local = v * 10    # グローバル変数vを10倍にする
    ans = 3 * v_local
    print(ans)

# calc()を実行する
calc()

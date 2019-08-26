# randomモジュールのrandint関数を読み込む
from random import randint
a = randint(0, 100) # 0〜100の乱数
b = randint(0, 100) 
# 判定（３つの条件がTrueのとき合格）
if a >= 40 and b >= 40 and (a+b) >= 120 :
    result = "合格"
else:
    result = "不合格"
    
# 結果の出力
text = f"a {a}、b {b}、合計{a+b}：{result}"
print(text)

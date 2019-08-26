import numpy as np
sigma = 3.5  # 分散
mu = 65    # 平均
# 得点のデータ（乱数で作成する）
data = sigma * np.random.randn(200) + mu
msg = "得点は？：".format(max, min)
x = float(input(msg))  # 得点
t_score = 10*(x - data.mean())/data.std() + 50    # 偏差値
print("平均点：", round(data.mean(),1 ))
print("標準偏差：", round(data.std(), 1))   # 標準偏差
print("偏差値：", round(t_score, 1))

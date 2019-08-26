import matplotlib.pyplot as plt
import numpy as np
X, Y = np.random.rand(100), np.random.rand(100)    # ランダムな配列を作る
V = np.random.rand(100)    # 色の濃淡を決めるデータの配列
plt.scatter(X, Y, s = 200, c = V, cmap = "Blues", edgecolors = "b")    # グラフを描く
plt.colorbar()    # カラーバーを表示する
plt.grid(True)    # グリッド
plt.show()    # 表示する

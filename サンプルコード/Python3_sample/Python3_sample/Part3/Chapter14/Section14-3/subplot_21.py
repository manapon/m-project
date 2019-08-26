import matplotlib.pyplot as plt
X1, Y1 = range(0, 7), [61, 45, 27, 88, 47, 56, 61]
X2, Y2 = range(0, 7), [17, 39, 46, 40, 27, 35, 41]
labels = ["A", "B", "C", "D", "E", "F", "G"]
fig = plt.figure()    # 図を作る
# 2行1列の上
ax1 = fig.add_subplot(2, 1, 1, facecolor = "cyan")    # サブプロットを追加する
ax1.bar(X1, Y1, color = "b", tick_label = labels)    # グラフの描画
ax1.set_title("snake")    # グラフのタイトル
# 2行1列の下
ax2 = fig.add_subplot(2, 1, 2,  facecolor = "cyan")    # サブプロットを追加する
ax2.bar(X2, Y2, color = "g", tick_label = labels)    # グラフの描画
ax2.set_title("fish")    # グラフのタイトル
plt.tight_layout()    # 下の図のタイトルが重ならないようにする
plt.show()    # 図を表示する
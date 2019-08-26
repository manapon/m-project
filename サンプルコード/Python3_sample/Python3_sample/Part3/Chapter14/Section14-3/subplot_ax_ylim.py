import matplotlib.pyplot as plt
X1, Y1 = range(0, 5), [61, 45, 27, 88, 47]
X2, Y2 = range(0, 5), [17, 39, 46, 40, 27]
labels = ["A", "B", "C", "D", "E"]
fig= plt.figure()    # 図を作る
# 1行2列の左
ax1 = fig.add_subplot(1, 2, 1)    # サブプロットを追加する
ax1.bar(X1, Y1, color = "b", tick_label = labels)    # グラフの描画
ax1.set_title("dog")    # グラフのタイトル
ymin, ymax = plt.ylim()   # 現在のY軸のレンジを取得する
# 1行2列の右
ax2 = fig.add_subplot(1, 2, 2)    # サブプロットを追加する
ax2.bar(X2, Y2, color = "g", tick_label = labels)    # グラフの描画
ax2.set_title("cat")    # グラフのタイトル
plt.ylim(ymin, ymax)    # Y軸のレンジをax1と合わせる
plt.show()    # 図を表示する
colors = ["blue", "red", "yellow", "red", "green"]
print("削除前", colors)
target = "red"
# 削除する値が含まれている間は繰り返し削除する
while target in colors :
    colors.remove(target)
print("削除後", colors)
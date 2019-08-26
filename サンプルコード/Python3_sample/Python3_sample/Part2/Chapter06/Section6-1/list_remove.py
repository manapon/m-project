colors = ["blue", "red", "yellow", "red", "green"]
print("削除前", colors)
target = "yellow"
# 削除する値が含まれているならば削除する
if target in colors :
    colors.remove(target)
print("削除後", colors)
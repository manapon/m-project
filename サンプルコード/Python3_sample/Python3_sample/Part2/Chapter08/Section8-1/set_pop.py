color_set = set()
#color_set = {"blue", "yellow", "red"} 
if color_set :
    print(f"{color_set}から", end="")   # 改行しない
    item = color_set.pop()
    print(f"{item}を取り除きました。")
    print(color_set)
else :
    print("セットは空です。")


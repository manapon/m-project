def size(item) :
    sizelist = ["XS", "S", "M", "L"]    # この順に並び替える
    pos = sizelist.index(item)    # itemのインデックス番号を値として返す
    return pos

# 並び替えるリスト
data = ["S", "M", "XS", "L", "M", "M","XS",  "S", "M", "L", "M"]
data.sort(key = size)    # dataをサイズ順に並べる
print(data)
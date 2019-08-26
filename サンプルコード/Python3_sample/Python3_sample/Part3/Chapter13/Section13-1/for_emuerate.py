file = "./data/tsuretsuregusa.txt"
with open(file, "r", encoding="utf_8") as fileobj:
    for i, line in enumerate(fileobj):  # ファイルオブジェクトから1行ずつ取り出す
        print(f"{i}: {len(line)}文字、{line}", end = "")
    print()


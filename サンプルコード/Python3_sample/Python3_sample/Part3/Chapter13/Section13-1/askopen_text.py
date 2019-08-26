import tkinter as tk
import tkinter.filedialog as fd
# tkアプリウインドウを表示しない
root = tk.Tk()
root.withdraw()
# オープンダイアログを表示する
file = fd.askopenfilename(
   title = "ファイルを選んでください。",
   filetypes=[("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)
# ファイルが選択されたならば開く
if file:
    with open(file, "r", encoding="utf_8") as fileobj:    # ファイルを開く
        text = fileobj.read()    # ファイルを読み込む
        print(text)

# datetimeモジュール
from datetime import datetime
# Datalogクラス
class Datalog:
    # 初期化メソッド
    def __init__(self):
        self.loglist = []
        
    # インスタンスメソッド
    def log(self, data):
        now = datetime.now()  # 現在の日時データ
        item = (now, data)  # タプルを作る
        self.loglist.append(item)  # loglistリストに追加する
        
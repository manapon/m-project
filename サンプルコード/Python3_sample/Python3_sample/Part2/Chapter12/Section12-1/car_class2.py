# Carクラス
class Car :
    # 初期化メソッド
    def __init__(self, color = "white") :
        self.color = color    # 引数で受け取った値を代入
        self.mileage = 0    # 0からスタート
       
    # インスタンスメソッド
    def drive(self, km) :
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)
        
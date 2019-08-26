# Goodsクラス
class Goods :
    # 初期化メソッド
    def __init__(self, name, price):
        # 非公開の__dataインスタンス変数（辞書）
        self.__data = {"name":name, "price":price}
    
    # nameプロパティ（ゲッター）
    @property
    def name(self):
        return self.__data["name"]
    
    # nameプロパティ（セッター）
    @name.setter
    def name(self, value):
        self.__data["name"] = value
     
     # priceプロパティ（ゲッター）
    @property
    def price(self):
        price = self.__data["price"]
        price_str = f"{price:,}円"
        return price_str
# スーパークラス
class Greet():
    def hello(self):
        print("やあ！")
        
    def bye(self):
        print("さよなら")
      
# サブクラス  
class Greet2(Greet):
    # スーパークラスのメソッドをオーバーライドする
    def hello(self, name = None):
        if name :
            print(name + "さん、こんにちは！")
        else :
            super().hello()    # スーパークラスのhello()をそのまま使う
        


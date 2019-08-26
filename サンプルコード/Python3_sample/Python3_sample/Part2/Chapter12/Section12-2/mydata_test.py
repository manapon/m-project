# Datalogクラスが定義してあるモジュールをインポートする
from datalog import Datalog
# Datalogクラスを継承したMydataクラス
class Mydata(Datalog):
    def printlog(self):
        # スーパークラスのインスタンス変数の値を取り出す
        for date, data in self.loglist :
            print(date, data)

# Mydataクラスのインスタンスを作って試す
obj = Mydata()
obj.log("あいう")  # スーパークラスのインスタンスメソッドを実行
obj.log("abc")
obj.log(123)
obj.printlog()  # サブクラスのインスタンスメソッドを実行

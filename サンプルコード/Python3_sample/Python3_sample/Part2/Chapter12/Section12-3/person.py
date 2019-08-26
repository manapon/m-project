class Person():
    def __init__(self, name):
        self.__name = name    # 非公開のインスタンス変数
        
    def who(self):
        print(self.__name + "です。")
        

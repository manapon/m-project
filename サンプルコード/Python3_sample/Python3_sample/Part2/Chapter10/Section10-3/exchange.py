#円をドルに換算する
def yen2dollar(yen, rate, charge = 0) :
    dollar = yen / (rate + charge)
    return dollar
    
#ドルを円に換算する
def dollar2yen(dollar, rate, charge = 0) :
    yen = dollar * (rate - charge)
    return yen
def average(*args) :
    if args :     # argsが空でないときに実行する
        ave = sum(args)/len(args)
        return ave
    else :
        return None
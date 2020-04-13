from selenium import webdriver
import chromedriver_binary
import time
import numpy as np
import datetime
import psycopg2
import sys
import os
import glob
import openpyxl as px
import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
import random, re
import sklearn
sklearn.__version__

wlank   = '0'

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()

sql = 'select hiduke0 from "kabumst" WHERE "scode0" > %s ORDER BY "hiduke0" DESC'
cursor.execute(sql,('0000',));
enddate = cursor.fetchone()
yosdate = enddate
stdate = '20190901'

sql = 'select * from "kabumst3" WHERE "lank0" > %s and "hiduke0" >= %s and "hiduke0" <= %s ORDER BY "hiduke0" ASC'
cursor.execute(sql,(wlank,stdate,enddate,));
results = cursor.fetchall()

# データをシャッフル --- (※2)
random.shuffle(results)

total_len = len(results)
train_len = int(total_len * 2 / 3)

train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data  = results[i][4:]
    label = results[i][3]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

# データを学習し、予測する --- (※4)
#clf = SGDClassifier()
#clf = RandomForestClassifier()
#clf = LogisticRegression()
clf = svm.SVC()
#clf = KNeighborsClassifier()

clf.fit(train_data, train_label)
pre = clf.predict(test_data)

#alg0 = "SGDClassifier"
#alg0 = "RandomForestClassifier"
#alg0 = "LogisticRegression"
alg0 = "svm.SVC"
#alg0 = "KNeighborsClassifier"

# 正解率を求める --- (※5)
ac_score = metrics.accuracy_score(test_label, pre)
print("正解率=", ac_score)

sql = 'select * from "kabumst3" WHERE "hiduke0" = %s ORDER BY "hiduke0" ASC'
cursor.execute(sql,(yosdate,));
results2 = cursor.fetchall()

total_len2 = len(results2)

yosoku_data  = []
yosoku_label = []
for i2 in range(total_len2):
   data2  = results2[i2][4:]
   label2 = results2[i2][3]
   yosoku_data.append(data2)

yosoku_label = clf.predict(yosoku_data)

cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0

for i3 in range(total_len2):
   if yosoku_label[i3] == '6' :
     print('level6:', results2[i3][0])
   if yosoku_label[i3] > '2' :
     data1 = results2[i3]
     scode0    = data1[0]
     hiduke0   = data1[1]
     sname0    = data1[2]
     lank0     = yosoku_label[i3]
     zenne0    = data1[4]
     hajime0   = data1[5]
     takane0   = data1[6]
     yasune0   = data1[7]
     dekidaka0 = data1[8]
     baibai0   = data1[9]
     jikaso0   = data1[10]
     hakokab0  = data1[11]
     hairima0  = data1[12]
     hitohai0  = data1[13]
     per0      = data1[14]
     pbr0      = data1[15]
     eps0      = data1[16]
     bps0      = data1[17]
     tenki0    = data1[18]
     heikin0   = data1[19]
     filler01  = data1[20]
     filler02  = alg0
     ins = 'INSERT INTO kabuyosoku3 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
     try:
       cursor.execute(ins,(scode0,hiduke0,sname0,lank0,zenne0,hajime0,takane0,yasune0,dekidaka0,baibai0,jikaso0,hakokab0,hairima0,hitohai0,per0,pbr0,eps0,bps0,tenki0,heikin0,filler01,filler02));
       conn.commit()
     except:
       print('※※※　ＤＢ更新エラー発生スキップします　※※※')
       continue
   if yosoku_label[i3] == '6' :
     cnt6 = cnt6 + 1
   elif yosoku_label[i3] == '5' :
     cnt5 = cnt5 + 1
   elif yosoku_label[i3] == '4' :
     cnt4 = cnt4 + 1
   elif yosoku_label[i3] == '3' :
     cnt3 = cnt3 + 1
   elif yosoku_label[i3] == '2' :
     cnt2 = cnt2 + 1
   else :
     cnt1 = cnt1 + 1

conn.commit()
print("処理終了","lank6:",cnt6,"lank5:",cnt5,"lank4:",cnt4,"lank3:",cnt3,"lank2:",cnt2,"lank1:",cnt1)


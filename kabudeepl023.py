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
import tensorflow as tf
import tensorflow.contrib.keras as keras

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
from keras.utils import np_utils

from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier
import random, re
import sklearn
sklearn.__version__

stdate  = input("分析開始日:")
enddate = input("分析終了日:")
yosdate = input("予測対象日:")
wlank   = '0'

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()

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

# ラベルデータをone-hotベクトルに直す
labels = {
    '1': [1, 0, 0, 0, 0, 0], 
    '2': [0, 1, 0, 0, 0, 0],
    '3': [0, 0, 1, 0, 0, 0],
    '4': [0, 0, 0, 1, 0, 0],
    '5': [0, 0, 0, 0, 1, 0],
    '6': [0, 0, 0, 0, 0, 1]
}

y_train = np.array(list(map(lambda v : labels[v] , train_label)))
x_train = np.array(train_data)

y_test = np.array(list(map(lambda v : labels[v] , test_label)))
x_test = np.array(test_data)

# モデル構造を定義
Dense = keras.layers.Dense
model = keras.models.Sequential()
model.add(Dense(504, activation='relu', input_shape=(504,)))
model.add(Dense(6, activation='softmax'))
model.summary()

# モデルを構築
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy'])

# 学習を実行
model.fit(x_train, y_train,
    batch_size=128,
    epochs=200)

# モデルを評価
score = model.evaluate(x_test, y_test, verbose=1)
print('正解率=', score[1], 'loss=', score[0])

sql = 'select * from "kabumst3" WHERE "hiduke0" = %s ORDER BY "hiduke0" ASC'
cursor.execute(sql,(yosdate,));
results2 = cursor.fetchall()

total_len2 = len(results2)
alg0 = "DeepLearning"

yosoku_data  = []
yosoku_label = []
for i2 in range(total_len2):
   data2  = results2[i2][4:]
   label2 = results2[i2][3]
   yosoku_data.append(data2)

yosoku_data = np.array(yosoku_data)
yosoku_label = model.predict_classes(yosoku_data)

cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0

for i3 in range(total_len2):
   yosoku_label2 = yosoku_label[i3]
   if yosoku_label2 == 6 :
     print('level6:', results2[i3][0])
   if yosoku_label2 > 2 :
     data1 = results2[i3]
     scode0    = data1[0]
     hiduke0   = data1[1]
     sname0    = data1[2]
     lank0     = str(yosoku_label2)
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
   if yosoku_label2 == 6 :
     cnt6 = cnt6 + 1
   elif yosoku_label2 == 5 :
     cnt5 = cnt5 + 1
   elif yosoku_label2 == 4 :
     cnt4 = cnt4 + 1
   elif yosoku_label2 == 3 :
     cnt3 = cnt3 + 1
   elif yosoku_label2 == 2 :
     cnt2 = cnt2 + 1
   else :
     cnt1 = cnt1 + 1

conn.commit()
print("処理終了","lank6:",cnt6,"lank5:",cnt5,"lank4:",cnt4,"lank3:",cnt3,"lank2:",cnt2,"lank1:",cnt1)

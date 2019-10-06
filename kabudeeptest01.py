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
import random, re
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
from sklearn.utils.testing import all_estimators

stdate  = input("分析開始日:")
enddate = input("分析終了日:")
yosdate = input("予測対象日:")
wlank   = '0'

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()

sql = 'select * from "kabumst" WHERE "lank0" > %s and "hiduke0" >= %s and "hiduke0" <= %s ORDER BY "hiduke0" ASC'
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

# classifierのアルゴリズム全てを取得する --- (*1)
warnings.filterwarnings('ignore')
allAlgorithms = all_estimators(type_filter="classifier")

for(name, algorithm) in allAlgorithms:
    # 各アリゴリズムのオブジェクトを作成 --- (*2)
    clf = algorithm()

    # 学習して、評価する --- (*3)
    clf.fit(train_data, train_label)
    y_pred = clf.predict(test_data)
    print(name,"の正解率 = " , accuracy_score(test_label, y_pred))


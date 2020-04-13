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
import codecs

#hiduke = input("対象日(YYYYMMDD):")
#hiduke = datetime.date.today()

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()

sql = 'select hiduke0 from "kabutrn" WHERE "scode0" > %s ORDER BY "hiduke0" DESC'
cursor.execute(sql,('0000',));
enddate = cursor.fetchone()
hiduke  = enddate[0]
hiduke_s = str(hiduke)

alg0 = "RandomForestClassifier"
alg1 = "ExtraTreeClassifier"

kin0 =  '2000'

sql = 'select * from "kabuyosoku3" WHERE "hiduke0" = %s and "zenne0" < %s ORDER BY "filler02" ASC'
cursor.execute(sql,(hiduke,kin0,));
yosoku31 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku3" WHERE "hiduke0" = %s and "zenne0" < %s'
cursor.execute(sql,(hiduke,kin0,));
endpointer = cursor.fetchall()
endpointer31  = int(endpointer[0][0])

stpointer = 0

file = open(rf"C:\Users\manap\OneDrive\デスクトップ\hantei\buysel\buymsg" + hiduke_s + ".txt", 'w')

text1 =  "\n" + "＊＊＊＊＊＊ level3 株価2000円未満抽出 ＊＊＊＊＊＊" + "\n"
file.write(text1)
for i in range(stpointer,endpointer31):
  scode   = yosoku31[i][0]
  hiduke0 = yosoku31[i][1]
  kabukazen = yosoku31[i][4]
  lank    = yosoku31[i][3]
  arglizm =  yosoku31[i][21] 
  text2 = "arglizm:" + str(arglizm) + "scode:" + str(scode) + " day:" + str(hiduke0) + " kin:" + str(kabukazen) + " lank:" + str(lank) + "\n"
  file.write(text2)

file.close()

print("処理終了")


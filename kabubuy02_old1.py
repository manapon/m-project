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

sql = 'select * from "kabuyosoku" WHERE "hiduke0" = %s and "filler02" = %s ORDER BY "scode0" ASC'
cursor.execute(sql,(hiduke,alg0,));
yosoku11 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku" WHERE "hiduke0" = %s and "filler02" = %s'
cursor.execute(sql,(hiduke,alg0,));
endpointer = cursor.fetchall()
endpointer11  = int(endpointer[0][0])

sql = 'select * from "kabuyosoku" WHERE "hiduke0" = %s and "filler02" = %s ORDER BY "scode0" ASC'
cursor.execute(sql,(hiduke,alg1,));
yosoku12 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku" WHERE "hiduke0" = %s and "filler02" = %s'
cursor.execute(sql,(hiduke,alg1,));
endpointer = cursor.fetchall()
endpointer12  = int(endpointer[0][0])



sql = 'select * from "kabuyosoku2" WHERE "hiduke0" = %s and "filler02" = %s ORDER BY "scode0" ASC'
cursor.execute(sql,(hiduke,alg0,));
yosoku21 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku2" WHERE "hiduke0" = %s and "filler02" = %s'
cursor.execute(sql,(hiduke,alg0,));
endpointer = cursor.fetchall()
endpointer21  = int(endpointer[0][0])

sql = 'select * from "kabuyosoku2" WHERE "hiduke0" = %s and "filler02" = %s ORDER BY "scode0" ASC'
cursor.execute(sql,(hiduke,alg1,));
yosoku22 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku2" WHERE "hiduke0" = %s and "filler02" = %s'
cursor.execute(sql,(hiduke,alg1,));
endpointer = cursor.fetchall()
endpointer22  = int(endpointer[0][0])



sql = 'select * from "kabuyosoku3" WHERE "hiduke0" = %s and "filler02" = %s ORDER BY "scode0" ASC'
cursor.execute(sql,(hiduke,alg0,));
yosoku31 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku3" WHERE "hiduke0" = %s and "filler02" = %s'
cursor.execute(sql,(hiduke,alg0,));
endpointer = cursor.fetchall()
endpointer31  = int(endpointer[0][0])

sql = 'select * from "kabuyosoku3" WHERE "hiduke0" = %s and "filler02" = %s ORDER BY "scode0" ASC'
cursor.execute(sql,(hiduke,alg1,));
yosoku32 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku3" WHERE "hiduke0" = %s and "filler02" = %s'
cursor.execute(sql,(hiduke,alg1,));
endpointer = cursor.fetchall()
endpointer32  = int(endpointer[0][0])

stpointer = 0

file = open(rf"C:\Users\manap\OneDrive\デスクトップ\hantei\buysel\buymsg" + hiduke_s + ".txt", 'w')

text1 =  "\n" + "level1 DeepLearning" + "\n"
file.write(text1)
for i in range(stpointer,endpointer11):
  scode   = yosoku11[i][0]
  hiduke0 = yosoku11[i][1]
  kabukazen = yosoku11[i][4]
  lank    = yosoku11[i][3]
  arglizm =  yosoku11[i][21] 
  text2 = "scode:" + str(scode) + " day:" + str(hiduke0) + " kin:" + str(kabukazen) + " lank:" + str(lank) + "\n"
  file.write(text2)

text1 =  "\n" + "level1 RandomForestClassifier" + "\n"
file.write(text1)
for i in range(stpointer,endpointer12):
  scode   = yosoku12[i][0]
  hiduke0 = yosoku12[i][1]
  kabukazen = yosoku12[i][4]
  lank    = yosoku12[i][3]
  arglizm =  yosoku12[i][21] 
  text2 = "scode:" + str(scode) + " day:" + str(hiduke0) + " kin:" + str(kabukazen) + " lank:" + str(lank) + "\n"
  file.write(text2)

text1 =  "\n" + "level2 DeepLearning" + "\n"
file.write(text1)
for i in range(stpointer,endpointer21):
  scode   = yosoku21[i][0]
  hiduke0 = yosoku21[i][1]
  kabukazen = yosoku21[i][4]
  lank    = yosoku21[i][3]
  arglizm =  yosoku21[i][21] 
  text2 = "scode:" + str(scode) + " day:" + str(hiduke0) + " kin:" + str(kabukazen) + " lank:" + str(lank) + "\n"
  file.write(text2)

text1 =  "\n" + "level2 RandomForestClassifier" + "\n"
file.write(text1)
for i in range(stpointer,endpointer22):
  scode   = yosoku22[i][0]
  hiduke0 = yosoku22[i][1]
  kabukazen = yosoku22[i][4]
  lank    = yosoku22[i][3]
  arglizm =  yosoku22[i][21] 
  text2 = "scode:" + str(scode) + " day:" + str(hiduke0) + " kin:" + str(kabukazen) + " lank:" + str(lank) + "\n"
  file.write(text2)

text1 =  "\n" + "level3 DeepLearning" + "\n"
file.write(text1)
for i in range(stpointer,endpointer31):
  scode   = yosoku31[i][0]
  hiduke0 = yosoku31[i][1]
  kabukazen = yosoku31[i][4]
  lank    = yosoku31[i][3]
  arglizm =  yosoku31[i][21] 
  text2 = "scode:" + str(scode) + " day:" + str(hiduke0) + " kin:" + str(kabukazen) + " lank:" + str(lank) + "\n"
  file.write(text2)

text1 =  "\n" + "level3 RandomForestClassifier" + "\n"
file.write(text1)
for i in range(stpointer,endpointer32):
  scode   = yosoku32[i][0]
  hiduke0 = yosoku32[i][1]
  kabukazen = yosoku32[i][4]
  lank    = yosoku32[i][3]
  arglizm =  yosoku32[i][21] 
  text2 = "scode:" + str(scode) + " day:" + str(hiduke0) + " kin:" + str(kabukazen) + " lank:" + str(lank) + "\n"
  file.write(text2)

file.close()

print("処理終了")


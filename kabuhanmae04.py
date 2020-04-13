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

#stpointer = int(input("開始ポインタ:"))
stpointer = 0

hiduke = datetime.date.today()

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()

sql = 'delete from "kabuyosoku4" WHERE "scode0" > 0000'
cursor.execute(sql);

sql = 'select * from "kabuyosoku" WHERE "scode0" > 0 ORDER BY "scode0" ASC'
cursor.execute(sql);
yosoku1 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku" WHERE "scode0" > 0 '
cursor.execute(sql);
endpointer1 = cursor.fetchall()
endpointer  = int(endpointer1[0][0])

print ("日付：",hiduke,"Connected!","総件数：",endpointer)
ren = 1
for i in range(stpointer,endpointer):
  scode   = yosoku1[i][0]
  hiduke0 = yosoku1[i][1]
  kabukanow = yosoku1[i][4]
  lank    = yosoku1[i][3]
  arglizm =  yosoku1[i][21] 
  sql = 'select * from "kabutrn" WHERE "scode0" = %s and "hiduke0" < %s ORDER BY "hiduke0" DESC'
  cursor.execute(sql,(scode,hiduke0,));
  results = cursor.fetchone()
  kabukazen = results[3]
  hidukezen = results[1]
  print (scode,"日付前:",hidukezen,"株価前：",kabukazen,"日付後:",hiduke0,"株価前：",kabukanow)
  if kabukanow > kabukazen :
    data1     = yosoku1[i]
    scode0    = data1[0]
    hiduke0   = data1[1]
    sname0    = data1[2]
    lank0     = data1[3]
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
    filler02  = data1[21]
    ins = 'INSERT INTO kabuyosoku4 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
      cursor.execute(ins,(scode0,hiduke0,sname0,lank0,zenne0,hajime0,takane0,yasune0,dekidaka0,baibai0,jikaso0,hakokab0,hairima0,hitohai0,per0,pbr0,eps0,bps0,tenki0,heikin0,filler01,filler02));
      conn.commit()
      print('↑↑↑　出力対象です。　↑↑↑')
    except:
      print('※※※　ＤＢ更新エラー発生スキップします　※※※')
      continue   

conn.commit()
print("処理終了")


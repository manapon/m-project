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

mst = pd.read_csv(rf"C:\Users\manap\OneDrive\デスクトップ\stocklist_all.csv", sep=',')
mstd = mst.values
endpointer = len(mstd)

hiduke = datetime.date.today()

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()
print ("日付：",hiduke,"Connected!","総件数：",endpointer)

cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0

for i in range(stpointer,endpointer):
  scode = mstd[i,0]
  sql = 'select * from "kabumst" WHERE "scode0" = %s ORDER BY "hiduke0" ASC'
  cursor.execute(sql,(scode,));
  results = cursor.fetchall()
  
  outsu = len(results)
  for i2 in range(0,outsu):
    data1 = results[i2]
    hiduke0   = data1[1]
    zenne0    = data1[4]

    #hidukew2 = hiduke0 + datetime.timedelta(weeks=1)
    hidukew2 = hiduke0 + datetime.timedelta(weeks=2)
    #hidukew2 = hiduke0 + datetime.timedelta(days=3)
    try:
      sql = 'select * from "kabumst" WHERE "scode0" = %s and "hiduke0" = %s ORDER BY "hiduke0" ASC'
      cursor.execute(sql,(scode,hidukew2,));
      results2 = cursor.fetchall()
      data2 = results2[0]
      zenne0w2 = data2[4]
      
      uppoint = zenne0w2 / zenne0
      
      if uppoint > 1.5 :
        label = '6'
        cnt6 = cnt6 + 1
        print("lank6:",scode)
      elif uppoint > 1.4 :
        label = '5'
        cnt5 = cnt5 + 1
      elif uppoint > 1.3 :
        label = '4'
        cnt4 = cnt4 + 1
      elif uppoint > 1.2 :
        label = '3'
        cnt3 = cnt3 + 1
      elif uppoint > 1   :
        label = '2'
        cnt2 = cnt2 + 1
      else :
        label = '1'
        cnt1 = cnt1 + 1
      
      sql = 'update "kabumst" set lank0 = %s WHERE "scode0" = %s and "hiduke0" = %s '
      cursor.execute(sql,(label,scode,hiduke0,));
      conn.commit()
      print("更新完了","コード：",scode,hiduke0)
    except:
      cnt0 = cnt0 + 1
      print('未来ＤＢ無しの為スキップ：',scode,hiduke0)

conn.commit()
print("処理終了","lank6:",cnt6,"lank5:",cnt5,"lank4:",cnt4,"lank3:",cnt3,"lank2:",cnt2,"lank1:",cnt1,"lank0:",cnt0)


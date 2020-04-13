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

sql = 'delete from "kabumst" WHERE "scode0" > 0000'
cursor.execute(sql);

for i in range(stpointer,endpointer):
  scode = mstd[i,0]
  sql = 'select * from "kabutrn" WHERE "scode0" = %s ORDER BY "hiduke0" DESC'
  cursor.execute(sql,(scode,));
  results = cursor.fetchall()
  
  tblsu = len(results)
  outsu = tblsu - 7

  for i2 in range(0,outsu):
    data1 = results[i2]
    scode0    = data1[0]
    hiduke0   = data1[1]
    sname0    = data1[2]
    lank0     = '0'

    zenne0    = data1[3]
    hajime0   = data1[4]
    takane0   = data1[5]
    yasune0   = data1[6]
    dekidaka0 = data1[7]
    baibai0   = data1[8]
    jikaso0   = data1[9]
    hakokab0  = data1[10]
    hairima0  = data1[11]
    hitohai0  = data1[12]
    per0      = data1[13]
    pbr0      = data1[14]
    eps0      = data1[15]
    bps0      = data1[16]
    tenki0    = data1[17]
    heikin0   = data1[18]
    filler01  = data1[19]
    filler02  = data1[20]
    
    data1 = results[i2+1]
    
    zenne1    = data1[3]
    hajime1   = data1[4]
    takane1   = data1[5]
    yasune1   = data1[6]
    dekidaka1 = data1[7]
    baibai1   = data1[8]
    jikaso1   = data1[9]
    hakokab1  = data1[10]
    hairima1  = data1[11]
    hitohai1  = data1[12]
    per1      = data1[13]
    pbr1      = data1[14]
    eps1      = data1[15]
    bps1      = data1[16]
    tenki1    = data1[17]
    heikin1   = data1[18]
    filler11  = data1[19]
    filler12  = data1[20]
    
    data1 = results[i2+2]
    
    zenne2    = data1[3]
    hajime2   = data1[4]
    takane2   = data1[5]
    yasune2   = data1[6]
    dekidaka2 = data1[7]
    baibai2   = data1[8]
    jikaso2   = data1[9]
    hakokab2  = data1[10]
    hairima2  = data1[11]
    hitohai2  = data1[12]
    per2      = data1[13]
    pbr2      = data1[14]
    eps2      = data1[15]
    bps2      = data1[16]
    tenki2    = data1[17]
    heikin2   = data1[18]
    filler21  = data1[19]
    filler22  = data1[20]
    
    data1 = results[i2+3]
    
    zenne3    = data1[3]
    hajime3   = data1[4]
    takane3   = data1[5]
    yasune3   = data1[6]
    dekidaka3 = data1[7]
    baibai3   = data1[8]
    jikaso3   = data1[9]
    hakokab3  = data1[10]
    hairima3  = data1[11]
    hitohai3  = data1[12]
    per3      = data1[13]
    pbr3      = data1[14]
    eps3      = data1[15]
    bps3      = data1[16]
    tenki3    = data1[17]
    heikin3   = data1[18]
    filler31  = data1[19]
    filler32  = data1[20]
    
    data1 = results[i2+4]
    
    zenne4    = data1[3]
    hajime4   = data1[4]
    takane4   = data1[5]
    yasune4   = data1[6]
    dekidaka4 = data1[7]
    baibai4   = data1[8]
    jikaso4   = data1[9]
    hakokab4  = data1[10]
    hairima4  = data1[11]
    hitohai4  = data1[12]
    per4      = data1[13]
    pbr4      = data1[14]
    eps4      = data1[15]
    bps4      = data1[16]
    tenki4    = data1[17]
    heikin4   = data1[18]
    filler41  = data1[19]
    filler42  = data1[20]
    
    data1 = results[i2+5]
    
    zenne5    = data1[3]
    hajime5   = data1[4]
    takane5   = data1[5]
    yasune5   = data1[6]
    dekidaka5 = data1[7]
    baibai5   = data1[8]
    jikaso5   = data1[9]
    hakokab5  = data1[10]
    hairima5  = data1[11]
    hitohai5  = data1[12]
    per5      = data1[13]
    pbr5      = data1[14]
    eps5      = data1[15]
    bps5      = data1[16]
    tenki5    = data1[17]
    heikin5   = data1[18]
    filler51  = data1[19]
    filler52  = data1[20]
    
    data1 = results[i2+6]
    
    zenne6    = data1[3]
    hajime6   = data1[4]
    takane6   = data1[5]
    yasune6   = data1[6]
    dekidaka6 = data1[7]
    baibai6   = data1[8]
    jikaso6   = data1[9]
    hakokab6  = data1[10]
    hairima6  = data1[11]
    hitohai6  = data1[12]
    per6      = data1[13]
    pbr6      = data1[14]
    eps6      = data1[15]
    bps6      = data1[16]
    tenki6    = data1[17]
    heikin6   = data1[18]
    filler61  = data1[19]
    filler62  = data1[20]
    
    ins = 'INSERT INTO kabumst VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
      cursor.execute(ins,(scode0,hiduke0,sname0,lank0,zenne0,hajime0,takane0,yasune0,dekidaka0,baibai0,jikaso0,hakokab0,hairima0,hitohai0,per0,pbr0,eps0,bps0,tenki0,heikin0,filler01,filler02,zenne1,hajime1,takane1,yasune1,dekidaka1,baibai1,jikaso1,hakokab1,hairima1,hitohai1,per1,pbr1,eps1,bps1,tenki1,heikin1,filler11,filler12,zenne2,hajime2,takane2,yasune2,dekidaka2,baibai2,jikaso2,hakokab2,hairima2,hitohai2,per2,pbr2,eps2,bps2,tenki2,heikin2,filler21,filler22,zenne3,hajime3,takane3,yasune3,dekidaka3,baibai3,jikaso3,hakokab3,hairima3,hitohai3,per3,pbr3,eps3,bps3,tenki3,heikin3,filler31,filler32,zenne4,hajime4,takane4,yasune4,dekidaka4,baibai4,jikaso4,hakokab4,hairima4,hitohai4,per4,pbr4,eps4,bps4,tenki4,heikin4,filler41,filler42,zenne5,hajime5,takane5,yasune5,dekidaka5,baibai5,jikaso5,hakokab5,hairima5,hitohai5,per5,pbr5,eps5,bps5,tenki5,heikin5,filler51,filler52,zenne6,hajime6,takane6,yasune6,dekidaka6,baibai6,jikaso6,hakokab6,hairima6,hitohai6,per6,pbr6,eps6,bps6,tenki6,heikin6,filler61,filler62));
      conn.commit()
      print("追加完了","コード：",scode0,hiduke0)
    except:
      print('※※※　ＤＢ更新エラー発生スキップします　※※※')

conn.commit()
sql = 'SELECT count(*) from kabumst'
cursor.execute(sql);
results = cursor.fetchall()
print("処理終了　　","ＤＢ件数：",results)


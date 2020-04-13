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

stpointer = 0

mst = pd.read_csv(rf"C:\Users\manap\OneDrive\デスクトップ\stocklist_all.csv", sep=',')
mstd = mst.values
endpointer = len(mstd)

hiduke = datetime.date.today()

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()
print ("日付：",hiduke,"Connected!","総件数：",endpointer)

for i in range(stpointer,endpointer):
  scode = mstd[i,0]
  sql = 'select * from "kabutrn" WHERE "scode0" = %s ORDER BY "hiduke0" ASC'
#  sql = 'select * from "kabutrn" WHERE "scode0" = %s ORDER BY "hiduke0" DESC'
#  sql = 'select * from "kabutrn" WHERE "scode0" = %s and "hiduke0" >= %s and "hiduke0" <= %s ORDER BY "hiduke0" ASC'
  cursor.execute(sql,(scode,));
#  cursor.execute(sql,(scode,stdate,enddate,));
  results = cursor.fetchall()
  
  tblsu = len(results)
  outsu = tblsu - 0

  zennew    = 0
  hajimew   = 0
  takanew   = 0
  yasunew   = 0
  dekidakaw = 0
  baibaiw   = 0
  jikasow   = 0
  hakokabw  = 0
  hairimaw  = 0
  hitohaiw  = 0
  perw      = 0
  pbrw      = 0
  epsw      = 0
  bpsw      = 0
  heikinw   = 0

  for i2 in range(0,outsu):
    cnt0 = 0
    data1 = results[i2]
    scode0    = data1[0]
    hiduke0   = data1[1]
    sname0    = data1[2]
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

    if zenne0 == 0 :
      zenne0 = zennew
      cnt0 = cnt0 + 1
    else :
      zennew = zenne0
    if hajime0 == 0 :
      hajime0 = hajimew
      cnt0 = cnt0 + 1
    else :
      hajimew = hajime0
    if takane0 == 0 :
      takane0 = takanew
      cnt0 = cnt0 + 1
    else :
      takanew = takane0
    if yasune0 == 0 :
      yasune0 = yasunew
      cnt0 = cnt0 + 1
    else :
      yasunew = yasune0
    if dekidaka0 == 0 :
      dekidaka0 = dekidakaw
      cnt0 = cnt0 + 1
    else :
      dekidakaw = dekidaka0
    if baibai0 == 0 :
      baibai0 = baibaiw
      cnt0 = cnt0 + 1
    else :
      baibaiw = baibai0
    if jikaso0 == 0 :
      jikaso0 = jikasow
      cnt0 = cnt0 + 1
    else :
      jikasow = jikaso0
    if hakokab0 == 0 :
      hakokab0 = hakokabw
      cnt0 = cnt0 + 1
    else :
      hakokabw = hakokab0
    if hairima0 == 0 :
      hairima0 = hairimaw
      cnt0 = cnt0 + 1
    else :
      hairimaw = hairima0
    if hitohai0 == 0 :
      hitohai0 = hitohaiw
      cnt0 = cnt0 + 1
    else :
      hitohaiw = hitohai0
    if per0 == 0 :
      per0 = perw
      cnt0 = cnt0 + 1
    else :
      perw = per0
    if pbr0 == 0 :
      pbr0 = pbrw
      cnt0 = cnt0 + 1
    else :
      pbrw = pbr0
    if eps0 == 0 :
      eps0 = epsw
      cnt0 = cnt0 + 1
    else :
      epsw = eps0
    if bps0 == 0 :
      bps0 = bpsw
      cnt0 = cnt0 + 1
    else :
      bpsw = bps0

    if tenki0  == '晴れ' :
      tenki0 = '1'
      cnt0 = cnt0 + 1
    elif tenki0  == '晴のち曇' :
      tenki0 = '2'
      cnt0 = cnt0 + 1
    elif tenki0  == '晴時々曇' :
      tenki0 = '3'
      cnt0 = cnt0 + 1
    elif tenki0  == '晴一時雨' :
      tenki0 = '4'
      cnt0 = cnt0 + 1
    elif tenki0  == '晴のち雨' :
      tenki0 = '5'
      cnt0 = cnt0 + 1
    elif tenki0  == '曇り' :
      tenki0 = '6'
      cnt0 = cnt0 + 1
    elif tenki0  == '曇のち晴' :
      tenki0 = '7'
      cnt0 = cnt0 + 1
    elif tenki0  == '曇時々晴' :
      tenki0 = '8'
      cnt0 = cnt0 + 1
    elif tenki0  == '曇時々晴' :
      tenki0 = '8'
      cnt0 = cnt0 + 1
    elif tenki0  == '雨' :
      tenki0 = '9'
      cnt0 = cnt0 + 1
    elif tenki0  == '雨のち晴' :
      tenki0 = '10'
      cnt0 = cnt0 + 1
    elif tenki0  == '曇時々雨' :
      tenki0 = '11'
      cnt0 = cnt0 + 1
    elif tenki0  == '雨時々曇' :
      tenki0 = '12'
      cnt0 = cnt0 + 1
    elif tenki0  == '曇のち雨' :
      tenki0 = '13'
      cnt0 = cnt0 + 1
    elif tenki0  == '雨のち曇' :
      tenki0 = '14'
      cnt0 = cnt0 + 1
    elif tenki0  == '曇一時雨' :
      tenki0 = '15'
      cnt0 = cnt0 + 1
    elif tenki0  == '大雨' :
      tenki0 = '19'
      cnt0 = cnt0 + 1
    elif tenki0  == '暴風雨' :
      tenki0 = '20'
      cnt0 = cnt0 + 1
    if filler01 is None :
      filler01  = 0
      cnt0 = cnt0 + 1
    if filler02 is None :
      filler02  = '0'
      cnt0 = cnt0 + 1

    if cnt0 > 0 :
#      print('コード：',scode,hiduke0)
      sql = 'update "kabutrn" set zenne0 = %s,hajime0 = %s,takane0 = %s,yasune0 = %s,dekidaka0 = %s,baibai0 = %s,jikaso0 = %s,hakokab0 = %s,hairima0 = %s,hitohai0 = %s,per0 = %s,pbr0 = %s,eps0 = %s,bps0 = %s,tenki0 = %s,filler01 = %s,filler02 = %s  WHERE "scode0" = %s and "hiduke0" = %s '
      cursor.execute(sql,(zenne0,hajime0,takane0,yasune0,dekidaka0,baibai0,jikaso0,hakokab0,hairima0,hitohai0,per0,pbr0,eps0,bps0,tenki0,filler01,filler02,scode,hiduke0,));
      conn.commit()

conn.commit()
sql = 'SELECT count(*) from kabutrn'
cursor.execute(sql);
results = cursor.fetchall()
print("処理終了　　","ＤＢ件数：",results)


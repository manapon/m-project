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

driver = webdriver.Chrome()
url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"
driver.get(url)
a = driver.find_element_by_class_name("forecastCity")
ten01 = a.text
ten11 = ten01.split("\n")
ten111 = ten11[1].split(" ")
tenki = ten111[0]
driver.close()

driver = webdriver.Chrome()
url = "https://stocks.finance.yahoo.co.jp/"
driver.get(url)
b = driver.find_element_by_id("wrapper")
hei01 = b.text
hei11 = hei01.split("\n")
heikin = hei11[48].replace(",","") 
driver.close()

mst = pd.read_csv(rf"C:\Users\manap\OneDrive\デスクトップ\stocklist_all.csv", sep=',')
#mst = pd.read_csv(rf"C:\Users\manap\OneDrive\デスクトップ\stocklist_all.csv", sep=';')
mstd = mst.values
endpointer = len(mstd)

#hiduke = str(datetime.date.today())
hiduke = '20191106'

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()
print ("日付：",hiduke,"Connected!","総件数：",endpointer)

sql = 'SELECT count(*) from kabutrn WHERE "hiduke0" = %s '
cursor.execute(sql,(hiduke,));
rerunpointer2 = cursor.fetchall()
rerunpointer  = int(rerunpointer2[0][0])

if rerunpointer >= endpointer :
  print ("リランの必要なしです。開始ポインター：",rerunpointer)
  sys.exit()

for i2 in range(rerunpointer,endpointer):
  scode1 = str(mstd[i2,0])
  scode  = mstd[i2,0]
  sname = mstd[i2,1]

#  hedlessモード
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  driver = webdriver.Chrome(options=options)

#  非hedlessモード
#  driver = webdriver.Chrome()
  url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=" + scode1
  driver.get(url)
#  キャプチャ
#  driver.get_screenshot_as_file(rf"C:\Users\manap\OneDrive\デスクトップ\sshot\ss" + scode1 + ".png")
  c = driver.find_element_by_class_name("innerDate")
  d = driver.find_element_by_id("rfindex")
  kabu1 = []
  kabu2 = []
  kabu1 = c.text
  kabu2 = d.text
  kabu01 = kabu1.split("\n")
  kabu02 = kabu2.split("\n")
  kabu001 = kabu01[0].split("（")
  zenne = kabu001[0].replace(",","")      # 前日終値
  if zenne == '---' :
    zenne   = 0
  
  kabu001 = kabu01[2].split("（")
  hajime  = kabu001[0].replace(",","")    # 始値
  if hajime == '---' :
    hajime   = 0
  
  kabu001 = kabu01[4].split("（")
  kabu011 = kabu001[0].split("高")
  if kabu011[0] == 'ストップ' :
    takane  = kabu011[1].replace(",","")    # 高値
  else:
    takane  = kabu011[0].replace(",","")    # 高値
  if takane == '---' :
    takane   = 0
  
  kabu001 = kabu01[6].split("（")
  kabu011 = kabu001[0].split("安")
  if kabu011[0] == 'ストップ' :
    yasune  = kabu011[1].replace(",","")    # 安値
  else:
    yasune  = kabu011[0].replace(",","")    # 安値
  if yasune == '---' :
    yasune   = 0
  
  kabu001 = kabu01[8].split("株")
  dekidaka = kabu001[0].replace(",","")   # 出来高
  if dekidaka == '---' :
    dekidaka   = 0
  
  kabu001 = kabu01[10].split("千")
  baibai  = kabu001[0].replace(",","")    # 売買代金
  if baibai == '---' :
    baibai   = 0
  
  kabu002 = kabu02[1].split("百")
  jikaso  = kabu002[0].replace(",","")    # 時価総額
  if jikaso == '---' :
    jikaso   = 0
  
  kabu002 = kabu02[3].split("株")
  hakokab = kabu002[0].replace(",","")    # 発行済株式数
  if hakokab == '---' :
    hakokab   = 0
  
  kabu002 = kabu02[5].split("%")
  hairima = kabu002[0].replace(",","")    # 配当利回り
  if hairima == '---' :
    hairima   = 0
  
  kabu002 = kabu02[7].split("（")
  hitohai = kabu002[0].replace(",","")    # 1株配当
  if hitohai == '---' :
    hitohai   = 0
  
  kabu12  = kabu02[9].split("倍")
  kabu002 = kabu12[0].split(")")
  if kabu002[0] == '---' :
    per   = 0
  else:
    per1   = kabu002[1].replace(" ","")    # PER
    per    = per1.replace(",","")          # PER
    if per == '---' :
      per   = 0
  
  kabu12  = kabu02[11].split("倍")
  kabu002 = kabu12[0].split(")")
  if kabu002[0] == '---':
    pbr   = 0
  else:
    pbr   = kabu002[1].replace(" ","")    # PBR
    if pbr == '---' :
      pbr   = 0
  
  kabu12  = kabu02[13].split("（")
  kabu002 = kabu12[0].split(")")
  if kabu002[0] == '---':
     eps   = 0
  else:
     kabu012 = kabu002[1].replace(",","")
     eps     = kabu012.replace(" ","")       # EPS
     if eps == '---' :
       eps   = 0
  
  kabu12  = kabu02[15].split("（")
  kabu002 = kabu12[0].split(")")
  if kabu002[0] == '---':
    bps   = 0
  else:
    kabu012 = kabu002[1].replace(",","")
    bps     = kabu012.replace(" ","")       # BPS
    if bps == '---' :
      bps   = 0

  print(i2,"コード:",scode,"前日終値",zenne,"始値",hajime,"高値",takane,"安値",yasune,"出来高",dekidaka,"売買代金",baibai)
  print("時価総額",jikaso,"発行済株式数",hakokab,"配当利回り",hairima,"1株配当",hitohai,"PER",per,"PBR",pbr,"EPS",eps,"BPS",bps)
  driver.close()
  ins = 'INSERT INTO kabutrn VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
  try:
    cursor.execute(ins,(scode,hiduke,sname,zenne,hajime,takane,yasune,dekidaka,baibai,jikaso,hakokab,hairima,hitohai,per,pbr,eps,bps,tenki,heikin));
    conn.commit()
  except:
    print('※※※　ＤＢ更新エラー発生スキップします　※※※')
    continue

conn.commit()
sql = 'SELECT count(*) from kabutrn'
cursor.execute(sql);
results = cursor.fetchall()
print("処理終了　　","ＤＢ件数：",results)


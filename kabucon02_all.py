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

sql = 'delete from "kabumst2" WHERE "scode0" > 0000'
cursor.execute(sql);

for i in range(stpointer,endpointer):
  scode = mstd[i,0]
  sql = 'select * from "kabutrn" WHERE "scode0" = %s ORDER BY "hiduke0" DESC'
  cursor.execute(sql,(scode,));
  results = cursor.fetchall()
  
  tblsu = len(results)
  outsu = tblsu - 14

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
    
    data1 = results[i2+7]
    
    zenne7    = data1[3]
    hajime7   = data1[4]
    takane7   = data1[5]
    yasune7   = data1[6]
    dekidaka7 = data1[7]
    baibai7   = data1[8]
    jikaso7   = data1[9]
    hakokab7  = data1[10]
    hairima7  = data1[11]
    hitohai7  = data1[12]
    per7      = data1[13]
    pbr7      = data1[14]
    eps7      = data1[15]
    bps7      = data1[16]
    tenki7    = data1[17]
    heikin7   = data1[18]
    filler71  = data1[19]
    filler72  = data1[20]

    data1 = results[i2+8]
    
    zenne8    = data1[3]
    hajime8   = data1[4]
    takane8   = data1[5]
    yasune8   = data1[6]
    dekidaka8 = data1[7]
    baibai8   = data1[8]
    jikaso8   = data1[9]
    hakokab8  = data1[10]
    hairima8  = data1[11]
    hitohai8  = data1[12]
    per8      = data1[13]
    pbr8      = data1[14]
    eps8      = data1[15]
    bps8      = data1[16]
    tenki8    = data1[17]
    heikin8   = data1[18]
    filler81  = data1[19]
    filler82  = data1[20]

    data1 = results[i2+9]
    
    zenne9    = data1[3]
    hajime9   = data1[4]
    takane9   = data1[5]
    yasune9   = data1[6]
    dekidaka9 = data1[7]
    baibai9   = data1[8]
    jikaso9   = data1[9]
    hakokab9  = data1[10]
    hairima9  = data1[11]
    hitohai9  = data1[12]
    per9      = data1[13]
    pbr9      = data1[14]
    eps9      = data1[15]
    bps9      = data1[16]
    tenki9    = data1[17]
    heikin9   = data1[18]
    filler91  = data1[19]
    filler92  = data1[20]

    data1 = results[i2+10]
    
    zenne10    = data1[3]
    hajime10   = data1[4]
    takane10   = data1[5]
    yasune10   = data1[6]
    dekidaka10 = data1[7]
    baibai10   = data1[8]
    jikaso10   = data1[9]
    hakokab10  = data1[10]
    hairima10  = data1[11]
    hitohai10  = data1[12]
    per10      = data1[13]
    pbr10      = data1[14]
    eps10      = data1[15]
    bps10      = data1[16]
    tenki10    = data1[17]
    heikin10   = data1[18]
    filler101  = data1[19]
    filler102  = data1[20]

    data1 = results[i2+11]
    
    zenne11    = data1[3]
    hajime11   = data1[4]
    takane11   = data1[5]
    yasune11   = data1[6]
    dekidaka11 = data1[7]
    baibai11   = data1[8]
    jikaso11   = data1[9]
    hakokab11  = data1[10]
    hairima11  = data1[11]
    hitohai11  = data1[12]
    per11      = data1[13]
    pbr11      = data1[14]
    eps11      = data1[15]
    bps11      = data1[16]
    tenki11    = data1[17]
    heikin11   = data1[18]
    filler111  = data1[19]
    filler112  = data1[20]

    data1 = results[i2+12]
    
    zenne12    = data1[3]
    hajime12   = data1[4]
    takane12   = data1[5]
    yasune12   = data1[6]
    dekidaka12 = data1[7]
    baibai12   = data1[8]
    jikaso12   = data1[9]
    hakokab12  = data1[10]
    hairima12  = data1[11]
    hitohai12  = data1[12]
    per12      = data1[13]
    pbr12      = data1[14]
    eps12      = data1[15]
    bps12      = data1[16]
    tenki12    = data1[17]
    heikin12   = data1[18]
    filler121  = data1[19]
    filler122  = data1[20]

    data1 = results[i2+13]
    
    zenne13    = data1[3]
    hajime13   = data1[4]
    takane13   = data1[5]
    yasune13   = data1[6]
    dekidaka13 = data1[7]
    baibai13   = data1[8]
    jikaso13   = data1[9]
    hakokab13  = data1[10]
    hairima13  = data1[11]
    hitohai13  = data1[12]
    per13      = data1[13]
    pbr13      = data1[14]
    eps13      = data1[15]
    bps13      = data1[16]
    tenki13    = data1[17]
    heikin13   = data1[18]
    filler131  = data1[19]
    filler132  = data1[20]
    
    ins = 'INSERT INTO kabumst2 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    try:
      cursor.execute(ins,(scode0,hiduke0,sname0,lank0,zenne0,hajime0,takane0,yasune0,dekidaka0,baibai0,jikaso0,hakokab0,hairima0,hitohai0,per0,pbr0,eps0,bps0,tenki0,heikin0,filler01,filler02,zenne1,hajime1,takane1,yasune1,dekidaka1,baibai1,jikaso1,hakokab1,hairima1,hitohai1,per1,pbr1,eps1,bps1,tenki1,heikin1,filler11,filler12,zenne2,hajime2,takane2,yasune2,dekidaka2,baibai2,jikaso2,hakokab2,hairima2,hitohai2,per2,pbr2,eps2,bps2,tenki2,heikin2,filler21,filler22,zenne3,hajime3,takane3,yasune3,dekidaka3,baibai3,jikaso3,hakokab3,hairima3,hitohai3,per3,pbr3,eps3,bps3,tenki3,heikin3,filler31,filler32,zenne4,hajime4,takane4,yasune4,dekidaka4,baibai4,jikaso4,hakokab4,hairima4,hitohai4,per4,pbr4,eps4,bps4,tenki4,heikin4,filler41,filler42,zenne5,hajime5,takane5,yasune5,dekidaka5,baibai5,jikaso5,hakokab5,hairima5,hitohai5,per5,pbr5,eps5,bps5,tenki5,heikin5,filler51,filler52,zenne6,hajime6,takane6,yasune6,dekidaka6,baibai6,jikaso6,hakokab6,hairima6,hitohai6,per6,pbr6,eps6,bps6,tenki6,heikin6,filler61,filler62,zenne7,hajime7,takane7,yasune7,dekidaka7,baibai7,jikaso7,hakokab7,hairima7,hitohai7,per7,pbr7,eps7,bps7,tenki7,heikin7,filler71,filler72,zenne8,hajime8,takane8,yasune8,dekidaka8,baibai8,jikaso8,hakokab8,hairima8,hitohai8,per8,pbr8,eps8,bps8,tenki8,heikin8,filler81,filler82,zenne9,hajime9,takane9,yasune9,dekidaka9,baibai9,jikaso9,hakokab9,hairima9,hitohai9,per9,pbr9,eps9,bps9,tenki9,heikin9,filler91,filler92,zenne10,hajime10,takane10,yasune10,dekidaka10,baibai10,jikaso10,hakokab10,hairima10,hitohai10,per10,pbr10,eps10,bps10,tenki10,heikin10,filler101,filler102,zenne11,hajime11,takane11,yasune11,dekidaka11,baibai11,jikaso11,hakokab11,hairima11,hitohai11,per11,pbr11,eps11,bps11,tenki11,heikin11,filler111,filler112,zenne12,hajime12,takane12,yasune12,dekidaka12,baibai12,jikaso12,hakokab12,hairima12,hitohai12,per12,pbr12,eps12,bps12,tenki12,heikin12,filler121,filler122,zenne13,hajime13,takane13,yasune13,dekidaka13,baibai13,jikaso13,hakokab13,hairima13,hitohai13,per13,pbr13,eps13,bps13,tenki13,heikin13,filler131,filler132));
      conn.commit()
      print("追加完了","コード：",scode0,hiduke0)
    except:
      print('※※※　ＤＢ更新エラー発生スキップします　※※※')

conn.commit()
sql = 'SELECT count(*) from kabumst2'
cursor.execute(sql);
results = cursor.fetchall()
print("処理終了　　","ＤＢ件数：",results)


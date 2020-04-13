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

new_book = px.Workbook()
sheet3 = new_book.active
sheet3["A1"].value = "証券ｺｰﾄﾞ"
sheet3["B1"].value = "日付"
sheet3["C1"].value = "株価(前)"
sheet3["D1"].value = "株価(後)"
sheet3["E1"].value = "上昇率"
sheet3["F1"].value = "ｱﾙｺﾞﾘｽﾞﾑ"
sheet3["G1"].value = "ﾗﾝｸ"
new_book.save(rf"C:\Users\manap\OneDrive\デスクトップ\hantei\kabuhantei05.xlsx")

conn = psycopg2.connect(host="localhost", database="manaponDB", user="postgres",password="manapon1219")
cursor = conn.cursor()

sql = 'select * from "kabuyosoku5" WHERE "scode0" > 0 ORDER BY "scode0" ASC'
cursor.execute(sql);
yosoku1 = cursor.fetchall()

sql = 'SELECT count(*) from "kabuyosoku5" WHERE "scode0" > 0 '
cursor.execute(sql);
endpointer1 = cursor.fetchall()
endpointer  = int(endpointer1[0][0])

print ("日付：",hiduke,"Connected!","総件数：",endpointer)
ren = 1
for i in range(stpointer,endpointer):
  scode   = yosoku1[i][0]
  hiduke0 = yosoku1[i][1]
  kabukazen = yosoku1[i][4]
  lank    = yosoku1[i][3]
  arglizm =  yosoku1[i][21] 
  hidukew2 = hiduke0 + datetime.timedelta(weeks=2)
  try:
    sql = 'select * from "kabutrn" WHERE "scode0" = %s and "hiduke0" = %s ORDER BY "hiduke0" ASC'
    cursor.execute(sql,(scode,hidukew2,));
    results = cursor.fetchone()
    kabukanow = results[3]
    jyousyouritu = kabukanow / kabukazen
    sql = 'update "kabuyosoku5" set filler01 = %s WHERE "scode0" = %s and "hiduke0" = %s '
    cursor.execute(sql,(kabukanow,scode,hiduke0,));
    conn.commit()
    print("更新完了","コード：",scode,hiduke0,"上昇率：",jyousyouritu,arglizm)
    ren = ren + 1
    sheet3["A"+str(ren)].value = scode
    sheet3["B"+str(ren)].value = hiduke0
    sheet3["C"+str(ren)].value = kabukazen
    sheet3["D"+str(ren)].value = kabukanow
    sheet3["E"+str(ren)].value = jyousyouritu
    sheet3["F"+str(ren)].value = arglizm
    sheet3["G"+str(ren)].value = lank
    new_book.save(rf"C:\Users\manap\OneDrive\デスクトップ\hantei\kabuhantei05.xlsx")
  except:
    print("更新不要","コード：",scode,hiduke0)
    
conn.commit()
print("処理終了")


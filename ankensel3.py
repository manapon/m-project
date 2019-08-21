import os
import glob
import openpyxl as px
import numpy as np
import pandas as pd
workbook = px.load_workbook(rf'C:\Users\manap\OneDrive\デスクトップ\ankensheet\(A002)案件シート（2019_北九州市_電子レセプトシステム運用保守支援業務）.xlsm',data_only=True)
sheet1 = workbook["案件シート"]
job = sheet1["D9"]
ankenmei = sheet1["D4"]
tantou   = sheet1["S5"]
kin1 = sheet1["G20"]
rieki1 = sheet1["G36"]
sheet2 = workbook["申請案件シート"]
kin2 = sheet2["G20"]
rieki2 = sheet2["G36"]
print("job:",job.value,"kin1:",kin1.value,"rieki1:",rieki1.value,"kin2:",kin2.value,"rieki2:",rieki2.value)
new_book = px.Workbook()
sheet3 = new_book.active
sheet3["A1"].value = "JOBNO"
sheet3["B1"].value = "売上金額(最新)"
sheet3["C1"].value = "営業利益(最新)"
sheet3["D1"].value = "売上金額(計画)"
sheet3["E1"].value = "営業利益(計画)"
sheet3["F1"].value = "案件名"
sheet3["G1"].value = "ＰＪ担当"

sheet3["A2"].value = job.value
sheet3["B2"].value = kin1.value
sheet3["C2"].value = rieki1.value
sheet3["D2"].value = kin2.value
sheet3["E2"].value = rieki2.value
sheet3["F2"].value = ankenmei.value
sheet3["G2"].value = tantou.value

new_book.save(rf"C:\Users\manap\OneDrive\デスクトップ\ankensel.xlsx")

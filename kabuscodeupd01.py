from selenium import webdriver
import chromedriver_binary
import time
from time import sleep
import numpy as np
import datetime
import psycopg2
import sys
import os
import shutil
import glob
import openpyxl as px
import pandas as pd

stpointer = 0
hiduke1 = datetime.date.today()
hiduke = str(hiduke1)

driver = webdriver.Chrome()
url = "http://kabusapo.com/dl-file/dl-stocklist.php"
driver.get(url)

print("少しお待ち下さい")
sleep(5)
print("お待たせしました")

shutil.copyfile(rf"C:\Users\manap\Downloads\stocklist.csv", rf"C:\Users\manap\OneDrive\デスクトップ\stocklist_all.csv")
shutil.copyfile(rf"C:\Users\manap\Downloads\stocklist.csv", rf"C:\Users\manap\OneDrive\デスクトップ\証券コード\stocklist_" + hiduke + ".csv")

driver.close()

os.remove(rf"C:\Users\manap\Downloads\stocklist.csv")


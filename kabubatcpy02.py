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

print("休日用BATをコピーします。")
sleep(5)
shutil.copyfile(rf"C:\Users\manap\OneDrive\デスクトップ\ＰＧＭ\kabusel_2.bat", rf"C:\Users\manap\OneDrive\デスクトップ\ＰＧＭ\kabusel.bat")
print("kabusel_2.batコピー完了")

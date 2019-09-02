from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get("http://www.python.org")

scode = '3626'
print("scode=", scode)
# HTMLを取得
url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=" + scode
print("url=", url)
driver.get(url)

a = driver.find_element_by_name("code")
b = driver.find_elements_by_class_name("lineFi clearfix")
c = driver.find_element_by_id("takane")



assert "Python" in driver.title

import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(5)
search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)
driver.quit()



from bs4 import BeautifulSoup
import urllib.request as req

scode = '3626'

print("scode=", scode)


# HTMLを取得
url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=" + scode

print("url=", url)

res = req.urlopen(url)

# HTMLを解析
soup = BeautifulSoup(res, "html.parser")

# 任意のデータを抽出 --- (※1)

a1 = soup.innerDate.lineFi clearfix.
b1 = soup.html.body.p


kaisine = soup.find("lineFi clearfix").string
kaisine = soup.find("lineFi clearfix").string
price = soup.select(".lineFi clearfix").string
print("kaisine=", price)







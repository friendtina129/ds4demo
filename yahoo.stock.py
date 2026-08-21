from bs4 import BeautifulSoup
import requests
from pprint import pprint

url="https://tw.stock.yahoo.com/quote/2345.TW"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
response.raise_for_status() #有異常就終止
#pprint( response.text)

#2
#將網頁內容交給 bs 分析
soup = BeautifulSoup(response.text, "html.parser")  #  html原始碼透過 html.parser分析

accton2345 = soup.find("span", class_="Fw(600) Fz(16px)--mobile Fz(14px) D(f) Ai(c) C($c-trend-down)")
#從網頁抓取class關鍵字
print(f'智邦2345目前股價: {accton2345.text}')
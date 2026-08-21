from bs4 import BeautifulSoup
import requests
from pprint import pprint

url="https://tw.news.yahoo.com/finance"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
}

headers2 = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Content-Type": "application/json",
    "Origin": "https://example.com",
    "Pragma": "no-cache",
    "Referer": "https://example.com/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    ),
    
}

response = requests.get(url, headers=headers2)
response.raise_for_status() #有異常就終止
#pprint( response.text)

#2
#將網頁內容交給 bs 分析
soup = BeautifulSoup(response.text, "html.parser")  #  html原始碼透過 html.parser分析

news_lists = soup.find_all('a')   # hyper link --> <a href='新聞網址'> 新聞標題 </a>
print(f'共抓取超連結數量: {len(news_lists)}')

for n in news_lists:
    print(f'新聞標題: {n.text}  |  連結位址:  {n.get("href")}')
    
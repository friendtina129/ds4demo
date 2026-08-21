from bs4 import BeautifulSoup
import requests
from pprint import pprint
import time     # 提供暫停的功能
import random   # 產生 2~3 的亂數產生器

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


#重複使用 request.get  直接回傳 bs 結構
def parser(url):    
    response = requests.get(url, headers=headers2)
    response.raise_for_status() #有異常就終止
    return BeautifulSoup(response.text)


soup = parser("https://tw.news.yahoo.com/finance")
news_lists = soup.find_all('a')
for n in news_lists[40:42]:    
    #如果可以 去除非相關的連結( 透過 ai 判斷)
    print(f'新聞標題: {n.text}')
    # 把新聞連結再丟給 parser( link ) 撈一次
    # 迴圈會跑很快 每次先暫停各 2~3秒  使用  time package
    delay = random.uniform(2,3.5)      #亂數產生 2~3.5秒  
    time.sleep(delay)                  #讓電腦暫時休眠 指定的秒數後再開始工作 
    subsoup = parser(n.get('href'))
    body = subsoup.body.text
    print(f'新聞內容: {body}')
    #print(f'新聞標題: {n.text}  |  連結位址:  {n.get("href")}')
from bs4 import BeautifulSoup
import requests
from pprint import pprint

url = "https://mymis168.github.io/bs4demo/apple.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response.raise_for_status() #有異常就終止
#pprint( response.text)

#將網頁內容交給 bs 分析
soup = BeautifulSoup(response.text, "html.parser")  #  html原始碼透過 html.parser分析

#soup 代表APPLE.HTML 的結構
print(f'網頁的title是: {soup.title.text}')
print(f'網頁的h2是: {soup.h2.text}')
print("========= 所有可用的 function ==========")
#pprint(dir(soup))
#pprint(soup.body.text)

#開始搜尋網頁的指定內容
tag_a = soup.a
tag_b = soup.find("a") #不指定條件 只回傳第一個
tag_c = soup.find("a", href="#ipad")

print(f'a = {tag_a.text}')
print(f'b = {tag_b.text}')
print(f'c = {tag_c.text}')

#尋找 class 為依據的條件
class_a = soup.find("div", class_="section-header")  # class_ 原因因為 python 有 class指令 衝突
print(f'c = {class_a.text}')
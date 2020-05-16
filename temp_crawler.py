''' 爬蟲作業三 顯示縣市氣溫'''
from bs4 import BeautifulSoup
import requests
import prettytable

t = prettytable.PrettyTable(["縣市名","溫度"], encoding="utf8")
r1 = requests.get(
        "https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        },
        params={
            "date":"Mon, 13 Apr 2020 02:55:24 GMT",
            "Referer":"https://www.cwb.gov.tw/V8/C/W/County_TempTop.html"
      }
    )
r1.encoding="utf-8"
b1=BeautifulSoup(r1.text,"html.parser")
r2=b1.find_all("tr")
for r3 in r2:
    rr1=(r3.find("th",{"scope":"row"}).text)
    rr2=(r3.find("span",{"class":"tem-C is-active"}).text)
    t.add_row((rr1,rr2))
print(t)


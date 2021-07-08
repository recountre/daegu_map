import requests
from bs4 import BeautifulSoup

url = "http://covid19.daegu.go.kr/00937400.html"

response = requests.get(url)
html = response
soup = BeautifulSoup(html.content.decode('utf-8', 'replace'), 'html.parser')
find = soup.select_one('#bbsList > tbody > tr.info_td > td > table > tbody > tr:nth-child(2) > td:nth-child(5) > p')
tx = find.text
print(tx)
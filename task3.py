from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as BS

url = "https://www.greenatom.ru/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

webpage = urlopen(req).read()

soup = BS(webpage, 'html.parser')

all_tags = soup.find_all()
tags_with_attrs = 0
for tag in all_tags:
    if tag.attrs:
        tags_with_attrs += 1

print(f"Кол-во тэгов на главной странице greenatom.ru: {len(all_tags)}. "
      f"Аттрибуты присутствуют в {tags_with_attrs} из них.")

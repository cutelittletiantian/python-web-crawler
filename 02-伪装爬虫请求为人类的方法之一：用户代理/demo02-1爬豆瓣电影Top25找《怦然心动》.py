import requests
from bs4 import BeautifulSoup
from bs4 import Tag

# 豆瓣top25的url
url = "https://movie.douban.com/top250?start=0&filter="

# 发出请求，伪装爬虫为浏览器，使用用户代理"User-Agent"
resp = requests.get(url=url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ("
                                                    "KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 "
                                                    "Edg/91.0.864.59"})

# 解析响应报文
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 定位"div class='hd'的标签"
content_div_hd = soup.find_all(name="div", class_="hd")  # type: list[Tag]

# 取出中文标题，title这个class的第一个
content_all = []
for div_hd in content_div_hd:
    content_all.append(
        div_hd.find_all(name="span", class_="title", limit=1)[0]
    )

# 剥去html标签及标题的空格，取出所有的标题
titles = [content.text.strip() for content in content_all]

# 找怦然心动是不是top25
if "怦然心动" in titles:
    print("怦然心动是豆瓣top25电影")

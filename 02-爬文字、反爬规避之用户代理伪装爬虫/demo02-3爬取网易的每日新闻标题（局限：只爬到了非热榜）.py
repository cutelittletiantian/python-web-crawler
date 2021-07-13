import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 待爬取的url（这里用的是静态资源......害，演示用嘛）
url = "http://nocturne.bczcdn.com/zip/1625207762993_63705/web.html"

# 伪装成浏览器的用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 " \
     "Safari/537.36 Edg/91.0.864.59 "

# 请求资源
resp = requests.get(url=url, headers={"User-Agent": ua})
# 防止乱码
resp.encoding = "utf-8"

# 解析响应资源内容
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 爬rank类标签
soup_rank = soup.find_all(name="td", class_="rank")  # type: list[Tag]

# rank类标签里面取出<a>标签
titles = []
for rank in soup_rank:
    titles.append(rank.find(name="a").text)

for title in titles:
    print(title)

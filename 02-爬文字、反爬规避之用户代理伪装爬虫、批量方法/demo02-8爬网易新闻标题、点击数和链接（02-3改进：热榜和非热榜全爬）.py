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
resp.encoding = resp.apparent_encoding

# 解析响应资源内容
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 所有标签在tabContents active标签下
content_all = soup.find_all(name="div", class_="tabContents active")  # type: list[Tag]

# 找出所有的标题所在标签tr
titleTags = []  # type: list[Tag]
for content in content_all:
    titleTags.extend(content.find_all(name="tr"))

# 筛选：不含<a>标签的tr要丢掉
titleTags = [titleTag for titleTag in titleTags if titleTag.find(name="a") is not None]  # type: list[Tag]

# 新闻标题, 点击量, 链接
newsItems = [(titleTag.find(name="a").text.strip(),
             int(titleTag.find(name="td", class_="cBlue").text.strip()),
             titleTag.find(name="a").attrs["href"]) for titleTag in titleTags]

for newsTitle, newsClick, newsLink in newsItems:
    print(f"新闻标题 {newsTitle}")
    print(f"点击量 {newsClick}")
    print(f"链接 {newsLink}")

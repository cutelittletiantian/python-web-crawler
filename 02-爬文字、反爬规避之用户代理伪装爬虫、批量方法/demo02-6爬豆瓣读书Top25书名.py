import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 豆瓣读书url
url = "https://book.douban.com/top250?start=0"

# 用户代理（伪装浏览器）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67 "

# 请求页面
resp = requests.get(url=url, headers={"User-Agent": ua})

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 取标签
bookInfoTags = soup.find_all(name="tr", class_="item")  # type: list[Tag]

bookInfos = []
for bookInfoTag in bookInfoTags:
    # 书名（格式要做好过滤）
    bookInfos.append(
        bookInfoTag.find(name="div", class_="pl2").find(name="a").text.strip().replace("\n", "").replace(" ", "")
    )

for bookInfo in bookInfos:
    print(bookInfo)

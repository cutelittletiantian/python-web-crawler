import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# B站协议和域名
bilibiliHost = "https://www.bilibili.com"
# 视频url
url = f"{bilibiliHost}/video/BV18V411z7cV"

# 用户代理（伪装浏览器）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67 "

# 请求页面
resp = requests.get(url=url, headers={"User-Agent": ua})

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 找到所有侧边相关视频的标签
content_all = soup.find_all(name="div", class_="card-box")  # type: list[Tag]
# 精选：筛出info标签
infoTags = [content.select(selector=".info a")[0] for content in content_all]  # type: list[Tag]

# 取出其中的标题和href
for infoTag in infoTags:
    print(f'{infoTag.text.strip()}:{infoTag.attrs["href"]}')

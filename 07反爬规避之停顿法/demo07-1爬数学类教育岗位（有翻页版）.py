import time
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 数学岗位url
url = "https://s.yingjiesheng.com/search.php?word=%E6%95%B0%E5%AD%A6&sort=score&start={0}"

# 伪装浏览器（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67 "

# 翻前3页
titles = []
for page in range(0, 21, 10):
    # 请求弹幕接口
    resp = requests.get(url=url.format(page), headers={"User-Agent": ua})
    # 统一前后台的编码，防止乱码
    resp.encoding = resp.apparent_encoding
    # 解析
    soup = BeautifulSoup(markup=resp.text, features="lxml")

    # 抓标题
    content_all = soup.find_all(name="h3", class_="title")  # type: list[Tag]
    # 取标题
    titles.extend([content.find(name="a").text.strip().replace("\n", "") for content in content_all])

    # 反爬规避：停顿两秒
    time.sleep(2)

for title in titles:
    print(title)

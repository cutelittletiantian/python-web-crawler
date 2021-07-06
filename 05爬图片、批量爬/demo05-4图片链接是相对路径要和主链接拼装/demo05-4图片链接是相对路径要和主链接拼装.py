import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 网站总url
url = "https://www.stockvault.net/"
# 浏览器伪装（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.64 "
# 保存图片的路径
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# 请求资源
resp = requests.get(url=url, headers={"User-Agent": ua})

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 取出所有带有图片url的标签
content_item = soup.find_all(name="div", class_="item")  # type: list[Tag]
for item in content_item:
    # 只有相对url（src不行，亲测，要用data-src）
    imgUrlRev = item.find(name="img")["data-src"]
    # 拼接完整路径
    imgUrl = url + imgUrlRev

    # 这里先不爬虫了，只想说明遇到相对路径的时候，不要忘记组装完整路径
    print(imgUrl)

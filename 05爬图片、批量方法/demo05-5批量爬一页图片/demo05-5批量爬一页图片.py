import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 网站总url
url = "https://www.futta.net/photo-season/autumn/"
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

# 找出所有待爬取的图片资源标签
content_all = soup.find_all(name="img", class_=["imgphoto", "imgphotob"])  # type: list[Tag]

# 取出图片的url
for imageIndex, image in enumerate(content_all, start=1):
    # 图片的url
    imgUrl = image["src"]
    # imgUrl = image.attrs["src"]  # 两种写法都可以，效果等同

    # 请求图片资源
    imgResp = requests.get(url=imgUrl, headers={"User-Agent": ua})

    # 执行保存
    if imgResp.status_code == 200:
        with open(file=os.path.join(targetPath, f"{imageIndex}.jpg"), mode="wb") as fpImg:
            fpImg.write(imgResp.content)

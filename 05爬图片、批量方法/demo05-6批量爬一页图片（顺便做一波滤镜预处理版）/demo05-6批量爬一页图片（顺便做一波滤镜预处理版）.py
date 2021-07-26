import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from PIL import Image, ImageFilter

# 网站总url
url = "https://nocturne-spider.baicizhan.com/2020/08/20/photo/"
# 浏览器伪装（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.64 "

# 请求资源
resp = requests.get(url=url, headers={"User-Agent": ua})

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 找出div标签下的所有img
content_div_img = soup.find(name="div", class_="post-body").find_all(name="img")  # type: list[Tag]

# 保存图片的路径
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# 逐个下载图片
for indexImg, imgContent in enumerate(content_div_img, start=1):
    # 请求图片资源
    imgResp = requests.get(url=imgContent["src"], headers={"User-Agent": ua})

    # 保存图片
    if imgResp.status_code == 200:
        # 图片路径
        imgPath = os.path.join(targetPath, f"{indexImg}.jpg")

        # 先保存图片
        with open(file=imgPath, mode="wb") as fp:
            fp.write(imgResp.content)
        # 再做图片处理
        with Image.open(fp=imgPath) as fpBefore:
            fpAfter = fpBefore.filter(ImageFilter.EMBOSS)
            fpAfter.save(imgPath)

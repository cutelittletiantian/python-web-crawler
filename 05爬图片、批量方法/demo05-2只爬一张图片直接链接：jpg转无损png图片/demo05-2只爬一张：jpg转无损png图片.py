import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 单个图片的url
url = "https://npbcz.files.wordpress.com/2020/09/4-1.jpg"

# 请求资源（这里不用伪装）
resp = requests.get(url=url)

# 取出图片的二进制流
imgContent = resp.content

# 写入文件中
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)
with open(file=os.path.join(targetPath, "math.png"), mode="wb") as fImg:
    fImg.write(imgContent)

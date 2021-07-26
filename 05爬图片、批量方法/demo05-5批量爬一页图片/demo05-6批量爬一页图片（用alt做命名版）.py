import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 网站总url
url = "https://www.dpm.org.cn/lights/royal.html"
# 浏览器伪装（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.64 "
# 保存图片的路径"result/dpm"
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)
targetPath = f"{targetPath}/dpm"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# 请求资源
resp = requests.get(url=url, headers={"User-Agent": ua})
# 报文编码与显示编码统一，防止乱码
resp.encoding = resp.apparent_encoding

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 找出所有故宫壁纸（简单期间这里只爬预览图）
content_all = soup.find_all(name="div", class_="pic")  # type: list[Tag]

# 取出img标签
imgTags = [imgTag.find(name="img") for imgTag in content_all]  # type: list[Tag]

# 剥去标签，取出图片名和标签url
imgInfos = [(imgTag.attrs["alt"].replace(" ", "_"), imgTag.attrs["src"]) for imgTag in imgTags]

# 下载图片
for imgName, imgUrl in imgInfos:
    # 请求图片资源
    resp = requests.get(url=imgUrl, headers={"User-Agent": ua})
    # 下载图片
    if resp.status_code == 200:
        with open(file=os.path.join(targetPath, f"{imgName}.jpg"), mode="wb") as fp:
            fp.write(resp.content)
        # 完成后给个消息，以免长期无响应
        print(f'{os.path.join(targetPath, f"{imgName}.jpg")}: 下载成功')
    else:
        print(f"error {resp.status_code} occurred on requesting {imgUrl}")

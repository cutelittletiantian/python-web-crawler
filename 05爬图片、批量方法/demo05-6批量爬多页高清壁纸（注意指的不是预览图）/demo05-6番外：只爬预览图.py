import os
import requests
from bs4.element import Tag
from bs4 import BeautifulSoup

# Note: 本问题方法不唯一，根据观察到的网页结构，中间要随机应变

# 爬取的图片保存的路径
targetPath = "result_preview"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# 故宫博物馆 协议://域名
hostname = "https://www.dpm.org.cn"
# 伪装爬虫：用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.64 "

# 全部图片内容
content_all = []  # type: list[Tag]
# 页面表示的相对url
pageRelUrl = "/lights/royal/p/{0}.html"
# 演示爬取3页图片的内容（这个部分的内容和方法1中有点不一样）
for page in range(1, 4):
    # 请求当前页资源
    resp = requests.get(url=f"{hostname}{pageRelUrl.format(page)}", headers={"User-Agent": ua})
    # 解析
    soup = BeautifulSoup(markup=resp.text, features="lxml")
    # 取出图片内容
    content_all.extend(soup.find_all(name="div", class_="pic"))

# 剥去标签，取出所有预览图url
previews = [content.find(name="img").attrs["src"] for content in content_all]

for preIndex, preview in enumerate(previews, start=1):
    # 请求资源
    resp = requests.get(url=preview, headers={"User-Agent": ua})
    # 保存图片
    if resp.status_code == 200:
        with open(file=os.path.join(targetPath, f"{preIndex}.jpg"), mode="wb") as fp:
            fp.write(resp.content)
            print(f'{os.path.join(targetPath, f"{preIndex}.jpg")}预览图下载成功')
    else:
        print(f"error {resp.status_code} occurred on requesting {preview}")

import os
import requests
from bs4.element import Tag
from bs4 import BeautifulSoup

# Note: 本问题方法不唯一，根据观察到的网页结构，中间要随机应变

# 爬取的图片保存的路径
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# 故宫博物馆 协议://域名
hostname = "https://www.dpm.org.cn"
# 伪装爬虫：用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.64 "

# 全部图片内容
content_all = []  # type: list[Tag]
# 下一页的相对链接（初始值：初始页url）
nextPageRel = "/lights/royal.html"
# 演示爬取3页图片的内容
for page in range(3):
    # 请求资源
    resp = requests.get(url=hostname+nextPageRel, headers={"User-Agent": ua})
    # 解析
    soup = BeautifulSoup(markup=resp.text, features="lxml")
    # 取出图片内容
    content_all.extend(soup.find_all(name="div", class_="pic"))
    # 下一页标签
    nextPageRel = soup.find(name="a", id="next")["href"]

# 剥去标签，组合出高清图所在的url
urlForHDimgs = [f'{hostname}{content.find(name="a").attrs["href"]}' for content in content_all]

# 所有的高清图url
hdUrls = []
# 访问高清图资源url，下载图片
for urlForHDimg in urlForHDimgs:
    # 请求资源
    resp = requests.get(url=urlForHDimg, headers={"User-Agent": ua})
    if resp.status_code == 200:
        # 解析html
        soup = BeautifulSoup(markup=resp.text, features="lxml")
        # 找到高清图资源的url
        hdUrl = soup.find(name="div", class_="pictureshow").find(name="img").attrs["src"]
        hdUrls.append(hdUrl)
    else:
        print(f"error {resp.status_code} occurred on requesting {urlForHDimg}")

# 逐个遍历高清图url
for urlIndex, hdUrl in enumerate(hdUrls, start=1):
    # 请求资源
    resp = requests.get(url=hdUrl, headers={"User-Agent": ua})
    if resp.status_code == 200:
        # 下载高清图
        with open(file=os.path.join(targetPath, f"{urlIndex}.jpg"), mode="wb") as fp:
            fp.write(resp.content)
        print(f'{os.path.join(targetPath, f"{urlIndex}.jpg")}: successfully download')
    else:
        print(f"error {resp.status_code} occurred on requesting {hdUrl}")

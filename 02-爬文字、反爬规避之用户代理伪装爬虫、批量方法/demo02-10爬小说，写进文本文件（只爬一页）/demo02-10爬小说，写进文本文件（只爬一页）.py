import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 待爬取的url：《小王子》
url = "http://www.xiaowangzi.org/index.html"

# 伪装成浏览器的用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.70 "

# 请求资源（这个网站反爬机制比较严格，除了ua还要用上请求头的其它内容，使得请求报文头部伪装得更像人类一些）
resp = requests.get(url=url, headers={
    "User-Agent": ua,
    "Upgrade-Insecure-Requests": "1",
    "If-None-Match": "2cd0-526e8d2463d40-gzip",
    "If-Modified-Since": "Tue, 15 Dec 2015 05:11:25 GMT",
    "Host": "www.xiaowangzi.org",
    "Connection": "keep-alive",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0"
})
# 防止乱码
resp.encoding = resp.apparent_encoding

# 如果响应了
if resp.status_code == 200:

    # 解析响应资源内容
    soup = BeautifulSoup(markup=resp.text, features="lxml")

    # 所有的正文标签
    contentAll = soup.find(name="div", id="cont").find_all(name="p")  # type: list[Tag]
    # 正文文本（不要插图）
    paragraphs = [content.text.strip() for content in contentAll if not content.find(name="img")]
    # 正文之间的多余空格要去掉
    paragraphs = [para.split() for para in paragraphs[:]]
    paragraphs = ["".join(paraItems) for paraItems in paragraphs[:]]

    # 写进文件的位置
    targetPath = "小王子.txt"
    # 不存在则新建文件
    if not os.path.exists(path=targetPath):
        with open(file=targetPath, mode="w", encoding=resp.encoding):
            # 新建完毕，空语句
            pass

    # 打开文件，追加写入
    with open(file=targetPath, mode="a", encoding=resp.encoding) as fp:
        # 最后一个链接可以不要
        fp.write("\n".join(paragraphs[:-1]))

else:
    print(f"Error {resp.status_code} on requesting {url}")

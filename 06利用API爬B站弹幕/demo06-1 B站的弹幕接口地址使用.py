import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 弹幕cid（这里假设就直接先给定了）
cid = "218710655"
# 弹幕接口
bulletApi = f"https://comment.bilibili.com/{cid}.xml"

# 伪装浏览器（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67 "

# 请求弹幕接口
resp = requests.get(url=bulletApi.format(cid), headers={"User-Agent": ua})
# 统一前后台的编码，防止乱码
resp.encoding = resp.apparent_encoding

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 提取弹幕节点
bulletTags = soup.find_all(name="d")  # type: list[Tag]
# 剥去标签
bullets = [bullet.text for bullet in bulletTags]

for bullet in bullets:
    print(bullet)

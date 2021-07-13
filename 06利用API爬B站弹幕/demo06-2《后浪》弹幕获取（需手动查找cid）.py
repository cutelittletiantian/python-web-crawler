import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 《后浪》视频url
vidUrl = "https://www.bilibili.com/video/av412935552/"

# 弹幕cid（通过视频url打开审查元素，找出的cid）
cid = "186803402"
# 弹幕接口
bulletApi = "https://comment.bilibili.com/{0}.xml"

# 伪装浏览器（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67 "

# 请求弹幕接口
resp = requests.get(url=bulletApi.format(cid), headers={"User-Agent": ua})
# 统一前后台的编码，防止乱码
resp.encoding = resp.apparent_encoding

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 取出弹幕标签
bulletAll = soup.find_all(name="d")  # type: list[Tag]

# 剥去标签，得到弹幕
bullets = [bullet.text for bullet in bulletAll]

print(bulletAll)

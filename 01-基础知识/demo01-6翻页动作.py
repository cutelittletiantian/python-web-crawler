import requests
from bs4.element import Tag
from bs4 import BeautifulSoup

# 带页数的糗事百科url，页数待填充，即{0}处填充页数
urlTemplate = r"https://www.qiushibaike.com/text/page/{0}/"

# 翻前5页的内容，找段子手昵称
for page in range(1, 6):
    # 请求页面
    resp = requests.get(url=urlTemplate.format(page))
    # 解析
    soup = BeautifulSoup(markup=resp.text, features="lxml")
    # 定位段子手昵称的标签<h2>，这里没有其它h2标签与之冲突
    jokerNames = soup.find_all(name="h2")  # type: list[Tag]
    # 剥去标签
    for jokerName in jokerNames:
        print(jokerName.string.strip())
        # 随机应变：这样爬也可以
        # print(jokerName.text.strip())

# Note: 也可以用demo01-1的方法，组装url不停地遍历

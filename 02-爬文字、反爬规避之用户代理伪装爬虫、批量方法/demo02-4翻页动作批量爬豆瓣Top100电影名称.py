import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 根据翻页时观察出来的url规律，得到的url模板，{0}用来后面的替换
# eg: https://movie.douban.com/top250?start=0, https://movie.douban.com/top250?start=25, ...
urlTemplate = "https://movie.douban.com/top250?start={0}"

# 用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.64 "

# 爬内容
content_all = []  # type: list[Tag]
# 每页25项
for itemOffset in range(0, 25 * 4, 25):
    # 请求资源
    resp = requests.get(url=urlTemplate.format(itemOffset), headers={"User-Agent": ua})
    if resp.status_code == 200:
        # 解析
        soup = BeautifulSoup(markup=resp.text, features="lxml")
        # 取出英文标题标签
        content_all.extend(
            soup.find_all(name="span", class_="title")
        )

# 剥去html标签
titles = [content.text for content in content_all]

for title in titles:
    print(title)

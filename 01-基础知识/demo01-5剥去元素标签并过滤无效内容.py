import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 待爬取URL
url = "https://nocturne-spider.baicizhan.com/2020/08/14/xun/"

# 请求网页资源
resp = requests.get(url=url)

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 爬取strong节点
content_all = soup.find_all(name="strong")  # type: list[Tag]
# print(content_all)

for content in content_all:
    # 去掉tag并过滤无效内容（过程是一步步尝试确定出来的）
    if content.text != "":
        print(content.text)
    # 这里等效的爬取，下面这种也可以
    # if content.string is not None:
    #     print(content.string)

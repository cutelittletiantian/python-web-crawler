import requests
from bs4 import BeautifulSoup

# 靶场
url = "https://nocturne-spider.baicizhan.com/2020/08/14/2/"

# 访问
resp = requests.get(url=url)

# 相应内容转为字符串
html = resp.text

# 解析
soup = BeautifulSoup(markup=html, features="lxml")

# 查找html标签<em>
content_all = soup.find_all(name="em")
print(content_all)

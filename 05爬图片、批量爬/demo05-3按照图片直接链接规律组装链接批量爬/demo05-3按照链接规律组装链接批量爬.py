import requests
from bs4 import BeautifulSoup
import os

# 批量爬的url模板
url = "https://npbcz.files.wordpress.com/2020/09/{0}-1.jpg?w=400"

# 结果路径
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# 16日至19日的图片
for day in range(16, 20):
    # 请求资源
    resp = requests.get(url=url.format(day))
    # 保存图片
    with open(file=os.path.join(targetPath, f"{day}-1.jpg"), mode="wb") as fp:
        fp.write(resp.content)

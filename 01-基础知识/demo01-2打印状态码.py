# demo01-2：获取某页面响应后，查看状态码
import requests

url = "https://nocturne-spider.baicizhan.com/6789"

# 获取响应
resp = requests.get(url=url)

# 找到响应码即可
print(resp.status_code)

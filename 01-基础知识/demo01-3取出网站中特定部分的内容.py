# demo01-3：读取相应得到的html文件，随意按字符串操作钠盐切片
import requests

url = "https://nocturne-spider.baicizhan.com/"

# 请求、响应
resp = requests.get(url=url)

# 正常响应(状态码：200)
if resp.status_code == 200:
    respText = resp.text
    # 随意切片输出
    print(respText[4107:4114])
else:
    print("数据载入有误")

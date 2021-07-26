import requests

# 随便给个带有错误符号的url
url_fault = "https:！！www.pexels.com。zh-cn。photo！4996652。"
# 字符串替换（支持链式调用）
url = url_fault.replace("！", "/").replace("。", "/")

# 用户代理（伪装爬虫为浏览器）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.64 "

# 请求资源
resp = requests.get(url=url, headers={"User-Agent": ua})

# 后续操作......
print(resp.text[:200])

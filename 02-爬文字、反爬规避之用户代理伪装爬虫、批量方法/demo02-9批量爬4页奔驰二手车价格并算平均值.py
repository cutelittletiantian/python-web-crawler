import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 待爬取的url，找规律......{0}处填页号，开始于1
url = "https://www.che168.com/china/benchi/benchicji/a0_1msdgscncgpi1ltocsp{0}exx0/?pvareaid=102179#currengpostion"

# 伪装成浏览器的用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 " \
     "Safari/537.36 Edg/91.0.864.59 "

prices = []
# 批量爬4页
for page in range(1, 5):
    # 请求资源
    resp = requests.get(url=url.format(page), headers={"User-Agent": ua})
    # 防止乱码
    resp.encoding = resp.apparent_encoding

    # 解析响应资源内容
    soup = BeautifulSoup(markup=resp.text, features="lxml")

    # 取出所有价格的标签
    priceTags = soup.find_all(name="div", class_="cards-price-box")  # type: list[Tag]
    # 取出所有的价格数值
    prices.extend([float(price.find(name="em").text) for price in priceTags if price.find(name="em").text.strip() != ""])

# 计算均值
print(sum(prices) / len(prices))

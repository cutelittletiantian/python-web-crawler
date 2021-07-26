import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 巧克力界面url，翻页规律：page=1, 3, 5..., 对应s=1, 61, 121
urlTemplate = "https://search.jd.com/search?keyword=%E5%B7%A7%E5%85%8B%E5%8A%9B&qrst=1&psort=3&suggest=1.def.0.0&wq" \
              "=%E5%B7%A7%E5%85%8B%E5%8A%9B&stock=1&ev=exbrand_%E5%BE%B7%E8%8A%99%EF%BC%88Dove%EF%BC%89%5E&psort=3" \
              "&page={0}&s={1}&click=0"

# 用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" \
     "91.0.4472.124 Safari/537.36 Edg/91.0.864.67"

# cookie
ck = "__jdu=16159420568861952865174; shshshfpa=5826a8b6-75c2-0083-30e5-46afd5e4f1bd-1619577920; " \
     "shshshfpb=iHWMuGcVgpZueIaMX3h8Y8A%3D%3D; qrsc=3; unpl=V2_ZzNtbUcEFBEiWBFVcxgMVWJTQlhKXhQVJV8RXH0ZXFIzAEJdclRC" \
     "FnUUR1NnGlQUZgsZX0pcRxFFCENkexhdBWMGEV5EVnMlMEsWBi8FXAdvARJYQlJDFHINQ1NyEFUNYDMRXXJWcxVyCEJcfhpdAWAKG1pCX0cWf" \
     "A9CVH0cbDVnCxZtQlVCE3UOTl1Lz%2fKRsouthPLylb%2fb3cvkrpD30dmFIl1LV0EddAlGU3gpXTVmM0AzmuH1zdC5WoDRlomN8E4SWkJTSx" \
     "B2CUJTchBbBW8HEVRFU0MTcDhHZHg%3d; __jdv=122270672|direct|-|none|-|1626414044812; areaId=17; " \
     "ipLoc-djd=17-1381-50713-0; __jda=122270672.16159420568861952865174.1615942057.1626414045.1626846526.6; " \
     "__jdb=122270672.1.16159420568861952865174|6.1626846526; __jdc=122270672; " \
     "shshshfp=e8faac7042779756ff8c8fcd3ee6801a; shshshsID=9e509ec3c4b2a5c2658e47bf1069ea94_1_1626846526958; " \
     "rkv=1.0; " \
     "3AB9D23F7A4B3C9B=27H5E4YJO7IWER4MXWANALUGCQTLQG5CJJDNXDQBVPRMWCBFAIMUTD4GSTJRGI7OAJ4B6MCFFRIV5O657LDWV43Y3Q"

# 所有商品标签
skuTags = []
# 遍历前5页
for page in range(5):
    # 请求资源
    resp = requests.get(url=urlTemplate.format(2 * page + 1, 60 * page + 1), headers={"User-Agent": ua, "cookie": ck})
    # 解析
    soup = BeautifulSoup(markup=resp.text, features="lxml")
    # 取出所有的商品标签
    skuTags.extend(soup.find_all(name="div", class_="gl-i-wrap"))

# 每个商品标签中的信息
skuInfos = []
for skuTag in skuTags:
    # 找出其中的价格和策略
    price = skuTag.find(name="div", class_="p-price").find(name="i").text
    strategyTags = skuTag.find(name="div", class_="p-icons").find_all(name="i")  # type: list[Tag]
    strategies = [strategy.text for strategy in strategyTags]
    skuInfos.append({"价格": price, "策略": " ".join(strategies)})

# 输出结果
for skuInfo in skuInfos:
    print(f"价格:{skuInfo['价格']} 策略:{skuInfo['策略']}")

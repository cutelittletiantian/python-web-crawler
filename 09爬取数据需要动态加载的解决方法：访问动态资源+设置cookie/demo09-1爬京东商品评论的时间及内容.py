import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import json

# 商品评论所在URL
url = "https://item.jd.com/1178886.html"

# 伪装浏览器（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67 "

# cookie
cookie = "__jdu=16159420568861952865174; " \
         "shshshfpa=5826a8b6-75c2-0083-30e5-46afd5e4f1bd-1619577920; " \
         "shshshfpb=iHWMuGcVgpZueIaMX3h8Y8A%3D%3D; " \
         "unpl=V2_ZzNtbUcEFBEiWBFVcxgMVWJTQlhKXhQVJV8RXH0ZXFIzAEJdclRCFnUUR1NnGlQUZgsZX0pcRxFFCENkexhdBWMGEV5EVnMlMEs" \
         "WBi8FXAdvARJYQlJDFHINQ1NyEFUNYDMRXXJWcxVyCEJcfhpdAWAKG1pCX0cWfA9CVH0cbDVnCxZtQlVCE3UOTl1Lz%2fKRsouthPLylb%2" \
         "fb3cvkrpD30dmFIl1LV0EddAlGU3gpXTVmM0AzmuH1zdC5WoDRlomN8E4SWkJTSxB2CUJTchBbBW8HEVRFU0MTcDhHZHg%3d; " \
         "__jdv=122270672|direct|-|none|-|1626414044812; " \
         "__jda=122270672.16159420568861952865174.1615942057.1624930797.1626414045.5; " \
         "__jdc=122270672; shshshfp=83025c30839774566eca1da3c982a7a4; " \
         "areaId=17; ipLoc-djd=17-1381-50713-0; __jdb=122270672.3.16159420568861952865174|5.1626414045; " \
         "shshshsID=8ef6b52dad8a3a124a5f96876b289c39_3_1626414068695; " \
         "3AB9D23F7A4B3C9B=27H5E4YJO7IWER4MXWANALUGCQTLQG5CJJDNXDQBVPRMWCBFAIMUTD4GSTJRGI7OAJ4B6MCFFRIV5O657LDWV43Y3Q"

# 动态资源数据所在url（这个要用心找）
dynamicRsrcUrl = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&" \
                "productId=1178886&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1"

# 请求动态资源
resp = requests.get(url=dynamicRsrcUrl, headers={"User-Agent": ua, "cookie": cookie})

# 加载json字符串为字典
resources = json.loads(s=resp.text.lstrip("fetchJSON_comment98(").rstrip(");"))

# 取出所有的评论
comments = resources["comments"]

# 取出评论的发送时间和内容
commentInfos = [(comment["creationTime"], comment["content"]) for comment in comments]

for creationTime, content in commentInfos:
    print(f"{creationTime} {content}")

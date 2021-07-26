from urllib import parse

# 想要调查的巧克力品牌
chocolateBrands = ["德芙", "徐福记", "阿尔卑斯", "好时", "大白兔", "士力架", "不二家", "费列罗", "明治"]

# url模板
beforeTemplateUrl = "https://search.jd.com/search?keyword={0}&qrst=1&wq={0}&stock=1"

# 填入url
for brand in chocolateBrands:
    # 对brand进行编码再填入
    afterUrl = beforeTemplateUrl.format(parse.quote(string=brand, encoding="utf-8"))
    print(afterUrl)
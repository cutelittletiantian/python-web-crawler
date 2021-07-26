import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import json

# 电视剧列表所在URL
url = "https://movie.douban.com/tv/#!type=tv&tag=热门&sort=recommend&page_limit=20&page_start=0"

# 伪装浏览器（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" \
     "91.0.4472.124 Safari/537.36 Edg/91.0.864.67"

# cookie
cookie = 'bid=dbb9M2fVE4Q; douban-fav-remind=1; __gads=ID=7e6bfae48ca96d19-22501c9ef1c60057:T=1617350723:RT' \
         '=1617350723:S=ALNI_MY0kxzKu1BXSy6_vf8zdhV6BaHjkg; __utmz=30149280.1623210174.3.3.utmcsr=baidu|utmccn=(' \
         'organic)|utmcmd=organic; ll="118254"; __utmc=30149280; __utmc=223695111; ' \
         '__utmz=223695111.1626411233.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ' \
         '_vwo_uuid_v2=D1ED86CCF3BDB7F59E251446261E86F14|10c3a4241e4d717c9576bc7d9d50863b; _pk_ses.100001.4cf6=*; ' \
         'ap_v=0,6.0; __utma=30149280.1949429731.1617350724.1626411233.1626421226.5; __utmb=30149280.0.10.1626421226; ' \
         '__utma=223695111.608737160.1626411233.1626411233.1626421226.2; __utmb=223695111.0.10.1626421226; ' \
         '_pk_id.100001.4cf6=5ae25e0a7bc8824f.1626411232.2.1626421572.1626411253. '

# 动态资源数据所在url（这个要用点心找）
dynamicRsrcUrl = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={0}"

# 电视剧名称、评分、链接逐一取出
movieInfos = []

# 爬5页
for page_start in range(0, 100, 20):
    # 请求动态资源
    resp = requests.get(url=dynamicRsrcUrl.format(page_start), headers={"User-Agent": ua, "cookie": cookie})
    # 加载json字符串为字典
    resources = json.loads(s=resp.text)
    # 取出所有的电视剧信息
    movieSubjects = resources["subjects"]
    # 电视剧名称、评分、链接逐一取出
    movieInfos.extend(
        [
            (
                movieSubject["title"],
                movieSubject["rate"] if movieSubject["rate"].strip() else "暂无评分",
                movieSubject["url"]
            ) for movieSubject in movieSubjects
         ]
    )

for title, rate, movieUrl in movieInfos:
    print(f"{rate} {title} {movieUrl}")

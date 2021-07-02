import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 豆瓣top25的url
url = "https://www.zhihu.com/topic/20753544/intro"

# 可供伪装的浏览器
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 " \
     "Safari/537.36 "

# 请求资源
resp = requests.request(method="get", url=url, headers={"User-Agent": ua})

# 解析标签
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 爬奖项名称
content_all = soup.find_all(name="div", class_="TopicMovieIntro-awardItemTitle")  # type: list[Tag]

# 剥去html标签
awards = [award.text.strip() for award in content_all]

for award in awards:
    print(award)

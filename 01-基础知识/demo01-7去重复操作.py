import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import jieba

# 《飞屋环游记》豆瓣影评
url = "https://movie.douban.com/subject/2129039/comments?sort=new_score&status=P"

# 用户代理（伪装爬虫为浏览器，防止爬虫被拦截）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 " \
     "Safari/537.36 Edg/91.0.864.59 "

# 请求网页资源
resp = requests.get(url=url, headers={"User-Agent": ua})

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 应该爬short标签
content_all = soup.find_all(name="span", class_="short")  # type: list[Tag]

# 去标签
comments = [comment.text for comment in content_all]

# 分词
wordList = []
for comment in comments:
    wordList.extend(jieba.lcut(comment))

# 去重
wordList = list(set(wordList))
print(len(wordList))

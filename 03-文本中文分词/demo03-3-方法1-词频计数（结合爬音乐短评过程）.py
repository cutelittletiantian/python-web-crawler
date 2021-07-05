import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import jieba
# from collections import Counter

# 音乐短评url
url = "https://music.douban.com/subject/30277745/comments/"

# 用户代理
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

# 词频统计
wordFreq = dict()
for word in wordList:
    wordFreq[word] = wordFreq.get(word, 0) + 1
# 排序
wordFreqSorted = sorted(wordFreq.items(), key=lambda item: item[1], reverse=True)

# 前10词频（假设就不清洗了，实际上你知道这个是应该清洗的）
print(wordFreqSorted[:10])

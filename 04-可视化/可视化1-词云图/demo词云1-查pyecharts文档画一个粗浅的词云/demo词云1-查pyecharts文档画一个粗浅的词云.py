import os

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import jieba
from pyecharts.charts import WordCloud
import pyecharts.options as opts
from pyecharts.globals import ThemeType

# 爬取一段文字
url = "https://nocturne-spider.baicizhan.com/2020/09/02/coco/"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 " \
     "Safari/537.36 Edg/91.0.864.59 "
resp = requests.get(url=url, headers={"User-Agent": ua})
soup = BeautifulSoup(markup=resp.text, features="lxml")
# 《寻梦环游记》简介
content_all = soup.find(name="div", class_="post-body")  # type: Tag
# 去html标签
contents = content_all.text

# 分词
wordList = jieba.lcut(contents)
# 词频
wordFreq = dict()
for word in wordList:
    wordFreq[word] = wordFreq.get(word, 0) + 1

# 去单字或标点
for kWord in dict(wordFreq).keys():
    if len(kWord) <= 1:
        wordFreq.pop(kWord)
# print(wordFreq)

# 可视化：分词后的结果生成词云图，字体大小范围为[30,70]，图片宽度为800，高度为500
resultPath = "result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
wcMovie = (
    WordCloud(
        init_opts=opts.InitOpts(theme=ThemeType.CHALK)
    )
    .add(
        series_name="",
        data_pair=[(k, v) for k, v in wordFreq.items()],
        word_size_range=(30, 70),
        width=800,
        height=500
    )
    .render(path=os.path.join(resultPath, "dream.html"))
)

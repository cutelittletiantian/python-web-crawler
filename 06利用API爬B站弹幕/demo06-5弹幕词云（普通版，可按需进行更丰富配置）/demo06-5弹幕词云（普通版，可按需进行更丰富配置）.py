import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from pyecharts.charts import WordCloud
import jieba

# 词云保存路径
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# 弹幕cid（这里假设就直接先给定了）
cid = "218710655"
# 弹幕接口
bulletApi = f"https://comment.bilibili.com/{cid}.xml"

# 伪装浏览器（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67 "

# 请求弹幕接口
resp = requests.get(url=bulletApi.format(cid), headers={"User-Agent": ua})
# 统一前后台的编码，防止乱码
resp.encoding = resp.apparent_encoding

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 提取弹幕节点
bulletTags = soup.find_all(name="d")  # type: list[Tag]
# 剥去标签
bullets = [bullet.text for bullet in bulletTags]

# 分词表
wordList = []
# 分词
for bullet in bullets:
    wordList.extend(jieba.lcut(bullet))

# 单字符清洗（演示方便起见，不做更复杂的清洗）
for word in wordList[:]:
    if len(word) <= 1:
        wordList.remove(word)

# 词频统计
wordFreq = dict()
for word in wordList:
    wordFreq[word] = wordFreq.get(word, 0) + 1

# 词云生成（查pyecharts文档）
# 数据统称为空，字体大小范围为[20,80]，保存并命名词云图为wordcloud.html
wc = (
    WordCloud()
    .add(
        series_name="",
        data_pair=[(k, v) for (k, v) in wordFreq.items()],
        word_size_range=[20, 80]
    )
    .render(path=os.path.join(targetPath, "wordcloud.html"))
)

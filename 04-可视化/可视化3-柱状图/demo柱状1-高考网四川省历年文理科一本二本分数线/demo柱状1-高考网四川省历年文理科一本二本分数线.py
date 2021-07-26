import os

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from pyecharts.charts import Bar

# 待爬取的url（这里用的是静态资源......害，演示用嘛）
url = "http://www.gaokao.com/{0}/fsx/"

# 伪装成浏览器的用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 " \
     "Safari/537.36 Edg/91.0.864.59 "

# 请求资源（四川省）
resp = requests.get(url=url.format("sichuan"), headers={"User-Agent": ua})
# 防止乱码
resp.encoding = resp.apparent_encoding

# 解析响应资源内容
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 找到文理科表所在标签
scoreTblInfoTag = soup.find(name="div", class_="cjArea tm15")
# 取出所有分数线表所在标签
scoreTblTags = scoreTblInfoTag.find_all(name="table")  # type: list[Tag]

# x轴数据（文理同步）
yearTags = scoreTblInfoTag.find(name="tr", class_="wkTit").find_all(name="th")[1:]  # type: list[Tag]
x_data = [year.text.strip() for year in yearTags]

# 表[0]文科一本
wkFirstTags = scoreTblTags[0].find(name="tr", class_="c_blue").find_all(name="td")  # type: list[Tag]
wkFirstItems = [wkScore.text.strip() for wkScore in wkFirstTags]
_, y_wkFirstScores = wkFirstItems[0], [int(wkFirstItem) for wkFirstItem in wkFirstItems[1:]]
# 表[0]文科二本
wkSecondTags = scoreTblTags[0].find(name="tr", class_="c_white").find_all(name="td")  # type: list[Tag]
wkSecondItems = [wkScore.text.strip() for wkScore in wkSecondTags]
_, y_wkSecondScores = wkSecondItems[0], [int(wkSecondItem) for wkSecondItem in wkSecondItems[1:]]

# 表[1]理科一本
lkFirstTags = scoreTblTags[1].find(name="tr", class_="c_blue").find_all(name="td")  # type: list[Tag]
lkFirstItems = [lkScore.text.strip() for lkScore in lkFirstTags]
_, y_lkFirstScores = lkFirstItems[0], [int(lkFirstItem) for lkFirstItem in lkFirstItems[1:]]
# 表[1]理科二本
lkSecondTags = scoreTblTags[1].find(name="tr", class_="c_white").find_all(name="td")  # type: list[Tag]
lkSecondItems = [lkScore.text.strip() for lkScore in lkSecondTags]
_, y_lkSecondScores = lkSecondItems[0], [int(lkSecondItem) for lkSecondItem in lkSecondItems[1:]]

# 可视化
c = (
    Bar()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(series_name="文科一本", y_axis=y_wkFirstScores)
    .add_yaxis(series_name="理科一本", y_axis=y_lkFirstScores)
    .add_yaxis(series_name="文科二本", y_axis=y_wkSecondScores)
    .add_yaxis(series_name="理科二本", y_axis=y_lkSecondScores)
)
# 渲染
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)
c.render(path=os.path.join(targetPath, "sc.html"))

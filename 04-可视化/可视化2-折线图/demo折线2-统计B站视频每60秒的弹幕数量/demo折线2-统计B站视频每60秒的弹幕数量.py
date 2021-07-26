import os
from pyecharts.charts import Line
import pyecharts.options as opts
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import pandas
from pandas import DataFrame, Series, CategoricalDtype

# 【B站弹幕接口p属性含义】
# <d p="157.47900,1,25,16777215,1548340494,0,389b20da,11114024647262210">啧啧，原来阿卡丽那么小？</d>
# 参数1（157.47900）：弹幕出现的时间，以秒数为单位
# 参数2（1）：弹幕的模式，1-3 滚动弹幕，4 底端弹幕，5顶端弹幕，6 逆向弹幕，7 精准定位，8 高级弹幕
# 参数3（25）：字号 （12非常小，16特小，18小，25中，36大，45很大，64特别大）
# 参数4（16777215）：字体的颜色；这串数字是十进制表示；通常软件中使用的是十六进制颜色码；
#            e.g:
#            白色
#            RGB值：(255,255,255)
#            十进制值：16777215
#            十六进制值：#FFFFFF
# 参数5（1548340494）：unix时间戳，从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数
# 参数6（0）：弹幕池，0普通池，1字幕池，2特殊池 【目前特殊池为高级弹幕专用】
# 参数7（389b20da）：发送者的ID，用于“屏蔽此弹幕的发送者”功能
# 参数8（11114024647262210）：弹幕在弹幕数据库中rowID 用于“历史弹幕”功能。

# 原视频url
urlVid = "https://www.bilibili.com/video/BV18V411z7cV?from=search&seid=7240183341993955226"
# 弹幕cid接口url
url = "https://comment.bilibili.com/218710655.xml"
# 视频总时长：12分23秒
vidDuration = 12 * 60 + 23

# 用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67"
# 获取弹幕页面
resp = requests.get(url=url, headers={"User-Agent": ua})
# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 取出所有d标签中的p属性
contentAll = soup.find_all(name="d")  # type: list[Tag]
bulletInfoAll = [bullet.attrs["p"] for bullet in contentAll]  # type: list[str]

# 取出弹幕发出的秒数
bulletTimeAll = [float(bullet.split(sep=",")[0].strip()) for bullet in bulletInfoAll]  # type: list[float]

# 按每60秒为间隔做一次分箱
seBulletByMins = pandas.cut(x=bulletTimeAll, bins=[x * 60 for x in range((vidDuration // 60 + 1) + 1)],
                            include_lowest=True)
# 分箱计数
seBulletCnt = Series(data=seBulletByMins).value_counts()  # type: Series
# 有序排列索引
seBulletCnt.sort_index(ascending=True, inplace=True)

# 可视化弹幕时间分布
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# x轴数据
x_data = [f"{int(item.left)}-{int(item.right)}" for item in seBulletCnt.index]

# 作图
c = (
    Line()
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="弹幕数",
        y_axis=seBulletCnt.values.tolist()
    )
)

# 渲染
c.render(path=os.path.join(targetPath, "line.html"))

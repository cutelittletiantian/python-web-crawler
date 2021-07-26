import os
from pyecharts.charts import Line
import pyecharts.options as opts

# 原始数据
# A电影的售票数据
y_data_A = [20, 10, 23, 134, 234, 14, 76]
# B电影的售票数据
y_data_B = [125, 82, 25, 62, 45, 74, 156]
# 一周的天数数据
x_data = ["第一天", "第二天", "第三天", "第四天", "第五天", "第六天", "第七天"]

# 绘制折线图
# 一条折线的数据统称为“A电影”，另一条折线的数据统称为“B电影”；
# 将生成的折线图命名为“data.html”
line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(series_name="A电影", y_axis=y_data_A)
    .add_yaxis(series_name="B电影", y_axis=y_data_B)
)

# 保存路径
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)
# 保存图片
line.render(path=os.path.join(targetPath, "data.html"))

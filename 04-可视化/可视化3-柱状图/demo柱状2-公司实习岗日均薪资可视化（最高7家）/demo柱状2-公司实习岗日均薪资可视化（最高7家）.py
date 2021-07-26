from pyecharts.charts import Bar
import os

# 可视化渲染保存路径
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

# 取出文件数据
with open(file="职位数据.txt", mode="r", encoding="utf-8") as fp:
    dataLines = fp.readlines()

# 取出公司（第2列）、薪资（第4列），薪资面议除外
dataRows = [dataLine.strip().split(",") for dataLine in dataLines]
dataRows = [dataItem for dataItem in dataRows if "薪资面议" not in dataItem[3]]

# 取出公司名称
companies = [dataItem[1] for dataItem in dataRows]

# 取出对应薪资
salaries = [dataItem[3] for dataItem in dataRows]
# 计算薪资区间中的平均值
salaries = [dataItem.replace("/天", "") for dataItem in salaries]
salaries = [dataItem.split("-") for dataItem in salaries]
salaries = [(int(dataItem[0]) + int(dataItem[1])) / 2 for dataItem in salaries]

# (公司, 工资)建立映射字典，数据去重
company_salary = list(set(zip(companies, salaries)))

# 按工资进行排序
comp_sa_sorted = sorted(company_salary, key=lambda item: item[1], reverse=True)

# 工资前7高的公司
comp_sa_first7 = comp_sa_sorted[:7]

# 可视化：柱状图
bar = (
    Bar()
    .add_xaxis(xaxis_data=[item[0] for item in comp_sa_first7])
    .add_yaxis(series_name="公司", y_axis=[item[1] for item in comp_sa_first7])
)
bar.render(path=os.path.join(targetPath, "salary.html"))

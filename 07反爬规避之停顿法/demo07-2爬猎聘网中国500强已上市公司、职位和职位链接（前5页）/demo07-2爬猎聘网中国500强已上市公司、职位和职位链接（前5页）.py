import os
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import time

# 猎聘500强url，职位以产品经理为例
url = "https://www.liepin.com/zhaopin/?compkind=&dqs=&pubTime=&pageSize=40&salary=&compTag=180&sortFlag=15" \
      "&degradeFlag=0&compIds=&subIndustry=&jobKind=&industries=&compscale=&key=%E4%BA%A7%E5%93%81%E7%BB%8F%E7%90%86" \
      "&siTag=i9Jq-FcUGTpC9QESjC5G3Q%7EfA9rXquZc5IkJpXC-Ycixw&d_sfrom=search_fp&d_ckId" \
      "=61ea6ea3f6d5f5edca49995a72e6c97b&d_curPage=0&d_pageSize=40&d_headId=61ea6ea3f6d5f5edca49995a72e6c97b&curPage" \
      "={0}"

# 伪装成浏览器的用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 " \
     "Safari/537.36 Edg/91.0.864.59 "

# 职业信息资源
jobItems = []

# 批量爬前5页信息
for page in range(5):
    # 请求资源（前5页）
    resp = requests.get(url=url.format(page), headers={"User-Agent": ua})
    # 防止乱码，统一显示utf-8
    resp.encoding = resp.apparent_encoding
    # 解析响应资源内容
    soup = BeautifulSoup(markup=resp.text, features="lxml")

    # 找职位信息
    jobInfoTags = soup.find_all(name="div", class_="sojob-item-main clearfix")  # type: list[Tag]
    # 取出上市企业的名称和url
    for jobInfoTag in jobInfoTags:
        # 上市则做处理
        if "上市" in jobInfoTag.find(name="p", class_="field-financing").find(name="span").text:
            # 职位公司名称
            firmNameTag = jobInfoTag.find(name="p", class_="company-name")
            firmName = firmNameTag.find(name="a").text
            # 取出职业名称以及相应的链接
            jobNameTag = jobInfoTag.find(name="div", class_="job-info")
            jobName = jobNameTag.find(name="h3").find(name="a").text.strip()
            jobUrl = jobNameTag.find(name="h3").find(name="a").attrs["href"]
            # 寄存
            jobItems.append((firmName, jobName, jobUrl))

    # 间歇2秒重新再请求下一页，防止被反爬拦截
    time.sleep(2)

# 写入文件
resultPath = "result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
with open(file=os.path.join(resultPath, "工作数据.txt"), mode="w") as fp:
    for jobItem in jobItems:
        fp.writelines(",".join(jobItem)+"\n")

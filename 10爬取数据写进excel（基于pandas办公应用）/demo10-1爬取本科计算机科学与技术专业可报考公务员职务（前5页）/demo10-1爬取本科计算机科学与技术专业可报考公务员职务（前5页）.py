import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import pandas
from pandas import DataFrame, Series

# 爬取多页的模板url
urlTemplate = "http://zwsearch.huatu.com/search_el/searchzyk.php?act=zyzycx&param=iPzE5nMlfeMt8rpXP4X4" \
              "%2B8s5i3jr5q31XqYDuQPPQPDQabhcEZH9C7kp8ueJ%2BEGeHcelVibJR7qhjO6%2FU3YWkeaGhYPcUXq3%2BkkB7%2B2" \
              "%2BLbvByizaMIDI%2FOIKEmELCTUD7x%2BYXW%2BbbLyMPPrqVRZ5F98&page={0}"

# 用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/" \
     "537.36 Edg/91.0.864.71"

# cookie
ck = "PHPSESSID=gng2eofd142q28v2njvafa1lmq; " \
     "UM_distinctid=17ac7c9f46058b-0f6b016cf94cc1-7a697f6c-1fa400-17ac7c9f461487; " \
     "CNZZDATA443728=cnzz_eid%3D339542294-1626845635-%26ntime%3D1626845635; " \
     "Hm_lvt_c5b3a7bc9cfb4e1133c856fee205fabd=1626849539; Hm_lvt_4f180beef63b7369b078602c780ef656=1626849539; " \
     "CNZZDATA1253166758=1336719698-1626845670-%7C1626845670; CNZZDATA1262541324=907499393-1626849378-%7C1626849378; " \
     "sajssdk_2015_cross_new_user=1; " \
     "sensorsdata2015jssdkchannel=%7B%22prop%22%3A%7B%22_sa_channel_landing_url%22%3A%22%22%7D%7D; " \
     "cookie_keywords=%25E8%25AE%25A1%25E7%25AE%2597%25E6%259C%25BA; " \
     "sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217ac7c9f5976ff-03d28f229ffdc08-7a697f6c-2073600" \
     "-17ac7c9f599eae%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type" \
     "%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword" \
     "%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24" \
     "latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22http%3A%2F%2Fzwsearch.huatu.com%2Fsearch_el%2F" \
     "searchzyk.php%3Fact%3Dzyzycx%26param%3DiPzE5nMlfeMt8rpXP4X4%252B8s5i3jr5q31XqYDuQPPQPDQabhcEZH9C7kp8ueJ" \
     "%252BEGeHcelVibJR7qhjO6%252FU3YWkeaGhYPcUXq3%252BkkB7%252B2%252BLbvByizaMIDI%252FOI%22%7D%2C%22%24device_id" \
     "%22%3A%2217ac7c9f5976ff-03d28f229ffdc08-7a697f6c-2073600-17ac7c9f599eae%22%7D; randcode=8048; " \
     "Hm_lpvt_4f180beef63b7369b078602c780ef656=1626850327; Hm_lpvt_c5b3a7bc9cfb4e1133c856fee205fabd=1626850327"

# 爬取前5页 地区、部门、用人司局和职位名称（前4列）

# 数据域
tblData = []
for page in range(1, 6):
    # 请求资源
    resp = requests.get(url=urlTemplate.format(page), headers={"User-Agent": ua, "Cookie": ck})
    # 解析资源
    soup = BeautifulSoup(markup=resp.text, features="lxml")
    # 找出表格的数据域
    tblBodyTags = soup.find(name="div", class_="table fsk01").find_all(name="tr")[1:]  # type: list[Tag]
    # 逐个找出数据的前4列
    tblValTags = [tblBodyTag.find_all(name="td")[:4] for tblBodyTag in tblBodyTags]  # type: list[Tag]
    for tblValTag in tblValTags:
        tblData.append([itemTag.text for itemTag in tblValTag])
# 再取出表头
tblHeader = [headerItem.text for headerItem
             in soup.find(name="div", class_="table fsk01").find_all(name="tr")[0].find_all(name="th")[:4]]

# 构造DataFrame
df = pandas.DataFrame(data=tblData, columns=tblHeader)

# 保存路径
targetPath = "公务员职位信息.xlsx"
# 写入excel文档
with pandas.ExcelWriter(path=targetPath, engine="openpyxl", mode="w") as writer:
    df.to_excel(excel_writer=writer, sheet_name="计算机科学与技术")

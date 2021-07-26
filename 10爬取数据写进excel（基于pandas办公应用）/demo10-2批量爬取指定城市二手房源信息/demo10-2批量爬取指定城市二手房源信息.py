import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import pandas as pd
from pandas import DataFrame, Series
import os

# 页面模板，{0}处填写的页面从1开始
urlTempPage = "https://cd.ke.com/ershoufang/pg{0}su1ie2sf1l2p5/"

# 用户代理
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" \
     "91.0.4472.164 Safari/537.36 Edg/91.0.864.71"


def get_preview_urls_of_page(page_: int) -> list[str]:
    """
    获取第page页预览页的所有房子预览信息url

    :param page_: 第page页

    :return: 返回当前页所有的房子的详情页url
    """
    # 请求
    resp_ = requests.get(url=urlTempPage.format(page_), headers={"User-Agent": ua})
    # 解析
    soup_ = BeautifulSoup(markup=resp_.text, features="lxml")
    # 取出当前页房源信息标签
    house_info_tags = \
        soup_.find(name="ul", class_="sellListContent").find_all(name="li", class_="clear")  # type: list[Tag]
    # 取出每一个url
    house_info_urls = [house_info_tag.a["href"] for house_info_tag in house_info_tags]

    return house_info_urls


def get_detail_of_house(url_: str) -> list:
    """
    获取房子的详情信息：

    房子总价/万，单价价格(元/平方)，建筑面积，小区名称，所在区域，房屋户型

    :param url_: 当前房源的详情页url

    :return: [房子总价/万，单价价格(元/平方)，建筑面积，小区名称，所在区域，房屋户型]依次组成的列表
    """
    # 请求
    resp_ = requests.get(url=url_, headers={"User-Agent": ua})
    # 解析
    soup_ = BeautifulSoup(markup=resp_.text, features="lxml")

    # 取出预览信息
    overview_content = soup_.find(name="div", class_="overview").find(name="div", class_="content")

    # 房子总价/万
    total_price = overview_content.find(name="span", class_="total").text
    # 单价价格(元/平方)
    unit_price = overview_content.find(name="span", class_="unitPriceValue").text
    # 建筑面积
    area = overview_content.find(name="div", class_="area").find(name="div", class_="mainInfo").text
    # 小区名称
    community_name = overview_content \
        .find(name="div", class_="communityName") \
        .find(name="a", class_="info no_resblock_a").text
    # 所在区域
    area_name = overview_content.find(name="div", class_="areaName").find(name="span", class_="info").a.text

    # 取出房源基本信息-基本属性介绍
    intro_content_tags = soup_.find(name="div", class_="introContent") \
        .find(name="div", class_="content").ul.find_all(name="li")  # type: list[Tag]

    # 房屋户型
    house_type = ""
    for intro_content_tag in intro_content_tags:
        if intro_content_tag.find(name="span", class_="label").text == "房屋户型":
            house_type = intro_content_tag.contents[1]
            break

    # 返回房源信息的完整版
    return [total_price, unit_price, area, community_name, area_name, house_type]


# 表头
tblHeader = ["房子总价/万", "单价价格(元/平方)", "建筑面积", "小区名称", "所在区域", "房屋户型"]
# 数据域
tblValues = []
# 详情页url集合
urlDetails = []

# 批量爬第1~5页详情url
for page in range(1, 6):
    urlDetails.extend(get_preview_urls_of_page(page_=page))

# 逐页爬取详情信息
for urlDetail in urlDetails:
    tblValues.append(get_detail_of_house(url_=urlDetail))

# 构造DataFrame
df = pd.DataFrame(columns=tblHeader, data=tblValues)

# 写入excel
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)
targetName = "二手房.xlsx"
with pd.ExcelWriter(path=os.path.join(targetPath, targetName), engine="openpyxl", mode="w") as writer:
    df.to_excel(excel_writer=writer, sheet_name="成都")

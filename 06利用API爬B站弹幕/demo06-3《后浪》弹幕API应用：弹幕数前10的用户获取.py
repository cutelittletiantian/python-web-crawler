from collections import Counter
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

# 《后浪》视频url
vidUrl = "https://www.bilibili.com/video/av412935552/"

# 弹幕cid（通过视频url打开审查元素寻找）
cid = "186803402"
# 弹幕接口
bulletApi = "https://comment.bilibili.com/{0}.xml"

# 伪装浏览器（用户代理）
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 " \
     "Safari/537.36 Edg/91.0.864.67 "

# 请求弹幕接口
resp = requests.get(url=bulletApi.format(cid), headers={"User-Agent": ua})
# 统一前后台的编码，防止乱码
resp.encoding = resp.apparent_encoding

# 解析
soup = BeautifulSoup(markup=resp.text, features="lxml")

# 取出弹幕标签
bulletAll = soup.find_all(name="d")  # type: list[Tag]

'''【B站弹幕接口p属性含义】
<d p="157.47900,1,25,16777215,1548340494,0,389b20da,11114024647262210">啧啧，原来阿卡丽那么小？</d>
参数1（157.47900）：弹幕出现的时间，以秒数为单位
参数2（1）：弹幕的模式，1-3 滚动弹幕，4 底端弹幕，5顶端弹幕，6 逆向弹幕，7 精准定位，8 高级弹幕
参数3（25）：字号 （12非常小，16特小，18小，25中，36大，45很大，64特别大）
参数4（16777215）：字体的颜色；这串数字是十进制表示；通常软件中使用的是十六进制颜色码；
           e.g:
           白色   
           RGB值：(255,255,255)     
           十进制值：16777215      
           十六进制值：#FFFFFF
参数5（1548340494）：unix时间戳，从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数
参数6（0）：弹幕池，0普通池，1字幕池，2特殊池 【目前特殊池为高级弹幕专用】
参数7（389b20da）：发送者的ID，用于“屏蔽此弹幕的发送者”功能
参数8（11114024647262210）：弹幕在弹幕数据库中rowID 用于“历史弹幕”功能。
'''

# 剥去标签，取出属性p中的第7个参数
bulletUsers = [bullet["p"].split(sep=",")[6] for bullet in bulletAll]

# 统计弹幕发送数Top10用户
bulletUsersCount = Counter(bulletUsers).most_common(10)

print(bulletUsersCount)

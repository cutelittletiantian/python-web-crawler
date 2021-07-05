import jieba

# 需要分词的字符串列表
contentList = ["肖邦在波兰被视为神童，1816年6岁的时候开始正式学习钢琴",
               "第一位老师是沃伊切赫•日维尼本身是一位画家、小提琴家",
               "他的姐姐路德维卡也和他一起学琴",
               "肖邦是个音乐天才，从小就展现出他惊人的音乐天赋，7岁时便能公开演奏",
               "他的第一首作品G小调和降B大调波兰舞曲创作于1817年，体现出肖邦不同寻常的即兴创作能力",
               "他在华沙获誉为“莫扎特的继承人”、“第二个莫扎特”。"]

# 分词
sentenceList = []
for content in contentList:
    wordList = jieba.lcut(content)
    sentenceList.extend(wordList)
    print(wordList)

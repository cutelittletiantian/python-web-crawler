import jieba
# 需要分词的字符串列表
sentenceList = ["小王子是一个超凡脱俗的仙童，他住在一颗只比他大一丁点儿的小行星上。",
                "陪伴他的是一朵他非常喜爱的小玫瑰花，但玫瑰花的虚荣心伤害了小王子对她的感情。",
                "小王子告别小行星，开始了遨游太空的旅行。",
                "他先后访问了六个行星，各种见闻使他陷入忧伤，他感到大人们荒唐可笑、太不正常。",
                "只有在其中一个点灯人的星球上，小王子才找到一个可以作为朋友的人。",
                "但点灯人的天地又十分狭小，除了点灯人他自己，不能容下第二个人。",
                "在地理学家的指点下，孤单的小王子来到人类居住的地球。"]

# 分词
wordList = []
for sentence in sentenceList:
    wordList.extend(jieba.lcut(sentence))

for word in wordList[:]:
    if len(word) <= 1:
        wordList.remove(word)

for word in wordList:
    print(word)

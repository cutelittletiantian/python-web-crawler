# demo01-1：URL翻前500页，每50页选中一次
for pn in range(0, 501, 50):
    print(f"https://tieba.baidu.com/f?kw=%E7%8C%AB&ie=utf-8&pn={pn}")

import os

# 目标路径
targetPath = "result"
if not os.path.exists(path=targetPath):
    os.mkdir(path=targetPath)

with open(file="name_list.txt", mode="r", encoding="utf-8") as fpNameList:
    studentNames = fpNameList.read().split(sep="\n")[:500]

with open(file=os.path.join(targetPath, "visitNames.txt"), mode="w", encoding="utf-8") as fpVisit:
    fpVisit.write("\n".join(studentNames))

# 输出观察
# with open(file="visitNames.txt", mode="r") as fpVisit:
#     print(fpVisit.read())

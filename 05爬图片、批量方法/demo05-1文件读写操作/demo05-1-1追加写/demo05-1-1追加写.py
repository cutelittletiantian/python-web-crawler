# 假设文件末尾追加一个"音乐之声"
with open(file="films.txt", mode="a", encoding="utf-8") as fpMovies:
    fpMovies.write("音乐之声\n")

# 输出
with open(file="films.txt", mode="r", encoding="utf-8") as fpMovies:
    movies = fpMovies.read()

print(movies)
# 输出每行为一个列表的情况
# print(movies.split("\n"))

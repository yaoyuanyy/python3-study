# 读取文件练习
# -- 读取配置文件
fpath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io/data.properties"
with open(fpath, "r", encoding="utf-8") as f:
    for readline in f.readlines():
        # 把末尾的"\n" 删掉
        print(readline.strip())


# 写入文件
with open(fpath, "t+a") as f:
    f.writelines("\nheight=10")



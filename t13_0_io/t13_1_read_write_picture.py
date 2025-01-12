# 读取一个图片，写入另一个图片

readFpath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io/python_img_1.png"
writeFpath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io/python_img_1.bak.png"

with open(writeFpath, 'wb') as writeF:
    with open(readFpath, "rb") as readF:
        bData = readF.read()
        print("len", bData)
        writeF.write(bData)



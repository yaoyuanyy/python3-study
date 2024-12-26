import imageio.v3 as imageio

# 对系统的变量和目录&文件进行操作

readFpath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io/python_img_1.png"
writeFpath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io/python_img_1_2.bak.png"

img = imageio.imread(readFpath)

imageio.imwrite(writeFpath, img)




# refer to https://www.geeksforgeeks.org/reading-images-in-python/
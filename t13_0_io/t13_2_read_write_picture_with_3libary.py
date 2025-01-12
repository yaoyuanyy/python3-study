import imageio.v3 as imageio

# 读取一个图片，写入另一个图片 使用第三库

readFpath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io/python_img_1.png"
writeFpath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io/python_img_1_2.bak.png"

img = imageio.imread(readFpath)

imageio.imwrite(writeFpath, img)




# refer to https://www.geeksforgeeks.org/reading-images-in-python/
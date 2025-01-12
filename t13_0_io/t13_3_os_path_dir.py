import os

# 系统信息
print("当前系统为", os.name)
print("当前系统详细信息", os.uname())


# 环境变量信息
print("系统环境变量", os.environ)
print("系统环境变量中的path", os.environ.get("PATH"))
print("系统环境变量中的path", os.environ.get("HOME"))


# 目录和文件信息
print("查看当前目录的绝对路径", os.path.abspath("."))
print("当前目录下创建一个新的路径test")
newDir = os.path.join(os.path.abspath("."), "new_test")
# 创建new_test新目录
if not os.path.exists(newDir):
    print("文件不存在，创建新的", newDir)
    os.mkdir(newDir)

# 删除new_test目录
# os.rmdir(newDir)

# 目录操作
## 1. 文件目录拆分
filePath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io/test.md"
# Tips splitxxx 方法返回一个tuple 元组：3-item tuple (drive, root, tail)
print("拆分后获取root目录", os.path.splitroot(filePath))
print("拆分后获取最后级别的文件/目录", os.path.split(filePath))
splitExt = os.path.splitext(filePath)
print("拆分后获取文件扩展名", splitExt[1])
print("拆分后获取xxx", os.path.splitdrive(filePath))


## 一行代码过去指定目录下的指定文件
curPath = "/Users/skyler/Documents/projects-pycharm/python3-study/t7_0_io"
print(curPath)
for x in os.listdir(curPath):
    if os.path.isfile(x) and os.path.splitext(x)[1] == '.py':
        print("当前文件", x)


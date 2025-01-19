# 获取系统信息的模块
# refer to https://liaoxuefeng.com/books/python/third-party-modules/psutil/index.html
# psutil官网：https://github.com/giampaolo/psutil
# psutil: https://hellowac.github.io/psutil-doc-zh/processes/process_class/cpu_percent.html


import psutil

# cpu信息
## 获取cpu信息
print("cpu逻辑核心", psutil.cpu_count())
print("cpu物理核心", psutil.cpu_count(logical=False))


# 统计cpu的用户/系统/空闲时间
print("cpu times", psutil.cpu_times(percpu=True))

# 统计cpu使用率，每秒刷新一次，累计10次
for x in range(10):
    print("cpu times", psutil.cpu_percent(interval=1, percpu=True))


# 内存信息

##


# 进程信息
##


# 磁盘信息
##


# 网络信息
##


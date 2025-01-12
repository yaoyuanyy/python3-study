# 使用子进程调用外部命令
# https://liaoxuefeng.com/books/python/process-thread/process/index.html

import subprocess


print("exec ls -l")
subprocess.run("ls -l", shell=True)

print("exec $ nslookup www.python.org")
result = subprocess.call(["nslookup", "www.python.org"])
print(result)

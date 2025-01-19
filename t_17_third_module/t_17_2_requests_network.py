# 网络请求
# refer to https://liaoxuefeng.com/books/python/third-party-modules/requests/index.html

import requests


# 不加header，结果返回的是418
header = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}

r = requests.get("https://www.douban.com", headers=header)
print(r)
print(r.status_code)
# print(r.text)
# print(r.content)

 # 请求带参数的
header = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
params = {"q":"python", "cat":"1001"}
r_param = requests.get("https://www.douban.com", params=params)
print(r_param.url)

from datetime import datetime as my_datetime, date


now = my_datetime.now()
print("当前时间:", now)


dt = my_datetime(2020, 5, 20, 11, 30)
print("构建的时间为:", dt)

strDt = dt.strftime("%Y-%m-%d %H:%M:%S")
print("strDt:", strDt)

newDt = my_datetime.strptime("2020-05-20 11:30:00", "%Y-%m-%d %H:%M:%S")
print("newDt:", newDt)

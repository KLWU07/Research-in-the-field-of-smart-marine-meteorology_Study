import pygrib
# 打开GRIB文件
grbs = pygrib.open('_mars-bol-webmars-public-svc-blue-003-2.grib')

# 遍历文件中的所有GRIB消息
for grb in grbs:
    print(grb)

# 关闭文件
grbs.close()
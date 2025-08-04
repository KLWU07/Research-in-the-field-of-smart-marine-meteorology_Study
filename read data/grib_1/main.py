import pygrib
# 打开GRIB文件
grbs = pygrib.open('A7D05011200050406001-HRES-single-level')

# 遍历文件中的所有GRIB消息
for grb in grbs:
    print(grb)

# 关闭文件
grbs.close()
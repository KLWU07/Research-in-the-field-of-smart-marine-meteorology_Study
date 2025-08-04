import pygrib
import numpy as np

# 打开GRIB文件
grbs = pygrib.open('A5F050100000515-ENS-extended-single-level')

grb1 =grbs[1] # 第1个变量
grb11 = grb1.keys() # 第1个变量里，键变量名
print(grb11) # 输出变量键变量名
print(len(grb11)) # 输出统计变量数量
print(type(grb11)) # 输出grb11类型

array = grb1.values

#
# lats, lons = grb1.latlons()   # 提取经纬坐标
# print(lats)

# np.savetxt( "a.csv", array, delimiter="," )

# 关闭文件
grbs.close()
import pygrib
import numpy as np

# 打开GRIB文件
grbs = pygrib.open('A5F050100000515-ENS-extended-single-level')
# 选择特定的GRIB消息（例如：）条件筛选
U_grb = grbs.select(name='Volumetric soil water layer 1',startStep = 342,endStep =342)[0]
# 获取数据
U_data = U_grb.values

# 获取数据的地理坐标
lats, lons = U_grb.latlons() # 注意：这个方法返回的是两个数组，分别代表纬度和经度

# 打印部分数据以验证
# print(U_data) # 输出数据
print("u Data Shape:", U_data.shape) # 获取数组或矩阵的维度信息
print("Latitude Range:", np.min(lats), np.max(lats)) # 纬度最小值和经度最大值
print("Longitude Range:", np.min(lons), np.max(lons)) # 经度最小值和经度最大值

# print(lats)
# print(lons)
# 关闭文件
grbs.close()

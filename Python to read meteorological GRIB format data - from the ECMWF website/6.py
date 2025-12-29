import pygrib
import numpy as np
from tqdm import tqdm

# 定义要读取的GRIB文件路径
file_path = '_mars-bol-webmars-public-svc-blue-003-2.grib'

# 使用pygrib打开GRIB文件
grbs = pygrib.open(file_path)

# 创建一个空的字典来存储数据
data_dict = {}
timestamps = []

# 创建一个空的三维数组，用于存储数据
data_array = np.empty((205, 253, 5989))

# 获取消息记录总数
num_records = grbs.messages

# 读取每个消息记录
for i, grb in enumerate(tqdm(grbs, total=num_records, desc='Updating Data')):
    name = grb.name

    # 提取数据和经纬度
    data, lats, lons = grb.data(lat1=3, lat2=54, lon1=73, lon2=136)

    # 获取有效时间
    validity_date = grb.validityDate
    validity_time = grb.validityTime
    timestamp = f"{validity_date} {validity_time}"
    timestamps.append(timestamp)

    # 将数据存储为NumPy数组
    data_array[:, :, i] = data

# 保存data_array为npz文件
data_dict = {
    'data_array': data_array,
    'timestamps': timestamps
}
np.savez('data_array.npz', **data_dict)
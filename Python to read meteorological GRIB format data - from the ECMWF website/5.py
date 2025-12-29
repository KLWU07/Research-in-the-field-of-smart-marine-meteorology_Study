import pandas as pd
import xarray as xr

# pycharm运行不了，只能命令行操作
# 读取GRIB文件
grib_file = 'A4E05011200050406001-ENS-model-level.grib2'

datasets = cfgrib.open_datasets(grib_file)

# 遍历所有数据集，并分别保存每个变量
for idx, ds in enumerate(datasets):
    df = ds.to_dataframe().reset_index()
    # 保存每个变量对应的DataFrame
    df.to_csv(f'data_{idx}.csv', index=False)# 文件后缀不一样
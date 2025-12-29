import cfgrib
import pandas as pd
import xarray as xr
# 另一种方法读取数据
# pycharm运行不了，只能命令行操作
# 读取GRIB文件
grib_file = 'A5F050100000515-ENS-extended-single-level'

datasets = cfgrib.open_datasets(grib_file)

# 遍历所有数据集，并分别保存每个变量
for idx, ds in enumerate(datasets):
    df = ds.to_dataframe().reset_index()
    # 保存每个变量对应的DataFrame
    df.to_csv(f'1data_{idx}.csv', index=False)# 文件后缀不一样
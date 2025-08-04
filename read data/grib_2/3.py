import pygrib

# 打开GRIB文件
grib_file_path = 'A5F050100000515-ENS-extended-single-level'
grbs = pygrib.open(grib_file_path)

# 遍历文件中的消息
for grb in grbs:
    # 打印消息的一些基本信息
    print(f"1参数名称: {grb.parameterName}")  # 参数名称，表示数据集中包含的气象参数，如温度、湿度、风速等。
    print(f"2单位: {grb.units}")  # 参数的单位
    print(f"3数据集生成日期: {grb.dataDate}")  # 数据日期，表示数据集生成或引用的日期。
    print(f"4日期 年: {grb.year}")
    print(f"5日期 月: {grb.month}")
    print(f"6日期 日: {grb.day}")
    print(f"7小时: {grb.dataTime}")  # 数据时间，表示数据集生成或引用的具体时间（小时、分钟等）
    print(f"8时间: {grb.time}")
    print(f"9获取时间小时: {grb.hour}")  # 获取时间小时
    print(f"10**: {grb.julianDay}")  # 儒略日，一年中的第几天（从1到365或366），用于提供一种独立于月份和日期的时间表示方法。
    print(f"11: {grb.indicatorOfTypeOfLevel}")  # 级别类型指示符，用于指示数据所在的垂直级别类型（如地面、特定气压层、特定高度层等）。
    print(f"12: {grb.level}")  # 级别值，表示数据所在的垂直级别的具体数值（如地面为0、1000hPa、850hPa等）
    print(f"13: {grb.pressureUnits}")  # 气压单位，如果数据集是在特定气压层上，则此字段表示该气压层的单位（通常是帕斯卡Pa）
    print('1----------------------------------------------------------------------------------------------------1')
    print(f"14: {grb.stepType}")  # 步长类型，表示数据集的时间步长是如何定义的（如累积、瞬时、平均等）。instant表示某个瞬间的数据或观测值；accumulated”（累积）数据
    print(f"15: {grb.stepUnits}")  # 步长单位，如果数据集表示一个预测或模拟的时间步长，则此字段表示该步长的单位（如小时、天等）。
    print(f"16: {grb.unitOfTimeRange}")  # 时间范围单位，如果数据集表示一个时间范围（如小时预报），则此字段表示该时间范围的单位（如小时、天等）。
    print(f"17: {grb.startStep}")  # 开始步长，如果数据集表示一个时间范围内的多个步长，则此字段可能表示第一个步长的值。
    print(f"18: {grb.endStep}")  # 结束步长，与startStep类似，但表示最后一个步长的值。
    print(f"19: {grb.stepRange}")  # 步长范围，可能表示预测或模拟的时间步长的开始和结束值（取决于stepType）
    print('2----------------------------------------------------------------------------------------------------2')
    print(f"20有效性日期: {grb.validityDate}")  # 有效性日期，表示数据集的时间范围或预测的开始日期。
    print(f"21有效性时间: {grb.validityTime}")  # 有效性时间，与validityDate结合使用，表示数据集的时间范围或预测的开始时间。
    print(f"22经纬度网格: {grb.gridType}")  # 经纬度网格（latitude-longitude grid）进行规则分布的数据。regular_ll这里的 "ll" 代表经纬度（latitude-longitude）的缩写
    print(f"23纬度范围: {grb.latlons()[0]}")  # 纬度范围，注意：.latlons()这个方法返回的是两个数组，分别代表纬度和经度
    print(f"24经度范围: {grb.latlons()[1]}")  # 经度范围
    print(f"25纬度: {grb.latitudes}")  # 纬度
    print(f"26经度: {grb.longitudes}")  # 经度
    print(f"27参数值: {grb.values }")  # 数据集中包含的实际数值
    print('******************************************************************')

# 关闭GRIB文件
grbs.close()


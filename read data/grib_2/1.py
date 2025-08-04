import pygrib
# 打开GRIB文件
grbs = pygrib.open('A5F050100000515-ENS-extended-single-level')

# 遍历文件中的所有GRIB消息,所有变量信息
for grb in grbs:
    print(grb)

# 关闭文件
grbs.close()

# 信息解读:1:Total precipitation:m (instant):regular_ll:surface:level 0:fcst time 336 hrs:from 202405010000
# 1 :数据列表的行号，有的文件可能包括多个数据
# Total precipitation:数据的名称，啥名称中文不知道在ecmwf.int/en/forecasts/datasets网站查，这里是总降水量，指的是某一时间段内，降水（如雨、雪等）在某一地区内积累的总量
# m (instant):数据的单位，这里的“m”可能代表降水量的度量单位，即毫米（millimeter）。而“(instant)”则可能表示这是一个瞬时降水量的预报，即预报的是某一具体时刻的降水量，而非一段时间内的平均降水量或累计降水量。
# regular_ll:常规数据，常规预报，而非特殊或紧急情况下的预报。
# surface:这里的“surface”可能指的是地面，表示预报的是地面上的降水量，单层没有气压层
# depthBelowLandLayer”理解为某个点或层在陆地表层以下的垂直距离
# isobaricInhPa:这个字段表示的是数据属性，此处表示是以hPa为单位的等压面
# level 0:这个字段表示的是高度层
# fcst time 336 hrs :预报时效，这里的“fcst”是forecast（预报）的缩写，而“336 hrs”表示预报的时间范围是336小时之后。换句话说，这是一个对未来336小时（约14天）后的降水量预报。
# from 202405010000 :起报时间，这个部分表示预报的起始时间，即2024年5月1日00时00分。这意味着预报的是从2024年5月1日00时00分开始，未来336小时（约14天）后的降水量情况。

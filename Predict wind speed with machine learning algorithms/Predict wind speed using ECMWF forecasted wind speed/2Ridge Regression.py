# 岭回归
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge  # 导入岭回归模型
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import matplotlib as mpl

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体，Windows
# plt.rcParams['font.sans-serif'] = ['Heiti TC']  # 黑体-繁，Mac
# plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # 文泉驿正黑，Linux

# 解决负号显示问题
plt.rcParams['axes.unicode_minus'] = False

# 1. 加载数据
data1 = pd.read_csv(r'data1.csv')

# 2. 确保 date_time 列是 datetime 类型
data1['date_time'] = pd.to_datetime(data1['date_time'], format='%Y/%m/%d %H:%M')

# 3. 定义时间范围并筛选数据
start_time = '2023-05-02 00:00:00'
end_time = '2024-06-30 18:00:00'
data1 = data1[(data1['date_time'] >= start_time) & (data1['date_time'] <= end_time)]

# 4. 按时间排序
data1 = data1.sort_values('date_time').reset_index(drop=True)

# 5. 提取特征和目标列
X = data1[['ecmwf_wind']]  # 特征列
y = data1['wind_obs']  # 目标列

# 6. 按具体时间段划分数据集
train_start = '2023-05-02 00:00:00'
train_end = '2024-04-30 18:00:00'
test_start = '2024-05-01 00:00:00'
test_end = '2024-06-30 18:00:00'

# 训练集索引
train_mask = (data1['date_time'] >= train_start) & (data1['date_time'] <= train_end)
# 测试集索引
test_mask = (data1['date_time'] >= test_start) & (data1['date_time'] <= test_end)

# 划分数据集
X_train, X_test = X[train_mask], X[test_mask]
y_train, y_test = y[train_mask], y[test_mask]

# 获取测试集对应的时间用于可视化
test_dates = data1['date_time'][test_mask]

# 7. 数据归一化（最大最小归一化）
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 8. 训练岭回归模型
# alpha为正则化参数，值越大正则化强度越高，可根据需要调整
model = Ridge(alpha=1.0)  # 可尝试不同的alpha值如0.1, 1, 10等
model.fit(X_train_scaled, y_train)

# 输出模型系数
print(f"岭回归系数: {model.coef_}")
print(f"岭回归截距: {model.intercept_}")

# 9. 预测
y_pred = model.predict(X_test_scaled)

# 10. 计算评价指标
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mbe = np.mean(y_test - y_pred)  # 平均偏差误差
r2 = r2_score(y_test, y_pred)

# 11. 输出评价指标
print(f"训练集样本量: {len(X_train)}")
print(f"测试集样本量: {len(X_test)}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"MBE: {mbe:.4f}")
print(f"R²: {r2:.4f}")

# 12. 预测值与观测值对比可视化（带时间维度）
plt.figure(figsize=(12, 6))
plt.plot(test_dates, y_test, label='观测风速', alpha=0.7)
plt.plot(test_dates, y_pred, label='预测风速', linestyle='--')
plt.xlabel('时间')
plt.ylabel('风速')
plt.title('测试集风速预测对比（岭回归）')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 13. 散点图可视化（预测值 vs 观测值）
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, label='预测值 vs 观测值')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='理想线')
plt.xlabel('观测风速')
plt.ylabel('预测风速')
plt.title('观测值与预测值对比（岭回归）')
plt.legend()
plt.grid(True)
plt.show()


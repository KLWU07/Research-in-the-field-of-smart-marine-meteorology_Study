# 代码在整体流程上是合理的，但针对时间序列数据，存在一个关键问题：使用train_test_split进行随机划分是不合适的。使用1.1linear regression代码训练
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# 1. 加载数据
data1 = pd.read_csv(r'data.csv')

# 2. 确保 date_time 列是 datetime 类型
data1['date_time'] = pd.to_datetime(data1['date_time'], format='%Y/%m/%d %H:%M')

# 3. 定义时间范围并筛选数据
start_time = '2023-07-01 00:00:00'
end_time = '2024-06-30 18:00:00'
data1 = data1[(data1['date_time'] >= start_time) & (data1['date_time'] <= end_time)]

# 4. 提取特征和目标列
X = data1[['ecmwf_wind']]  # 特征列
y = data1['wind_obs']  # 目标列

# 5. 数据集划分（训练集和测试集）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 6. 数据归一化（最大最小归一化）
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 7. 训练简单线性回归模型
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# 8. 预测
y_pred = model.predict(X_test_scaled)

# 9. 计算评价指标
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
mbe = np.mean(y_test - y_pred)  # 平均偏差误差
r2 = r2_score(y_test, y_pred)

# 10. 输出评价指标
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"MBE: {mbe:.4f}")
print(f"R²: {r2:.4f}")

# 11. 数据可视化
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, label='Predicted vs Observed')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', label='Ideal Line')
plt.xlabel('Observed Wind Speed')
plt.ylabel('Predicted Wind Speed')
plt.title('Observed vs Predicted Wind Speed')
plt.legend()
plt.grid(True)
plt.show()
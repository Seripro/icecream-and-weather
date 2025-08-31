import pandas as pd

# ファイルの読み込み
file_path = 'ta_ice.xlsx'
data = pd.read_excel(file_path)


import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

import numpy as np
from sklearn.linear_model import LinearRegression

# 説明変数と目的変数
X = data['月平均気温'].values.reshape(-1, 1)
y = data['アイスクリーム支出金額'].values

# 回帰モデルの作成と学習
model = LinearRegression()
model.fit(X, y)

# 回帰係数と切片
slope = model.coef_[0]
intercept = model.intercept_

# 回帰直線の計算
x_range = np.linspace(X.min(), X.max(), 100)
y_range = slope * x_range + intercept

# 散布図と回帰直線のプロット
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['月平均気温'], y=data['アイスクリーム支出金額'], label='data point')
plt.plot(x_range, y_range, color='red', label='regression line')
plt.title('Scatterplot and regression line of Average monthly temperature and Amount of Ice Cream Spending')
plt.xlabel('Average monthly temperature (℃)')
plt.ylabel('Amount of Ice Cream Spending (Yen)')
plt.legend()
plt.grid(True)
plt.show()

# 回帰式
slope, intercept
import numpy as np

# 주어진 데이터
x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([35, 50, 45, 64, 66, 70])

# 상관계수 계산
correlation_coefficient = np.corrcoef(x, y)[0, 1]

기울기 = correlation_coefficient * (np.std(y)/np.std(x))
절편 = np.mean(y) - 기울기 * np.mean(x)
print("기울기:", 기울기.round(2))
print("절편:", 절편.round(2))
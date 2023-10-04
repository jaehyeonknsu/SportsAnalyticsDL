import numpy as np

# 주어진 데이터
x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([35, 50, 45, 64, 66, 70])

# 상관계수 계산
correlation_coefficient = np.corrcoef(x, y)[0, 1]
# 결정계수 계산
correlation_coefficient2 = correlation_coefficient**2

print("상관계수:", correlation_coefficient.round(2))
print("결정계수:", correlation_coefficient2.round(2))
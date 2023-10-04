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

# x값 입력 받음
x_input = float(input("훈련시간을 입력하세요: "))

#x값에 대한 y값 추정
y_estimate = 기울기 * x_input + 절편

print(f"훈련시간 {x_input}시간에 대한 추정 경기력는?: {y_estimate:.2f}입니다")
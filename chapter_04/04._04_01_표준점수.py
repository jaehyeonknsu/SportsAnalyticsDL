# 필요한 라이브러리 불러오기
import numpy as np

# 주어진 데이터
data = [85, 90, 88, 92, 78, 95, 89, 70, 75, 82]

# 데이터의 평균과 표준편차 계산
mean = np.mean(data)
std_dev = np.std(data)

# 각 데이터 값에 대한 표준점수 계산 및 출력
z_scores = [(value - mean) / std_dev for value in data]
print('평균:', mean)
print('표준편차:', std_dev)
print('표준점수:', z_scores)
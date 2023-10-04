import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 주어진 데이터
x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([35, 50, 45, 64, 66, 70])

# 상관계수 계산
correlation_coefficient = np.corrcoef(x, y)[0, 1]

기울기 = correlation_coefficient * (np.std(y)/np.std(x))
절편 = np.mean(y) - 기울기 * np.mean(x)
print("기울기:", 기울기.round(2))
print("절편:", 절편.round(2))

# 한글 폰트 설정 (gulim 폰트 사용)
font_path = "C:/Windows/Fonts/gulim.ttc"  # gulim 폰트 파일 경로로 수정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 회귀선 그리기
x_range = np.linspace(min(x), max(x), 100)
y_pred = 기울기 * x_range + 절편

plt.scatter(x, y, color='blue', label='실제 데이터')
plt.plot(x_range, y_pred, color='red', label='회귀선')
plt.xlabel('훈련시간')
plt.ylabel('경기력')
plt.legend()
plt.show()

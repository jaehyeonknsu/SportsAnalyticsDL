import numpy as np
import matplotlib.pyplot as plt

# 주어진 데이터
x = np.array([3, 4, 5, 6, 7, 8])
y = np.array([35, 50, 45, 64, 66, 70])
from matplotlib import font_manager, rc

# 상관계수 계산
correlation_coefficient = np.corrcoef(x, y)[0, 1]
print("상관계수:", correlation_coefficient.round(2))

# 한글 폰트 설정 (gulim 폰트 사용)
font_path = "C:/Windows/Fonts/gulim.ttc"  # gulim 폰트 파일 경로로 수정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 산포도 그리기
plt.scatter(x, y, color='blue')
plt.xlabel('훈련시간')
plt.ylabel('경기력')
plt.title('산포도')
plt.grid(True)
plt.show()
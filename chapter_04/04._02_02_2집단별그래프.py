import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 파일 경로 설정
file_path = "chapter_04\Athletes.csv"
# CSV 파일 읽기
data = pd.read_csv(file_path)

# 소숫점 한자리 나타내기
summary_by_sport = data.groupby('Sport')['Height'].agg(['count', 'mean'])
summary_by_sport['mean'] = summary_by_sport['mean'].round(1)

# 한글 폰트 설정 (gulim 폰트 사용)
font_path = "C:/Windows/Fonts/gulim.ttc"  # gulim 폰트 파일 경로로 수정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 그래프 그리기
plt.figure(figsize=(10, 6))
summary_by_sport['mean'].plot(kind='bar', color='blue', label='평균 키')
plt.ylabel('평균 키 (cm)')
plt.title('스포츠별 평균 키')
plt.legend()
plt.xticks(rotation=45)
plt.show()

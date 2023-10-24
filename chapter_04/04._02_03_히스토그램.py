import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 파일 경로 설정
file_path = "chapter_04/Athletes.csv"

# CSV 파일 읽기
data = pd.read_csv(file_path)

# 한글 폰트 설정 (gulim 폰트 사용)
font_path = "C:/Windows/Fonts/gulim.ttc"  # gulim 폰트 파일 경로로 수정
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 'Total Pay'의 분포를 히스토그램으로 그리기
plt.figure(figsize=(10, 6))
plt.hist(data['Total Pay'], bins=20, color='skyblue', edgecolor='black')
plt.title("Total Pay 분포")
plt.xlabel("Total Pay")
plt.ylabel("빈도")
plt.grid(True)
plt.show()
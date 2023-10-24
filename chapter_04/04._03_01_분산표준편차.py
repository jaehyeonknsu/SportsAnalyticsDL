import pandas as pd

# 파일 경로 설정
file_path = "chapter_04/Athletes.csv"

# CSV 파일 읽기
data = pd.read_csv(file_path)

# 'Height' 분산 계산
height_variance = data['Height'].var().round(1)
height_std = data['Height'].std().round(1)

print("Height 분산:", height_variance)
print("Height 표준편차:", height_std)
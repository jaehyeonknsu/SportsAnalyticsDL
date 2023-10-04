import pandas as pd

# 파일 경로 설정
file_path = "chapter_04\Athletes.csv"

# CSV 파일 읽기
data = pd.read_csv(file_path)

# 'Height' 변이계수 계산
height_cv = (data['Height'].std() / data['Height'].mean()) * 100

print("Height 변이계수:", round(height_cv, 1), "%")
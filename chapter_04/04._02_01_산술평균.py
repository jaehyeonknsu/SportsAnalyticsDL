import pandas as pd

# 파일 경로 설정
file_path = "chapter_04/Athletes.csv"
# CSV 파일 읽기
data = pd.read_csv(file_path)
print(data.head(0))
      
# 'Height'의 산술평균 계산
average_height = data['Height'].mean()
print("신장의 산술평균: ", average_height, "cm")
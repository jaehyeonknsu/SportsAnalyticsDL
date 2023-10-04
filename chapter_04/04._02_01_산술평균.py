import pandas as pd

# 파일 경로 설정
file_path = "C:/Users/USER/Dropbox/내 PC (DESKTOP-R99G944)/Desktop/AI스포츠_교재_집필/data_set/Athletes.csv"
# CSV 파일 읽기
data = pd.read_csv(file_path)
print(data.head(0))
      
# 'Height'의 산술평균 계산
average_height = data['Height'].mean()
print("신장의 산술평균: ", average_height, "cm")
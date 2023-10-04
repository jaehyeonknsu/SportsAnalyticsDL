import pandas as pd

# 파일 경로 설정
file_path = "chapter_04\Athletes.csv"
# CSV 파일 읽기
data = pd.read_csv(file_path)

# 'Sports' 집단별 산술평균, 사례수
summary_by_sport = data.groupby('Sport')['Height'].agg(['count', 'mean'])

# 소숫점 한자리 나타내기
summary_by_sport['mean'] = summary_by_sport['mean'].round(1)
print(summary_by_sport)
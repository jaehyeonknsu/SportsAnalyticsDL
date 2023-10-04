import pandas as pd
import scipy.stats

# 파일 경로 설정
file_path = "chapter_04\Athletes.csv"
# CSV 파일 읽기
data = pd.read_csv(file_path)

# 'Total Pay'의 산술평균 계산
average_pay = data['Total Pay'].mean()
print("연봉의 산술평균: $", average_pay)

# 'Total Pay'의 중앙값 계산
median_pay = data['Total Pay'].median()
print("연봉의 중앙값  : $", median_pay)

# 'Total Pay'의 기하평균 계산
geometric_mean_pay = scipy.stats.gmean(data['Total Pay']).round(1)
print("연봉의 기하평균: $", geometric_mean_pay)

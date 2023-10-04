import numpy as np

# 두 행렬 정의
matrix_A = np.array([2, 3, 4])
matrix_B = np.array([[4, 1], [3, 2], [2, 3]])

# 행렬 곱셈 계산
result_matrix = np.dot(matrix_A, matrix_B)

# 결과 출력
print(result_matrix)
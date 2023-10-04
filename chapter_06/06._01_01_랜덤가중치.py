import numpy as np

# 입력 노드 수와 은닉층 노드 수 설정
input_nodes = 5
hidden_nodes = 5

# 평균과 표준 편차 설정
mean = 0.0
stddev = 1.0 / np.sqrt(input_nodes)  # 표준 편차를 입력 노드 수의 역수로 설정

# 가중치 초기화
initial_weights = np.random.normal(mean, stddev, (hidden_nodes, input_nodes))

# 결과 출력
print("가중치 초기화 결과:", initial_weights)
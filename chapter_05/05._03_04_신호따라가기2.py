import numpy as np

# 입력값
input_layer = np.array([0.5, 1, 0.3])

# 가중치
hidden_weights = np.array([
    [0.8, 0.7, 0.6],
    [0.1, 0.3, 0.2],
    [0.5, 0.4, 0.6]
])

output_weights = np.array([
    [0.6, 0.7, 0.8],
    [0.3, 0.2, 0.2],
    [0.4, 0.5, 0.6]
])

# 은닉 계층의 출력 계산
hidden_layer_output = np.dot(input_layer, hidden_weights)

# 시그모이드 활성화 함수를 적용
hidden_layer_output1 = 1 / (1 + np.exp(-hidden_layer_output))

# 출력 계층의 출력 계산
output_layer_output = np.dot(hidden_layer_output1, output_weights)

# 시그모이드 활성화 함수를 적용
output_layer_output1 = 1 / (1 + np.exp(-output_layer_output))

print("입력-은닉:", hidden_layer_output)
print("입력-은닉_활성함수:", hidden_layer_output1)

print("출력값:", output_layer_output)
print("출력값_활성함수:", output_layer_output1)
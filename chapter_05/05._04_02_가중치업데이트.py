import numpy as np

# 주어진 값
오차 = 0.1341
입력1_출력 = 2.0
입력2_출력 = 0.5
가중치_입력1 = 0.2
가중치_입력2 = 0.3
학습률 = 0.1  # 학습률 설정

# 시그모이드 활성화 함수와 미분 함수
x = 가중치_입력1 * 입력1_출력 + 가중치_입력2 * 입력2_출력
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

항_1 = 오차
항_2 = sigmoid(x)*(1-sigmoid(x))
항_3_1 = 입력1_출력
항_3_2 = 입력2_출력

가중치변화1 = -(항_1) * 항_2 * 항_3_1
가중치변화2 = -(항_1) * 항_2 * 항_3_2

가중치1업데이트 = 가중치_입력1 - 가중치변화1 * 학습률
가중치2업데이트 = 가중치_입력2 - 가중치변화2 * 학습률
print("노드1가중치변경:", 가중치1업데이트)
print("노드2가중치변경:", 가중치2업데이트)

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def calculate_output(inputs, weights):
    if len(inputs) != len(weights):
        raise ValueError("입력값과 가중치의 개수가 맞지 않습니다.")
    
    weighted_sum = sum([x * w for x, w in zip(inputs, weights)])
    output = sigmoid(weighted_sum)
    return output

inputs = [1, 2, 3]
weights = [1, 1, 1]

output = calculate_output(inputs, weights)
print("Output:", output)
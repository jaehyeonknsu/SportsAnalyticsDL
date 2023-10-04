import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def calculate_output(inputs, weights):
    if len(inputs) != len(weights):
        raise ValueError("The length of inputs and weights should be the same.")
    
    weighted_sum = sum([x * w for x, w in zip(inputs, weights)])
    output = sigmoid(weighted_sum)
    return output

inputs = [2, 0.5]
weights = [[0.7, 0.6], [0.2, 0.3]]

outputs = []
for i in range(len(weights)):
    output = calculate_output(inputs, weights[i])
    outputs.append(output)

print("Outputs:", outputs)
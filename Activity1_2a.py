import numpy as np

# Given data
random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

# Calculate sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Calculate sigmoid for each value and print
sigmoid_values = [sigmoid(x) for x in random_values]
print("Sigmoid values:")
for val, sigmoid_val in zip(random_values, sigmoid_values):
    print(f"Sigmoid({val}) = {sigmoid_val}")



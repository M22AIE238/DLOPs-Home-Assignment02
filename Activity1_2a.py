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


import numpy as np

# Given data
random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

# ReLU function
def ReLU(x):
    return np.maximum(0, x) 

# Leaky ReLU function
def Leaky_ReLU(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

# Tanh function
def Tanh(x):
    return np.tanh(x)

# Calculate outputs for each function
ReLU_values = ReLU(np.array(random_values))
Leaky_ReLU_values = Leaky_ReLU(np.array(random_values))
Tanh_values = Tanh(np.array(random_values))

# Print the results
print("ReLU values:")
print(Leaky_ReLU_values) ## A bug is created by wrong printing wrong values
print("\nLeaky ReLU values:")
print(ReLU_values)
print("\nTanh values:")
print(Tanh_values)



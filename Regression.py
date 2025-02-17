import numpy as np

def mean_removal(data):
  mean = np.mean(data, axis=0)
  centered_data = data - mean
  return centered_data

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
centered_data = mean_removal(data)
print("Original data:\n", data)
print("Centered data:\n", centered_data)
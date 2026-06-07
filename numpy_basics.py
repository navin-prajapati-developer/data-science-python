# NumPy Basics - Working with Numbers

import numpy as np

# Creating arrays
numbers = np.array([1, 2, 3, 4, 5])
print("Array:", numbers)

# Math operations
print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))
print("Max:", np.max(numbers))
print("Min:", np.min(numbers))

# 2D array (like a table)
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\nMatrix:")
print(matrix)
print("Shape:", matrix.shape)

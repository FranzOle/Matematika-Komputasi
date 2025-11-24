import numpy as np

matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriks A:\n", matrix_a)

matrix_b = np.array([[1, 1], [2, 2]])
matrix_c = np.array([[3, 3], [4, 4]])

result_add = matrix_b + matrix_c
print("Penjumlahan Matriks: \n", result_add)

transpose_a = np.transpose(matrix_a)
print("Transpose Matriks A:\n", transpose_a)
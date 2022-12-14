# From openai chatgpt
import numpy as np

# Without lib
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]]

matrix_sum = [[matrix_1[i][j] + matrix_2[i][j] for j in range(3)] for i in range(3)]
print(matrix_sum)

# Use lib
arr1 = np.array([[1, 2],
                 [3, 4]])
arr2 = np.array([[5, 6],
                 [7, 8]])

arr_result = np.multiply(arr1, arr2)
print(f'Matrix Product of arr1 and arr2 is:\n{arr_result}')

arr_result = np.matmul(arr2, arr1)
print(f'Matrix Product of arr2 and arr1 is:\n{arr_result}')

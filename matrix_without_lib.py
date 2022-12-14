# From openai chatgpt
matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_2 = [[10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]]

matrix_sum = [[matrix_1[i][j] + matrix_2[i][j] for j in range(3)] for i in range(3)]
print(matrix_sum)

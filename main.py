import random


#функция для создания матрицы заданного размера с случайными числами
def createRandomMatrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

# Функция для отображения матрицы
def printMatrix(matrix,name):
    print(f"\nМатрица {name}:")
    for row in matrix:
        print(row)
#функция для сложения двух матриц
def addMatrices(matrix_a,matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return result_matrix
#функция для вычитания двух матриц
def subtractMatrices(matrix_a,matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return result_matrix
#функция для умножения двух матриц
def multiplyMatrices(matrix_a,matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_a[i][k]*matrix_b[k][j]
    return result_matrix
#функция для транспонирования матрицы
def transposeMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix

#функция для вычисления определителя 2x2 матрицы
def determinant2x2(matrix):
    return (matrix[0][0] * matrix[1][1] -
            matrix[0][1] * matrix[1][0])

#функция для вычисления определителя 3x3 матрицы
def determinant3x3(matrix):
    det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
           matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
           matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))
    return det
#функция для вычисления следа матрицы
def traceMatrix(matrix):
    trace = 0
    size = min(len(matrix), len(matrix[0]))
    for i in range(size):
        trace += matrix[i][i]
    return trace
#функция для скалярного умножения матрицы на число
def scalarMultiply(matrix,scalar):
    rows = len(matrix)
    cols = len(matrix[0])
    result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result_matrix[i][j] = matrix[i][j] * scalar
    return result_matrix
#функция для нахождения максимального элемента в матрице
def maxElement(matrix):
    max_val = matrix[0][0]
    for row in matrix:
        for value in row:
            if value>max_val:
                max_val = value
    return max_val
#функция для нахождения минимального элемента в матрице
def minElement(matrix):
    min_val = matrix[0][0]
    for row in matrix:
        for value in row:
            if value<min_val:
                min_val = value
    return min_val
#функция для проверки, является ли матрица симметричной
def isSymmetric(matrix):
    rows = len(matrix)
    for i in range(rows):
        for j in range(i + 1, rows):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
#функция для сравнения двух матриц на равенство
def matricesEqual(matrix_a,matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return False
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            if matrix_a[i][j] != matrix_b[i][j]:
                return False
    return True

#функция для сложения всех элементов матрицы
def sumOfElements(matrix):
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    return total_sum

#функция для создания единичной матрицы заданного размера
def identityMatrix(size):
    identity_mat = [[1 if i == j else 0
                     for j in range(size)]
                    for i in range(size)]

    return identity_mat

#функция для нахождения максимального значения в каждом столбце
def maxInColumns(matrix):
    num_cols = len(matrix[0])
    max_values = []
    for j in range(num_cols):
        col_max = float('-inf')
        for i in range(len(matrix)):
            if matrix[i][j]>col_max:
                col_max = matrix[i][j]
        max_values.append(col_max)
    return max_values
# Функция для нахождения минимального значения в каждом столбце
def minInColumns(matrix):
    num_cols = len(matrix[0])
    min_values = []
    for j in range(num_cols):
        col_min = float('inf')
        for i in range(len(matrix)):
            if matrix[i][j]< col_min:
                col_min = matrix[i][j]
        min_values.append(col_min)
    return min_values

#функция для создания нулевой матрицы заданного размера
def zeroMatrix(rows,cols):
    return [[0] * cols for _ in range(rows)]

#функция для сложения всех элементов матрицы
def sumOfElements(matrix):
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    return total_sum
#функция для проверки, является ли матрица диагональной
def isDiagonal(matrix):
    rows = len(matrix)
    for i in range(rows):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] != 0:
                return False
    return True

#функция для нахождения подматрицы (удаление заданной строки и столбца)
def submatrix(matrix,remove_row, remove_col):
    sub_mat = []
    for i in range(len(matrix)):
        if i == remove_row:
            continue
        new_row = []
        for j in range(len(matrix[i])):
            if j == remove_col:
                continue
            new_row.append(matrix[i][j])
        sub_mat.append(new_row)
    return sub_mat

#ввод размеров матриц от пользователя
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

#создаем две случайные матрицы
matrix_A = createRandomMatrix(rows, cols)
matrix_B = createRandomMatrix(rows, cols)

#выводим созданные матрицы
printMatrix(matrix_A, 'A')
printMatrix(matrix_B, 'B')

#сложение матриц
matrix_C = addMatrices(matrix_A, matrix_B)
printMatrix(matrix_C, 'C (A + B)')

#вычитание матриц
matrix_D = subtractMatrices(matrix_A, matrix_B)
printMatrix(matrix_D, 'D (A - B)')

#умножение матриц (только если количество столбцов A равно количеству строк B)
if cols == rows:
    matrix_E = multiplyMatrices(matrix_A, matrix_B)
    printMatrix(matrix_E, 'E (A * B)')

    #вычисление определителя 3x3 матрицы (если размерность 3x3)
    if rows == 3 and cols == 3:
        det_A = determinant3x3(matrix_A)
        det_B = determinant3x3(matrix_B)
        print(f"\nОпределитель матрицы A: {det_A}")
        print(f"Определитель матрицы B: {det_B}")

    #вычисление следа матриц
    trace_A = traceMatrix(matrix_A)
    trace_B = traceMatrix(matrix_B)
    print(f"\nСлед матрицы A: {trace_A}")
    print(f"След матрицы B: {trace_B}")

    #транспонирование матрицы A
    transposed_F_A = transposeMatrix(matrix_A)
    printMatrix(transposed_F_A, 'F (A^T)')

    #транспонирование матрицы B
    transposed_G_B = transposeMatrix(matrix_B)
    printMatrix(transposed_G_B, 'G (B^T)')

    #скалярное умножение на число (например, 2)
    scalar_value = 2
    scaled_H_A = scalarMultiply(matrix_A, scalar_value)
    printMatrix(scaled_H_A, f'H (A * {scalar_value})')

#нахождение максимального и минимального элементов в матрице А
max_A_element = maxElement(matrix_A)
min_A_element = minElement(matrix_A)

#нахождение максимального и минимального элементов в матрице B
max_B_element = maxElement(matrix_B)
min_B_element = minElement(matrix_B)

print(f"\nМаксимальный элемент в A: {max_A_element}")
print(f"Минимальный элемент в A: {min_A_element}")

print(f"Максимальный элемент в B: {max_B_element}")
print(f"Минимальный элемент в B: {min_B_element}")

#проверка на симметричность
symmetrical_A_flag = isSymmetric(matrix_A)
symmetrical_B_flag = isSymmetric(matrix_B)

print(f"\nМатрица A симметрична: {symmetrical_A_flag}")
print(f"Матрица B симметрична: {symmetrical_B_flag}")

#сравнение двух матриц на равенство
equal_check_flag = matricesEqual(matrix_A, matrix_B)
print(f"\nМатрица A равна Матрице B: {equal_check_flag}")

#сложение всех элементов в A и B
total_sum_A = sumOfElements(matrix_A)
total_sum_B = sumOfElements(matrix_B)

print(f"\nСумма всех элементов в A: {total_sum_A}")
print(f"Сумма всех элементов в B: {total_sum_B}")

#создание единичной матрицы
identity_mat_size = min(rows, cols)
identity_mat = identityMatrix(identity_mat_size)
printMatrix(identity_mat, "Eдиничная Матрица")

#проверка на диагональность
diag_A = isDiagonal(matrix_A)
diag_B = isDiagonal(matrix_B)

print(f"\nМатрица A диагональная: {diag_A}")
print(f"Матрица B диагональная: {diag_B}")

#максимальные значения в каждом слолбце для А и B
max_in_cols_A = maxInColumns(identity_mat)
max_in_cols_B = maxInColumns(identity_mat)

print(f"\nМаксимальные значения в каждом столбце для A: {max_in_cols_A}")
print(f"Максимальные значения в каждом столбце для B: {max_in_cols_B}")

#минимальные значения в каждом слолбце для А и B
min_in_cols_A = minInColumns(identity_mat)
min_in_cols_B = minInColumns(identity_mat)

print(f"\nМинимальные значения в каждом столбце для A: {min_in_cols_A}")
print(f"Минимальные значения в каждом столбце для B: {min_in_cols_B}")

#построение нулевой матрицы
zero_mat = zeroMatrix(rows, cols)
printMatrix(zero_mat, "Нулевая Матрица")

#нахождение подматрицы после удаления первой строки и первого столбца
sub_mat = submatrix(matrix_A, 0, 0)

printMatrix(sub_mat, "Подматрица после удаления первой строки и первого столбца")

#вывод сообщения о завершении работы программы
print("\nВсе операции выполнены успешно!")

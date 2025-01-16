def input_matrix(rows, cols, matrix_name):
    print(f"Enter elements for {matrix_name}:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0] * cols for _ in range(rows)]  
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] * matrix2[i][j]
    return result
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix1 = input_matrix(rows, cols, "Matrix 1")
matrix2 = input_matrix(rows, cols, "Matrix 2")

result_matrix = add_matrices(matrix1, matrix2)
print("Resultant matrix after addition:")
for row in result_matrix:
    print(row)

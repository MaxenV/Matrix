from matrix_lib import Matrix

matrix1 = Matrix([[4, 4, 3, 5], [7, 8, 5, 7], [2, 7, 3, 1], [6, 3, 4, 5]])
matrix2 = Matrix([[4, 4, 3, 5], [7, 8, 5, 7], [2, 7, 3, 1], [6, 3, 4, 5]])

matrix3 = Matrix([[4, 4, 3], [7, 8, 5], [2, 7, 3], [6, 3, 4]])

matrix4 = Matrix([[5, 3, 6, 2], [7, 4, 6, 8], [1, 5, 3, 6]])

# matrixI = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


matrix1.show_matrix()
matrix1.transpose()
print()
matrix1.show_matrix()

print()
print()
matrix3.show_matrix()
matrix3.transpose()
print()
matrix3.show_matrix()

print()
print()
matrix4.show_matrix()
matrix4.transpose()
print()
matrix4.show_matrix()

from matrix_lib import *

# matrix1 = Matrix([[4, 4, 3, 5], [7, 8, 5, 7], [2, 7, 3, 1], [6, 3, 4, 5]])
# matrix2 = Matrix([[4, 4, 3, 5], [7, 8, 5, 7], [2, 7, 3, 1], [6, 3, 4, 5]])
#
# matrix3 = Matrix([[4, 4, 3], [7, 8, 5], [2, 7, 3], [6, 3, 4]])
#
# matrix4 = Matrix([[5, 3, 6, 2], [7, 4, 6, 8], [1, 5, 3, 6]])
#
# # matrixI = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
#
#
# matrix1.show_matrix()
# matrix1.transpose()
# print()
# matrix1.show_matrix()
#
# print()
# print()
# matrix3.show_matrix()
# matrix3.transpose()
# print()
# matrix3.show_matrix()
#
# print()
# print()
# matrix4.show_matrix()
# matrix4.transpose()
# print()
# matrix4.show_matrix()


# #table3 = Matrix([[4, 7, 3, 5, 5, 6], [7, 8, 5, 9, 5, 6], [2, 7, 3, 1, 5, 6], [6, 3, 4, 7, 5, 8], [6, 3, 4, 5, 5, 3], [6, 3, 4, 5, 3, 6]])

# table = [[4, 7, 3, 5], [7, 8, 5, 9], [2, 7, 3, 1], [6, 3, 4, 5]]
table2 = [[4, 4, 3], [7, 8, 5], [2, 7, 3]]
table3 = [[7, 8, 5], [2, 7, 3], [4, 4, 3]]
# print(un_op_determinant(table3))

# print(len(table))
# print(table[5])
#
# print([x for cto, x in enumerate(table) if cto != en])
# mtx = table2
# print(mtx)
# for count, value in enumerate(mtx[0]):
#     # new_mtx = Matrix()
#     # print([[vl for ct, vl in enumerate(row) if ct != count] for cc, row in enumerate(mtx) if cc != 1])
#     print(count)

mtx = Matrix(table2)
mtx2 = Matrix(table3)
mtx.show_matrix()
mtx.multipy(mtx2)

mtx.show_matrix()

# mt2 = inverse(mtx)
#
# mtx.show_matrix()
# mt2.show_matrix()

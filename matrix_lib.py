from random import randint


class Matrix:
    def __init__(self, *mtx):
        if len(mtx) > 0:
            if type(mtx[0]) == list:
                if check_if_correct(mtx[0]):
                    self.matrix = mtx[0]
                    self.columns = len(self.matrix[0])
                    self.rows = len(self.matrix)
                else:
                    print("Given matrix in invalid")
            elif type(mtx[0]) == int:
                if len(mtx) > 1 and type(mtx[1]) == int:
                    self.columns = mtx[0]
                    self.rows = mtx[1]
                    self.matrix = self.fill_matrix_random(1, 50)
                else:
                    self.columns = mtx[0]
                    self.rows = mtx[0]
                    self.matrix = self.fill_matrix_random(1, 50)
            else:
                raise TypeError("Required list or int")

        else:
            self.rows = 0
            self.columns = 0
            self.matrix = list()

    def fill_matrix_asks_user(self):
        return [[int(input(f"Type number on {w}{c}: ")) for c in range(1, self.columns+1)]
                for w in range(1, self.rows+1)]

    def fill_matrix_random(self, minimum, maximum):
        return [[randint(minimum, maximum) for _ in range(1, self.columns+1)] for _ in range(1, self.rows+1)]

    def show_matrix(self):
        for row in self.matrix:
            for num in row:
                print(num, end="\t")
            print()

    def check_if_square(self):
        return self.columns == self.rows

    def check_if_similar(self, mtx):
        return self.columns == mtx.columns and self.rows == mtx.rows

    def check_if_can_multiply(self, mtx):
        return self.rows == mtx.columns

    def add(self, ad_matrix):
        if not self.check_if_similar(ad_matrix):
            print("You can add only similar matrices")
        else:
            for row in range(self.rows):
                for col in range(self.columns):
                    self.matrix[row][col] += ad_matrix.matrix[row][col]

    def subtract(self, ad_matrix):
        if not self.check_if_similar(ad_matrix):
            print("You can subtract only similar matrices")
        else:
            for row in range(self.rows):
                for col in range(self.columns):
                    self.matrix[row][col] -= ad_matrix.matrix[row][col]

    def transpose(self):
        rows = len(self.matrix)
        new_rows = self.rows

        for x in range(self.rows):
            for y in range(x, self.columns):
                if y < new_rows:
                    self.matrix[y].append(self.matrix[x].pop(0))
                    if x != y and y < rows:
                        self.matrix[x].append(self.matrix[y].pop(0))
                else:
                    new_rows += 1
                    self.matrix.append([self.matrix[x].pop(0)])

        for x in range(self.columns, self.rows):
            for z in range(self.columns):
                self.matrix[z].append(self.matrix[x].pop(0))

        self.columns = self.rows
        self.rows = new_rows

def check_if_correct(mtx):
    if type(mtx[0]) == list:
        num_cols = len(mtx[0])
        for row in mtx:
            if type(row) == list and num_cols != len(row):
                return False
            for num in row:
                if not (type(num) == int or type(num) == float):
                    return False
    else:
        return False
    return True

def determinant2x2(mtx):
    if len(mtx.matrix) == 2 and len(mtx.matrix[0]) == 2:
        return mtx.matrix[0][0] * mtx.matrix[1][1] - mtx.matrix[1][0] * mtx.matrix[0][1]
    else:
        print("It is not 2x2 determinant")


def determinant3x3(mtx):
    if len(mtx.matrix) == 3 and len(mtx.matrix[0]) == 3:
        plus = mtx.matrix[0][0] * mtx.matrix[1][1] * mtx.matrix[2][2]
        plus += mtx.matrix[0][1] * mtx.matrix[1][2] * mtx.matrix[2][0]
        plus += mtx.matrix[0][2] * mtx.matrix[1][0] * mtx.matrix[2][1]

        minus = mtx.matrix[2][0] * mtx.matrix[1][1] * mtx.matrix[0][2]
        minus += mtx.matrix[2][1] * mtx.matrix[1][2] * mtx.matrix[0][0]
        minus += mtx.matrix[2][2] * mtx.matrix[1][0] * mtx.matrix[0][1]
        return plus - minus
    else:
        print("It is not 3x3 determinant")


def un_op_determinant(mtx):
    if check_if_correct(mtx.matrix):
        if len(mtx.matrix) == 1:
            return mtx.matrix[0][0]
        elif len(mtx.matrix) == 2:
            return determinant2x2(mtx)
        elif len(mtx.matrix) == 3:
            return determinant3x3(mtx)
        else:
            det = 0
            for count, value in enumerate(mtx.matrix[0]):
                new_mtx = Matrix([[vl for ct, vl in enumerate(row) if ct != count]
                                  for cc, row in enumerate(mtx.matrix) if cc != 0])
                det += pow(-1, count) * value * un_op_determinant(new_mtx)
            return det
    else:
        print("Can't show determinant from not square matrix")


def determinant(mtx):
    new_matrix = mtx.matrix

    for row_number, row in enumerate(new_matrix):
        rn_value = row[row_number]

        for num2, row2 in enumerate(new_matrix[row_number+1:]):
            multiplier = row2[row_number] * (rn_value**(-1))

            for index, value in enumerate(row):
                row2[index] = row2[index] - multiplier * row[index]

    det_value = 1
    for index, row in enumerate(new_matrix):
        det_value = det_value*row[index]

    return round(det_value, 5)

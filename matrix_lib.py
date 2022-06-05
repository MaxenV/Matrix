from random import randint


class Matrix:
    def __init__(self, *mtx):
        if len(mtx) > 0:
            if type(mtx[0]) == list:
                if self.check_if_correct(mtx[0]):
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
        return [[int(input(f"Type number on {w}{c}: ")) for c in range(1, self.columns+1)] for w in range(1, self.rows+1)]

    def fill_matrix_random(self, minimum, maximum):
        return [[randint(minimum, maximum) for _ in range(1, self.columns+1)] for _ in range(1, self.rows+1)]

    def show_matrix(self):
        for row in self.matrix:
            for num in row:
                print(num, end="\t")
            print()


    @staticmethod
    def check_if_correct(mtx):
        if type(mtx[0]) == list:
            num_cols = len(mtx[0])
            for row in mtx:
                if type(row) == list and num_cols != len(row):
                    return False
                for num in row:

                    print(type(num))
                    if not (type(num) == int or type(num) == float):
                        return False
        else:
            return False
        return True

    def check_if_square(self):
        return self.columns == self.rows

    def check_if_similar(self, mtx):
        return self.columns == mtx.columns and self.rows == mtx.rows

    def check_if_can_multiply(self, mtx):
        return self.rows == mtx.columns


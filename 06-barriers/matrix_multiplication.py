import time
import random


class MatrixMultiply:

    def __init__(self, matrix_size):

        self.matrix_size = matrix_size
        self.matrix_a = self.getRandomMatrix(matrix_size)
        self.matrix_b = self.getRandomMatrix(matrix_size)
        self.result = matrix = [ [0]* matrix_size for _ in range(matrix_size)]

    @staticmethod
    def getRandomMatrix(matrix_size):

        matrix = [ [0]* matrix_size for _ in range(matrix_size)]

        for row in range(matrix_size):
            for col in range(matrix_size):
                matrix[row][col] = random.randint(-5, 5)

        return matrix

    def printMatix(self):


        for row in range(self.matrix_size):
            print(self.matrix_a[row], self.matrix_b[row], self.result[row])


    def multiply(self):

        for row in range(self.matrix_size):
            for col in range(self.matrix_size):

                for i in range(self.matrix_size):
                    self.result[row][col] += self.matrix_a[row][i]*self.matrix_a[i][col]



if __name__ == "__main__":


    matrix_size = 5

    obj = MatrixMultiply(matrix_size)

    start = time.time()

    obj.multiply()

    end = time.time()

    obj.printMatix()

    print(f"Time Taken : {end-start}")


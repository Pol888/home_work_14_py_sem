class Matrix:
    '''An instance of this class stores 1 matrix in memory, performs operations with other instances'''
    def __init__(self, matrix:list):
        '''The matrix is initialized by a property of this class'''
        if not isinstance(matrix, list):
            print('Warning: Несоответствующий тип данных')
        self.matrix = matrix

    def __str__(self):
        """Displays the string representation of the matrix"""
        string_representation = ''
        for i in self.matrix:
            string_representation += str(i) + '\n'
        return 'It`s matrix\n' + string_representation

    def __repr__(self):
        """String representation of the current instance"""
        return f'Matrix({str(self.matrix)})'

    def matrix_size(self):
        """Calculates the size of the matrix"""
        return len(self.matrix) * len(self.matrix[0])

    def __add__(self, other):
        """Performs matrix addition"""
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in
                            range(len(self.matrix[0]))] for i in range(len(self.matrix))])
        return "The matrices do not correspond to the dimensions"

    def __mul__(self, other):
        """Performs the product of matrices"""
        if len(self.matrix[0]) == len(other.matrix):
            new_mx = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for y in range(len(self.matrix[0])):
                        new_mx[i][j] += self.matrix[i][y] * other.matrix[y][j]
            return Matrix(new_mx)
        return "The matrices do not correspond to the dimensions"

    def __eq__(self, o) -> bool:
        '''Compares matrices (operator: ==)'''
        return self.matrix_size() == o.matrix_size()

    def __ne__(self, o) -> bool:
        '''Compares matrices (operator: !=)'''
        return self.matrix_size() != o.matrix_size()

    def __gt__(self, o) -> bool:
        '''Compares matrices (operator: >)'''
        return self.matrix_size() > o.matrix_size()

    def __ge__(self, o) -> bool:
        '''Compares matrices (operator: <=)'''
        return self.matrix_size() <= o.matrix_size()

    def __lt__(self, o) -> bool:
        '''Compares matrices (operator: <)'''
        return self.matrix_size() < o.matrix_size()

    def __le__(self, o) -> bool:
        '''Compares matrices (operator: >=)'''
        return self.matrix_size() >= o.matrix_size()

if __name__ == '__main__':
    print(Matrix([[1, 2, 3], [4, 5, 6]]) * Matrix([[1, 1, 1], [2, 2, 2], [1, 1, 1]]))

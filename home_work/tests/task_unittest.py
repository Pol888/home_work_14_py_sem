import unittest
from home_work.task_a_main_home import *
import io
from unittest.mock import patch

class TestFullMatrix(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_init_warning(self, mock_stdout):
        self.assertTrue(Matrix(([1, 2, 3], [4, 5, 6])))
        self.assertEquals(mock_stdout.getvalue(), 'Warning: Несоответствующий тип данных\n')

    def test_init_and_str(self):
        self.assertEquals(Matrix([[1, 2, 3], [4, 5, 6]]).__str__(), 'It`s matrix\n[1, 2, 3]\n[4, 5, 6]\n')
        self.assertEquals(Matrix([[1, 2, 3], [4, 5, 6]]).__repr__(), 'Matrix([[1, 2, 3], [4, 5, 6]])')
    def test_size_matrix(self):
        self.assertEquals(Matrix([[1, 2, 3], [4, 5, 6]]).matrix_size(), 6)
    def test___add__(self):
        self.assertEquals(Matrix([[1, 2, 3], [4, 5, 6]]) + Matrix([[1, 1, 1], [1, 1, 1]]),
                          Matrix([[2, 3, 4], [5, 6, 7]]))
        self.assertEquals(Matrix([[1, 2, 3], [4, 5, 6]]) + Matrix([[1, 1, 1]]),
                          'The matrices do not correspond to the dimensions')
    def test___mul__(self):
        self.assertEquals(Matrix([[1, 2, 3], [4, 5, 6]]) * Matrix([[1, 1, 1], [2, 2, 2], [1, 1, 1]]),
                          Matrix([[8, 8, 8], [20, 20, 20]]))
        self.assertEquals(Matrix([[1, 2, 3], [4, 5, 6]]) * Matrix([[1, 1, 1], [2, 2, 2]]),
                          'The matrices do not correspond to the dimensions')




if __name__ == '__main__':
    unittest.main(verbosity=2)

'''============================= test session starts =============================
collecting ... collected 5 items

task_unittest.py::TestFullMatrix::test___add__ 
task_unittest.py::TestFullMatrix::test___mul__ 
task_unittest.py::TestFullMatrix::test_init_and_str 
task_unittest.py::TestFullMatrix::test_init_warning 
task_unittest.py::TestFullMatrix::test_size_matrix 

======================== 5 passed, 8 warnings in 0.12s ========================
PASSED                    [ 20%]PASSED                    [ 40%]PASSED               [ 60%]PASSED               [ 80%]PASSED                [100%]
Process finished with exit code 0'''
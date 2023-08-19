import pytest
from home_work.task_a_main_home import *



def test_init_warning(capfd):
    Matrix(([1, 2, 3], [4, 5, 6]))
    cap = capfd.readouterr()
    assert cap.out == 'Warning: Несоответствующий тип данных\n'

def test_init_and_str():
    assert Matrix([[1, 2, 3], [4, 5, 6]]).__str__() == 'It`s matrix\n[1, 2, 3]\n[4, 5, 6]\n'
    assert Matrix([[1, 2, 3], [4, 5, 6]]).__repr__() == 'Matrix([[1, 2, 3], [4, 5, 6]])'

def test_size_matrix():
    assert Matrix([[1, 2, 3], [4, 5, 6]]).matrix_size() == 6

def test___add__():
    assert Matrix([[1, 2, 3], [4, 5, 6]]) + Matrix([[1, 1, 1], [1, 1, 1]]) == Matrix([[2, 3, 4], [5, 6, 7]])
    assert Matrix([[1, 2, 3], [4, 5, 6]]) + Matrix([[1, 1, 1]]) == 'The matrices do not correspond to the dimensions'
def test___mul__():
    assert Matrix([[1, 2, 3], [4, 5, 6]]) * Matrix([[1, 1, 1], [2, 2, 2], [1, 1, 1]]) == \
           Matrix([[8, 8, 8], [20, 20, 20]])
    assert Matrix([[1, 2, 3], [4, 5, 6]]) * Matrix([[1, 1, 1], [2, 2, 2]]) == \
           'The matrices do not correspond to the dimensions'



if __name__ == '__main__':
    pytest.main(['-v'])

'''============================= test session starts =============================
collecting ... collected 5 items

task_pytest.py::test_init_warning PASSED                                 [ 20%]
task_pytest.py::test_init_and_str PASSED                                 [ 40%]
task_pytest.py::test_size_matrix PASSED                                  [ 60%]
task_pytest.py::test___add__ PASSED                                      [ 80%]
task_pytest.py::test___mul__ PASSED                                      [100%]

============================== 5 passed in 0.07s =============================='''
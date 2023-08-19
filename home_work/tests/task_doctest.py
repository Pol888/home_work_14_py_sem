import doctest

if __name__ == '__main__':
    doctest.testfile('task_doctest.txt', verbose=True)


"""Trying:
    from home_work.task_a_main_home import *
Expecting nothing
ok
Trying:
    Matrix([[1, 2, 3], [4, 5, 6]]).__str__()
Expecting:
    'It`s matrix\n[1, 2, 3]\n[4, 5, 6]\n'
ok
Trying:
    Matrix([[1, 2, 3], [4, 5, 6]]).__repr__()
Expecting:
    'Matrix([[1, 2, 3], [4, 5, 6]])'
ok
Trying:
    Matrix([[1, 2, 3], [4, 5, 6]]).matrix_size()
Expecting:
    6
ok
Trying:
    Matrix([[1, 2, 3], [4, 5, 6]]) + Matrix([[1, 1, 1], [1, 1, 1]])
Expecting:
    Matrix([[2, 3, 4], [5, 6, 7]])
ok
Trying:
    Matrix([[1, 2, 3], [4, 5, 6]]) + Matrix([[1, 1, 1]])
Expecting:
    'The matrices do not correspond to the dimensions'
ok
Trying:
    Matrix([[1, 2, 3], [4, 5, 6]]) * Matrix([[1, 1, 1], [2, 2, 2], [1, 1, 1]])
Expecting:
    Matrix([[8, 8, 8], [20, 20, 20]])
ok
Trying:
    Matrix([[1, 2, 3], [4, 5, 6]]) * Matrix([[1, 1, 1], [2, 2, 2]])
Expecting:
    'The matrices do not correspond to the dimensions'
ok
1 items passed all tests:
   8 tests in task_doctest.txt
8 tests in 1 items.
8 passed and 0 failed.
Test passed."""
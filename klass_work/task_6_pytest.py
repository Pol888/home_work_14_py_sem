import pytest
from klass_work.task_6 import *
import sys


@pytest.fixture
def fix_1():
    return User('Pol', '1', '3'), User('Pol', '1', '999')


@pytest.fixture
def fix_2():
    path = 'C:\\Users\\pollove\\Desktop\\home_work_14_py_sem\\klass_work\\task_6_file_name_id_al.json'
    return Project(path, 2), path


def test_user_class(fix_1):
    assert fix_1[0].__str__() == 'Имя - Pol, id - 1, уровень доступа - 3'
    assert fix_1[0] == fix_1[1]


def test_project_class___loading_data(fix_2):
    assert isinstance(fix_2[0].lots_of_users, set)
    assert len(fix_2[0].lots_of_users) == 4
    assert isinstance(list(fix_2[0].lots_of_users)[0], User)


def test_project_class_init(fix_2):
    assert fix_2[0].file_name == fix_2[1]
    assert fix_2[0].sys_access_level == 2
    assert fix_2[0].system_users == []


def test_project_class_log_in_to_the_system(fix_2):
    sys.stdin = open('test_project_class_log_in_to_the_system.txt')
    with pytest.raises(AccessError):
        fix_2[0].log_in_to_the_system()


def test_project_class_log_in_to_the_system_to_the___to_add_a_user(fix_2):
    sys.stdin = open('test_project_class_log_in_to_the_system_to_the___to_add_a_user.txt')
    fix_2[0].log_in_to_the_system()
    assert fix_2[0].system_users[0] == User('Pol', '32')


if __name__ == '__main__':
    pytest.main(['-v'])

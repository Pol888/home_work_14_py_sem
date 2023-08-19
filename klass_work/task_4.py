import pytest
from klass_work.task_1 import special_function


def test_1():
    assert special_function("super mario") == "super mario"


def test_2():
    assert special_function("Super MARIo") == "super mario"


def test_3():
    assert special_function("Super, MARIo.") == "super mario"


def test_4():
    assert special_function("super marioсупермарио") == "super mario"


def test_5():
    assert special_function("supeR maRio,-супермарио") == "super mario"


if __name__ == '__main__':
    pytest.main()

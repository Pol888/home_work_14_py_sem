import unittest
from task_1 import special_function


class TestSpecialFunction(unittest.TestCase):

    def test_1(self):
        self.assertEquals(special_function("super mario"), "super mario")

    def test_2(self):
        self.assertEquals(special_function("Super MARIo"), "super mario")

    def test_3(self):
        self.assertEquals(special_function("Super, MARIo."), "super mario")

    def test_4(self):
        self.assertEquals(special_function("super marioсупермарио"), "super mario")

    def test_5(self):
        self.assertEquals(special_function("supeR maRio,-супермарио"), "super mario")


if __name__ == '__main__':
    unittest.main(verbosity=2)

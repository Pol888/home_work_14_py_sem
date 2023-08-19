import unittest
from klass_work import task_5
import klass_work


class TestClassRectangle(unittest.TestCase):

    def test_init_and_str(self):
        self.assertEquals(task_5.Rectangle(2, 4).width, 4)
        self.assertEquals(task_5.Rectangle(4, 2).length, 4)
        self.assertEquals(task_5.Rectangle(5).width, 5)

        with self.assertRaises(klass_work.task_5.RectangleSideError):
            klass_work.task_5.Rectangle(-1, 3)
            klass_work.task_5.Rectangle(3, -1)

    def test_str(self):
        self.assertEquals(task_5.Rectangle(4, 2).__str__(), 'length = 4 and width = 2')

    def test_perimeter(self):
        self.assertEquals(task_5.Rectangle(3, 5).rectangle_perimeter(), 16)

    def test_area(self):
        self.assertEquals(task_5.Rectangle(3, 5).area_of_a_rectangle(), 15)

    def test_sum(self):
        self.assertEquals((task_5.Rectangle(4, 2) + task_5.Rectangle(1, 3)).rectangle_perimeter(), 20)

    def test_difference(self):
        self.assertEquals((task_5.Rectangle(4, 2) - task_5.Rectangle(1, 3)).rectangle_perimeter(), 4)

    def test_eq(self):
        self.assertTrue(task_5.Rectangle(4, 2) == task_5.Rectangle(2, 4))

    # итд.....


if __name__ == '__main__':
    unittest.main(verbosity=2)

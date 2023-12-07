import unittest
from code import find_solution1, find_solution2


class TestSolutions(unittest.TestCase):
    def test_get_distance(self):
        self.assertEqual(find_solution1('test1.txt'), 6440)

    def test_find_solution1(self):
        self.assertEqual(find_solution2('test1.txt'), 5905)


if __name__ == '__main__':
    unittest.main()

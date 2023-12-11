import unittest
from code import find_solution1, solve


class TestSolutions(unittest.TestCase):
    def test_find_solution1(self):
        self.assertEqual(find_solution1('test1.txt'), 374)


    def test_find_solution2(self):
        self.assertEqual(solve('test1.txt', 9), 1030)


if __name__ == '__main__':
    unittest.main()

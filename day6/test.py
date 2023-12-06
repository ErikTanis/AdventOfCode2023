import unittest
from code import get_distance, find_solution1


class TestSolutions(unittest.TestCase):
    def test_get_distance(self):
        self.assertEqual(get_distance(2, 7), 10)

    def test_find_solution1(self):
        self.assertEqual(find_solution1('test1.txt'), 288)



if __name__ == '__main__':
    unittest.main()

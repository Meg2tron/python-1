import unittest
import second_largest


class Second_Largest(unittest.TestCase):
    def test_case1(self):
        array = [10, 8, 90, 20]
        self.assertEqual(second_largest.second_largest(array), 20)
        pass

    def test_case2(self):
        array = [10, -1, -90, 20]
        self.assertEqual(second_largest.second_largest(array), 10)
        pass

    def test_case3(self):
        array = [0, 0, 0, 0]
        self.assertEqual(second_largest.second_largest(array), 0)
        pass


    pass


unittest.main()

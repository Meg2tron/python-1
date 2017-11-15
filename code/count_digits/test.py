import unittest
import count_digits

class Count_Cigits(unittest.TestCase):
    def testing_case1(self):
        self.assertEqual(count_digits.count_digits(123), 3)
        pass

    def testing_case2(self):
        self.assertEqual(count_digits.count_digits(0), 0)
        pass

    def testing_case3(self):
        self.assertEqual(count_digits.count_digits(4588), 4)
        pass

    def testing_case4(self):
        self.assertEqual(count_digits.count_digits(1), 1)
        pass

    def testing_case5(self):
        self.assertEqual(count_digits.count_digits(-1), 0)
        pass

    pass

unittest.main()

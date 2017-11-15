import unittest
import sum_of_digits

class Sum_Digits(unittest.TestCase):
    def testing_case1(self):
        self.assertEqual(sum_of_digits.sum_of_digits(123), 6)
        pass

    def testing_case2(self):
        self.assertEqual(sum_of_digits.sum_of_digits(0), 0)
        pass

    def testing_case3(self):
        self.assertEqual(sum_of_digits.sum_of_digits(4588), 25)
        pass

    def testing_case4(self):
        self.assertEqual(sum_of_digits.sum_of_digits(1), 1)
        pass

    def testing_case5(self):
        self.assertEqual(sum_of_digits.sum_of_digits(-1), None)
        pass

    pass

unittest.main()

import unittest
import gcd

class GCD(unittest.TestCase):
    def testing_case1(self):
        self.assertEqual(gcd.get_gcd(10,5), 5)
        pass

    def testing_case2(self):
        self.assertEqual(gcd.get_gcd(20,10), 10)
        pass

    def testing_case3(self):
        self.assertEqual(gcd.get_gcd(4,5), 1)
        pass

    def testing_case4(self):
        self.assertEqual(gcd.get_gcd(0,5), 0)
        pass

    pass

unittest.main()

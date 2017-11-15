import unittest
import get_lcm

class GCD(unittest.TestCase):
    def testing_case1(self):
        self.assertEqual(get_lcm.get_lcm(10,5), 5)
        pass

    def testing_case2(self):
        self.assertEqual(get_lcm.get_lcm(20,10), 10)
        pass

    def testing_case3(self):
        self.assertEqual(get_lcm.get_lcm(4,5), 1)
        pass

    def testing_case4(self):
        self.assertEqual(get_lcm.get_lcm(0,5), 0)
        pass

    pass

unittest.main()

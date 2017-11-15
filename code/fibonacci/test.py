import unittest
import fibonacci

limit1 = 5
limit2 = 7
class Fibonacci(unittest.TestCase):
    def testing_case1(self):
        self.assertEqual(fibonacci.get_series(limit1), [0, 1, 1, 2, 3, 5])
        pass

    def testing_case2(self):
        self.assertEqual(fibonacci.get_series(limit2), [0, 1, 1, 2, 3, 5, 8, 13])
        pass

    pass

unittest.main()

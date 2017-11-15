import unittest
import factorial

class Factorial(unittest.TestCase):
    def testing_iterative(self):
        self.assertEqual(factorial.iterative(6), 720)
        pass

    def testing_recursive(self):
        self.assertEqual(factorial.recursive(5), 120)
        pass


    pass

unittest.main()

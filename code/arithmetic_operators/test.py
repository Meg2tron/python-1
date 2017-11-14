import unittest
import arithmetics


class Test_Arithmetics(unittest.TestCase):
    def testing_addition_two_numbers(self):
        self.assertEqual(arithmetics.addition(1, 2), 3)
        pass

    def testing_multiplying_two_numbers(self):
        self.assertEqual(arithmetics.multiplication(1, 2), 2)
        pass

    def testing_subtracting_two_numbers(self):
        self.assertEqual(arithmetics.subtract(1, 2), -1)
        pass

    def testing_int_divide_two_numbers(self):
        self.assertEqual(arithmetics.int_division(1, 2), 0)
        pass

    def testing_divide_two_numbers(self):
        self.assertEqual(arithmetics.default_division(1, 2), 0.5)
        pass

    def testing_remainder_of_two_numbers(self):
        self.assertEqual(arithmetics.remainder(1, 2), 1)
        pass

    def testing_exponential_two_numbers(self):
        self.assertEqual(arithmetics.exponential(1, 2), 1)
        pass
    pass

unittest.main()

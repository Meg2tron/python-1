import unittest
import armstrong_number

class Armstrong_Number(unittest.TestCase):

    def testing_armstrong(self):
        self.assertEqual(armstrong_number.is_armstrong(371), True)
        pass

    def testing_non_armstrong(self):
        self.assertEqual(armstrong_number.is_armstrong(10), True)
        pass

    pass

unittest.main()

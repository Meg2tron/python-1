import unittest
import palindrome_checker

class Palindrome_Tester(unittest.TestCase):
    def testing_palindrome(self):
        self.assertEqual(palindrome_checker.check_palindrome("nitin"), True)
        pass

    def testing_non_palindrome(self):
        self.assertEqual(palindrome_checker.check_palindrome("tbhaxor"), False)
        pass



    pass

unittest.main()

import unittest
import lapindrome_checker

class Lapindrome_Tester(unittest.TestCase):
    def testing_easy_lapindrome(self):
        self.assertEqual(lapindrome_checker.check_lapindrome("xyzyx"), True)
        pass

    def testing_tricky_lapindrome(self):
        self.assertEqual(lapindrome_checker.check_lapindrome("abcafcbaa"), True)
        pass

    def testing_easy_non_lapindrome(self):
        self.assertEqual(lapindrome_checker.check_lapindrome("abc"), False)
        pass

    def testing_tricky_non_lapindrome(self):
        self.assertEqual(lapindrome_checker.check_lapindrome("abwceddaewb"), False)
        pass



    pass

unittest.main()

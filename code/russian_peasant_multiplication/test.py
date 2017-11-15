import unittest
import russian_peasant

class Russian_Peasant(unittest.TestCase):
    def testing_case1(self):
        self.assertEqual(russian_peasant.russian_peasant(6, 34), 204)
        pass

    def testing_case2(self):
        self.assertEqual(russian_peasant.russian_peasant(10, 34), 340)
        pass

    def testing_case3(self):
        self.assertEqual(russian_peasant.russian_peasant(6, 4), 24)
        pass

    def testing_case4(self):
        self.assertEqual(russian_peasant.russian_peasant(6, 0), 0)
        pass

    pass

unittest.main()

import unittest
import hello

class Test_Hello(unittest.TestCase):
    def testing_without_name(self):
        self.assertEqual(hello.say_hello(), "Hello, World!")
        pass

    def testing_with_name(self):
        name = "Gurkirat"
        self.assertEqual(hello.say_hello(name), "Hello, {}!".format(name))
    pass

unittest.main()

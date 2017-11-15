import unittest
import stack

# right side of the list is the top most element
class Stack_Test(unittest.TestCase):
    def test_case1(self):
        # declared an instance
        stk = stack.Stack()

        # pushing 3 value
        stk.push(1)
        stk.push(2)
        stk.push(3)

        # getting stack
        self.assertEqual(stk.get_stack(), [1,2,3])

        # poping element from stack
        self.assertEqual(stk.pop(), 3)

        # again getting top most element
        self.assertEqual(stk.get_top(), 2)
        pass


    def test_case2(self):
        # declared an instance
        stk = stack.Stack()

        # pushing 3 value
        stk.push(10)
        stk.push(20)
        stk.push(30)

        # getting stack
        self.assertEqual(stk.get_stack(), [10,20,30])

        # poping element from stack
        self.assertEqual(stk.pop(), 30)

        # again getting top most element
        self.assertEqual(stk.get_top(), 20)
        pass

    pass

unittest.main()

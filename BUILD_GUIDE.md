# What is Travis-CI and Why To Use ?
The simplest way to explain Travis CI is that it runs your program's tests every time you commit to GitHub. The point of this is that you can often discover very quickly if your commit broke something, and fix it before it becomes a problem

# What does assert do ?
Python’s assert statement is a debugging aid that tests a condition. If the condition is true, it does nothing and your program just continues to execute. But if the assert condition evaluates to false, it raises an AssertionError exception with an optional error message.

# What is unittest in python?
The Python unit testing framework (module name `unittest`), supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework

# Asserts in unittest module
```python
self.assertEqual(var1, var2, msg=None)
self.assertNotEqual(var1, var2, msg=None)
self.assertTrue(expr, msg=None)
self.assertRaises(exception, func, para, meters, ...)
```

# How To Use ?
**For every test file we will use self.assertEqual()**

1. Import unittest module
```python
import unittest
```
2. Import Program
```python
import <program_name>
```
3. Create a class in python of any name for eg: Testing_Program and inherit unittest.TestCase and add methods with `testing_` as prefix
```python
class Testing_Program(unittest.TestCase):
  def testing_case1(self):
    self.assertEqual(<program_name>.<function_name>(values1, values2 ...),  <expected answer>)
  pass
```
4. Calling  `unittest.main()`
```python
unittest.main()
```

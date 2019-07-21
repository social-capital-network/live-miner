import unittest

class CheckNumbers(unittest.TestCase):
    def test_int_float(self):
        self.assertEqual(1, 1.0)

if __name__ == "__main__":
    unittest.main()

# from
# Phillips, Dusty. Python 3 Object-Oriented Programming: Build robust and maintainable software with object-oriented design patterns in Python 3.8, 3rd Edition (pp. 372-373). Packt Publishing. Kindle Edition. 

# Running all tests:
# python -m unittest discover

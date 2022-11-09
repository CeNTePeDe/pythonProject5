import unittest
from first_programm.LogFactorial import factorial

class FactorialTestCase(unittest.TestCase):
    def test_fact(self):
        res = factorial(4)
        self.assertEqual(24, 24)

    def test_error(self):
        with self.assertRaises(TypeError) as e:
            res = factorial(0.4)
            self.assertEqual("вводимые данные должны быть целочисленные", e.exception.args[0])
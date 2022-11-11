import unittest
import doctest
from first_programm.LogFactorial import factorial
import first_programm.LogFactorial as LogFactorial


def load_tests(loader, tests, ignore):
    """ Данная функция нужна, для того чтобы запукстить doctest"""
    tests.addTests(doctest.DocTestSuite(LogFactorial))
    return tests

class FactorialTestCase(unittest.TestCase):
    def test_fact(self):
        res = factorial(4)
        self.assertEqual(24, 24)

    def test_error_type(self):
        with self.assertRaises(ValueError) as e:
            res = factorial(0.4)
            self.assertEqual("вводимые данные должны быть целочисленные", e.exception.args[0])

    def test_error_value(self):
        with self.assertRaises(ValueError) as e:
            res = factorial(-5)
            self.assertEqual("вводимые данные должны быть неотрицательные", e.exception.args[0])

if __name__ == '__main__':
    unittest.main()

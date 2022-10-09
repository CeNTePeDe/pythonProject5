import unittest
from testing_prog.count_square import square_eq_solver


class SquareEqSolverTestCase(unittest.TestCase):
    def test_no_root(self):
        res = square_eq_solver(10, 0, 2)
        self.assertEqual(len(res), 0)

    def test_single_root(self):
        res = square_eq_solver(10, 0, 0)
        self.assertEqual(len(res), 1)
        self.assertEqual(res, [0])

    def test_multiple_root(self):
        res = square_eq_solver(2, 5, -3)
        self.assertEqual(len(res), 2)
        self.assertEqual(res, [0.5, -3])

    def test_error(self):
        with self.assertRaises(AttributeError) as e:
            res = square_eq_solver(0.1, 0.5, -3)
            self.assertEqual("вводимые данные должны быть целочисленные", e.exception.args[0])



    #def no_sight(self):
    #    with self.assertRaises(ValueError) as e:
#



if __name__ == '__main__':
    unittest.main()

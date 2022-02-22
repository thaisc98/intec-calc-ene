import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_suma(self):
        self.assertEqual(4, self.calc.sumar(2, 2))
        self.assertEqual(13, self.calc.sumar(1, 12))
        self.assertEqual(1100, self.calc.sumar(100, 1000))
        self.assertEqual(0, self.calc.sumar(0, 0))
        self.assertEqual("Invalid", self.calc.sumar(1, -1))
        
    def test_Multiplicar(self):
        self.assertEqual(6, self.calc.Multiplicar(2, 3))
        self.assertEqual(12, self.calc.Multiplicar(3, 4))
        self.assertEqual(100, self.calc.Multiplicar(50, 2))
        self.assertEqual(0, self.calc.Multiplicar(5, 0))
        self.assertEqual("Invalid", self.calc.Multiplicar(3, -2))

if __name__ == '__main__':
    unittest.main()
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
        

    def test_multiplicar(self):
        self.assertEqual(6, self.calc.multiplicar(2, 3))
        self.assertEqual(12, self.calc.multiplicar(3, 4))
        self.assertEqual(100, self.calc.multiplicar(50, 2))
        self.assertEqual(0, self.calc.multiplicar(5, 0))
        self.assertEqual("Invalid", self.calc.multiplicar(3, -2))
        
    def test_resta(self):
        self.assertEqual(0,self.calc.restar(2, 2))
        self.assertEqual(10,self.calc.restar(20, 10))
        self.assertEqual(-200,self.calc.restar(100, 300))
        self.assertEqual(350,self.calc.restar(400, 50))
        self.assertEqual("Invalid",self.calc.restar(1, -1))

    def test_divide(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(2, self.calc.divide(4, 2))
        self.assertEqual("Invalid", self.calc.sumar(1, -1))


if __name__ == '__main__':
    unittest.main()
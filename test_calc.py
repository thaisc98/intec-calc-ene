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

    # Tests for the square function
    def test_square_should_return_4(self): 
        self.assertEqual(4, self.calc.square(2))

    def test_square_should_return_16(self): 
        self.assertEqual(16, self.calc.square(4))
        
    def test_square_should_return_25(self): 
        self.assertEqual(25, self.calc.square(5))
        
    def test_square_should_return_100(self): 
        self.assertEqual(25, self.calc.square(5))
        
    def test_square_should_return_Invalid(self): 
        self.assertEqual("Invalid", self.calc.square(-3))
    # Finishing tests for the square function 


if __name__ == '__main__':
    unittest.main()
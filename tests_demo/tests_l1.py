import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
    
    def test_sum(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.get_sum(),10, 'The sum is wrong')
        
    def test_diff(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.get_difference(),6, 'The difference is wrong')
        
    def test_product(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.get_product(),16, 'The product is wrong')
        
    def test_quotient(self):
        calculation = Calculator(8,2)
        self.assertEqual(calculation.get_quotient(),4, 'The quotient is wrong') 
         
 
if __name__ == '__main__':
    unittest.main()
        
        
#assertEqual(a, b) a == b
#assertNotEqual(a, b) a != b
#assertTrue(x) bool(x) is True
#assertFalse(x) bool(x) is False
#assertIs(a, b) a is b
#assertIsNot(a, b) a is not b
#assertIsNone(x) x is None
#assertIsNotNone(x) x is not None
#assertIn(a, b) a in b
#assertNotIn(a, b) a not in b#
#assertIsInstance(a, b) isinstance(a, b)
#assertNotIsInstance(a, b) not isinstance(a, b)
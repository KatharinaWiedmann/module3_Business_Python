# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 09:55:46 2019

@author: Katharina
"""
import unittest 
from calculator import Calculator 

class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator() 
    
    def test_calculator_add_method_returns_correct_result(self):
#        result = self.calc.add(2,2)
#        self.assertEqual(4, result)
#        shorter version: 
        self.assertEqual(self.calc.add(2,2), 4)
    def test_calculator_returns_error_message_if_both_args_no_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
    def test_calculator_returns_error_message_if_x_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
    def test_calculator_returns_error_message_if_y_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')
        
        
if __name__ == '__main__':
    unittest.main()
    

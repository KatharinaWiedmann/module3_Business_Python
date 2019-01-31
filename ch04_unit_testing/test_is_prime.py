# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:51:27 2019

@author: Katharina
"""

import unittest
from is_prime import is_prime 
import sys 
#
##without classes (easiest form):
#unittest.TestCase.assertTrue(is_prime(5))
#
#
#class prime_test(unittest.TestCase):
#    def test_prime(self):
#        self.assertTrue(is_prime(5))
#        #self.assertTrue(is_prime(sys.argv[1]))       
#        #sys.argv[1] tests for input that user gives, whereas is_prime(5) only tests for 5 
##        
##    def sys_input(self):
##        self.assertIsInstance(sys.argv[1], int)
##        
#if __name__ == "__main__":
#    prime_test.test_prime()
##if.... calls all the functions in the file



class PrimesTest(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(5))

#is_prime(5.3) gives Error
#is_prime(5.0)  gives OK 


if __name__ == "__main__":
    unittest.main()
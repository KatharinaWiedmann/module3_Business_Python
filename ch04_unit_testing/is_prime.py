# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 09:44:24 2019

@author: Katharina
"""

def is_prime(number):
    """Return True if number is prime"""
    #Has to start at 1 or 2, as cannot be divided by 0!! 
    for element in range(2, number):
        if number %  element == 0:
            return False
    return True
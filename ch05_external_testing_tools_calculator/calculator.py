# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:41:28 2019

@author: Katharina
"""

class Calculator():
    def add(self, x, y):
        number_types = (int, float, complex)
        if isinstance(x, number_types) and isinstance (y, number_types):
            #only for debugging
#            import pdb; pdb.set_trace()
            result = x - y 
            print('Result is:{}'.format(result))
            return result
        else:
            raise ValueError
    
        
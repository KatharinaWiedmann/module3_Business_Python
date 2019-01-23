# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:40:27 2019

@author: Katharina
"""
## ------------------------NOTES ----------------------------------------------------##
##FIRST TRY 
#try:
#    f = open('testfile')
#except Exception:
#    print('This file does not exist or the file name is wrong. Please doube check.')
#    
#    
#    
##SECOND TRY   
#try:
#    f = open('testfile.txt')
#    s1 = not_exists
#
#except Exception:
#    print('Error')
#
##THIRD TRY -- now sees tha problem is not that it can't open the file but it sees that the variable 's1' i not defined 
#try:
#    f = open('testfile.txt')
#    s1 = not_exists
#
#except FileNotFoundError:
#    print('Error')
#    
##FOURTH TRY: -- you can open it but there is a problem after opening it (as can't find s1)
#try: 
#    f = open('testfile.txt')
#    s1 = not_exists
#except FileNotFoundError:
#    print('Sorry, this file does not exist or the file name is wrong. Please doule check.')
#except Exception:
#    print('Something is wrong after opening function.')


##-------------------------END OF NOTES ----------------------------------------------##    
    
#TASK 1: -- doesn't print Error message anymore. 
try:
    f = open('testfile.txt')
except Exception:
    print('This file does not exist or the file name is wrong. Please doube check.')
    


##TASK 2: -- you can open it but there is a problem after opening it (as can't find s1)
try: 
    f = open('testfile.txt')
    s1 = not_exists
except FileNotFoundError:
    print('Sorry, this file does not exist or the file name is wrong. Please doule check.')
except Exception:
    print('Something is wrong after opening function.')
    
    
    
    
##TASK 3: -- prints exception if after opening something within the doc is wrong --> as it can't find s1 it will print the corresponding message --> that it can't find s1
try:
    f=open('testfile.txt')
    s1 = not_exist
except Exception as e:
    print(e)
    
    
    
##TASK 4: --else block runs if try block doesn't raise an exception
#         -- here else bock will be executed --> opens the test file and pronts whats inside 
try:
    f = open('testfile.txt')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
    
    
##TASK 5: -- finally block run regardless of whether try block is successfull or not 
#         -- doesn't find the file if "testfile" prints error message and "executing finally"
#         -- if testfile.txt will open and print what's insde the testfile and "executing finally"
try:
    f = open('testfile')
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('executing finally..')
    
    
##TASK 6: --manually raises Exception (but ony if if statement is true! otherwise nothing happens )

try: 
    f = open('testfile.txt')
    if f.name == 'testfile.txt':
        raise Exception
except Exception as e:
    print('file names are the same')
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 09:27:38 2019

@author: Katharina
"""
#TASK1/TASK2 : Revising user input 
age = int(input("What's your age? "))

#TASK 3: saves user input starting with lower case letter 
option = input("Please enter yes or no ").lower()
print(option)


#TASK 4: Try to get a user input with certain length
while True:
    userInput = input('Do you like dogs? Please only type yes or no. ')
    if len(userInput) <= 3:
        print('Thanks I have saved your answer')
        break
    else:
        print('Please only type in yes or no ')
       
 
#TASK5: Using a while infinite loop 
        
print('*******choice**********')
print('1) Display my name')
print('2) Display my age')
print('3) Display my city')
choice = 0

while True:    
    choice = int(input('Please choose a number between 1-3 '))
    while choice < 1 or choice> 3:
        print('What is your choice? ')
        break
    if choice == 1:
        print('Ms Wu')
        break
    elif choice == 2:
        print('5 years old')
        break
    elif choice == 3:
        print('London')
        break
    
    
#Task6: Extension to TASK 5 --> What if user inputs e.g. 'three'     
print('*******choice**********')
print('1) Display my name')
print('2) Display my age')
print('3) Display my city')
choice = 0


while True: 
    try:
        #remember that choice = 0 (initialized above), so will enter the first while loop and ask for new choice as long as choice is not between 1-3
        while choice < 1 or choice> 3:
            choice = int(input('Please choose a number between 1-3 '))
        break
    except ValueError:
        print('Please type a number ')
              
        
if choice == 1:
    print('Ms Wu')
elif choice == 2:
    print('5 years old')
elif choice == 3:
    print('London')





TASK 7: Class-based user input validation
Option 1 - if statement makes sure that there is a description and a value bigger than 0, otherwise will raise a ValueError  
class Spam(object):
    def __init__(self, description, value):
        if not description or value <= 0:
            raise ValueError
        self.description = description
        self.value = value

s = Spam('', -5)

#Option 2 - assert statements make sure that conditions are met otherwise AssertionError
class Spam(object):
    def __init__(self, description, value):
        assert description !=""
        assert value > 0
        self.description = description 
        self.value = value

#s = Spam('s', 3)
s = Spam('', -5)






























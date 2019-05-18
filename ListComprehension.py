"""
Demo of different types List comprehension in python
"""


"""Below is basic list comprehension
"""
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

square = [ n*n for n in numbers]
print(square)


"""Conditionaly pick elements in list
    1. Also we can use functions 
"""

def minus1(nm):
    return nm-1

evenMinus1 = [ minus1(n) for n in numbers if n%2 ==0]
print(evenMinus1)








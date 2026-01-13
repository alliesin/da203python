# -*- coding: utf-8 -*-
"""
DA 203/MDA 600 Assignment 4

"""
# %%
"""
Problem 1. Write a python script point.py. Create a Point class, a Shape 
class, a Line class, and a Rectangle class. 

a. A point is a tuple of two integers, e.g. (3, 5).
b. Add a move method to the Point class that receives dx and dy, which
   are the amounts of change to apply to the point. Example: passing 
   (-2, 4) to the method will turn the point from (3, 5) to (1, 9).
c. The Shape class has p1 and p2 two attributes, representing two 
   points. Its area method is blank. 
d. The Line class inherits from Shape. A line is determined by its 
   two end points, e.g. (3, 5) and (1, 6).
e. Add a length method to the Line class return the length of a line.
f. The Rectangle class also inherits from Shape. A rectangle with 
   horizontal and vertical sides is determined by its upper right point 
   and the lower left point.
g. Add attributes width and height to the Rectangle class. Override the 
   area method and add a perimeter method to the Rectangle class. 
h. For all these classes, add a special method __str__ to return a string
   representation of an object.
i. Overload the subtraction (-) operator for the Point class to return a 
   tuple that stores the difference of two points. Use this overloaded 
   operator when calculating the length of a line.
   
Use the following code to test.

p1 = Point(3, 5)
p2 = p1.move(-2, 4)
print(p1, p2)
s1 = Line(p1, p2)
print(s1)
print(round(s1.length(), 2))
r1 = Rectangle(p1, p2)
print(r1.perimeter())
print(r1.area())


"""
# point.py

pass

# %%
"""
Problem 2. Write a python script frac.py. Define a fraction 
class that will overload the +, -, *, /, and == operators. Determine 
which additional methods you will need. For instance, you will need 
LCD (Least Common Demonimator) and LCM (Least Common Multiple) in 
fraction addition, subtraction or simplification.    

Test 1: Run your program from the command line:
    frac 1/2 - 3/8
    
Test 2: Read the following expressions from a file and parse each line:
    1/2 + 3/4
    5/6 - 1/2
    3/4 * 6/7
    3/5 / 2/5

"""
# frac.py

pass
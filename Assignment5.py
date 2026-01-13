# -*- coding: utf-8 -*-
"""
"""

# Assignment 5.py

# %%
"""
Q1. Write a class Counter iterator that:
- accepts a starting value and an ending value
- produces numbers from start to end inclusive
- implements the iterator protocol (__iter__ and __next__)

Sample code:
    
for i in Counter(2, 5):
    print(i)
    
Sample output: 2 3 4 5.
"""

class Counter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.start <= self.end:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
    
# %%
'''
Q2. Write a generator function even_numbers(limit) that 
yields all even numbers from 0 up to limit (inclusive).

Sample code: list(even_numbers(10))
Sample outputs: [0, 2, 4, 6, 8, 10].
'''
def even_numbers(limit):
    num = 0
    while num <= limit:
        yield num
        num += 2
        

# %%
'''
Q3. Create a class DataStream that:
- takes a list of numbers
- stores them in the instance via __dict__
- provides a generator method .positive() that yields 
only positive numbers
- implements an iterator that iterates over the original list

Sample code: 
ds = DataStream([-1, 3, -2, -5, 4, 2])
for x in ds.positive():
    print(x, end=' ')
    
Sample output: 3 4 2

Sample code:
for x in ds:
    print(x, end=' ')
    
Sampe output: -1 3 -2 -5 4 2
'''

class DataStream:
    def __init__(self, aLst):
        self.lst = aLst     #initializing like this stores it in the instance with __dict__ regardless I think
    
    def __iter__(self):
        return iter(self.lst)
    
    def positive(self):
        for x in self.lst:
            if x > 0:
                yield x

# %%
'''
Q4. Create a class Student with:
- a class attribute school = "Python Academy"
- private attributes __name and __gpa
- property gpa with:
getter (returns GPA)
setter (ensures GPA is between 0.0 and 4.0)
deleter (sets GPA to None)
- a method info() that returns all student data

Sample code: 
s = Student('Alice', 3.0)
print(s.info())
del s.gpa
print(s.gpa)
s.gpa = 5.0

'''
class Student:
    school = "Python Academy"
    def __init__(self, name, gpa):
        self.__name = name
        self.__gpa = gpa
    
    @property
    def gpa(self):
        return self.__gpa
    
    @property
    def name(self):
        return self.__name
    
    @gpa.setter
    def gpa(self, x):
        if (x != None) and (x > 4.0 or x < 0):
            raise ValueError("GPA out of range.")
        self.__gpa = x
        
    @gpa.deleter
    def gpa(self):
        self.gpa = None
        
    def info(self):
        return self.name, self.gpa, self.school
        
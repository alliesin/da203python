# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 13:20:29 2025

@author: Allie
"""

class Vector:

    def __init__(self, *args):
        #if no values are given, default
        if len(args) == 0: 
            self.values = (0,0)
        else: 
            self.values = args
    
    def __str__(self):
        # ex: Vector(1, 2)
        return f"Vector{self.values}"
    
    def __repr__(self):
        # ex: (1, 2)
        return str(self.values)
    
    def __iter__(self):
        #iterate through the class, needed for functions to work
        return iter(self.values)
    
    def __len__(self):
        #size of Vector
        return len(self.values)
    
    def __getitem__(self, index):
        #allows indexing and slicing
        if isinstance(index, slice):
            return Vector(*self.values[index])
        return self.values[index]
    
    def __setitem__(self, index, value):
        #replace a value
        setLst = list(self.values)
        setLst[index] = value
        self.values = tuple(setLst)
    
    def __add__(self, other):
        #add two Vectors of same length or add constant to all values of one Vector
        if len(self) == len(other.values):
            if isinstance(other, Vector):
                added = tuple(a + b for a, b in zip(self, other))
            elif isinstance(other, (int,float)):
                added = tuple(a + other for a in self)
            else:
                raise ValueError("Unable to add with your type.")
        else:
            raise Exception("Cannot add vectors of differing sizes.")
        return Vector(*added)

    def __sub__(self, other):
        #subtract two Vectors of same length or subtract constant to all values of one Vector
        if len(self) == len(other.values):
            if isinstance(other, Vector):
                subbed = tuple(a - b for a, b in zip(self, other))
            elif isinstance(other, (int, float)):
                subbed = tuple(a - other for a in self)
            else:
                raise ValueError("Unable to subtract with your type.")
        else:
            raise Exception("Cannot subtract vectors of differing sizes.")
        return Vector(*subbed)
    
    def __mul__(self, other):
        #scalar multiplication
        if isinstance(other, (int, float)):
            multiplied = tuple(a * other for a in self)
        else:
            raise ValueError("Unable to multiply with your type.")
        return Vector(*multiplied)
    
    def __truediv__(self, other):
        #scalar division
        if isinstance(other, (int, float)):
            divided = tuple(a / other for a in self)
        else:
            raise ValueError("Unable to divide with your type.")
        return Vector(*divided)
        
    def __radd__(self, other):
        #needed for sum
        return self.__add__(other)
    
    def __rmul__(self, other):
        #just in case lol
        return self.__mul__(other)
        
    def dotprod(self, other):
        #dot product of two Vectors same size
        if isinstance(other, Vector):
            if len(self) == len(other.values):
                mult = [a * b for a, b in zip(self, other)]
                dotprod = sum(mult)
                return dotprod
            else:
                raise Exception("Cannot compute dot product of differing Vector sizes.")
        else:
            raise ValueError("Cannot take dot product of type other than Vector.")
                
    def cumsum(self):
        #cumulative sum of values in one Vector
        cumsumLst = []
        total = 0
        for num in self.values:
            total += num
            cumsumLst.append(total)
        return tuple(cumsumLst)
                 
    def cumprod(self):
        #cumulative product of values in one Vector
        cumprodLst = []
        total = 1
        for num in self.values:
            total *= num
            cumprodLst.append(total)
        return tuple(cumprodLst)
    
    def mean(self):
        #average of values in Vector
        return (sum(self.values) / len(self))
        
    def std(self):
        #population standard deviation of values in Vector
        from math import sqrt
        mean = (sum(self.values) / len(self))
        totalnum = len(self)
        temp = list(float(num) for num in self.values)
        var  = sum(pow(num-mean,2) for num in temp) / totalnum
        return round(sqrt(var), 3) #rounded to 3 decimal points

    def __max__(self):
        #maximum value in a Vector
        return max(self.values)
        
    def __min__(self):
        #minimum value in a Vector
        return min(self.values)
        
    def argmax(self):
        #index of maximum value in a Vector
        return (self.values).index(max(self))
    
    def argmin(self):
        #index of minimum value in a Vector
        return (self.values).index(min(self))
    
    def magnitude(self):
        return sum(abs(num) for num in self.values)
        
        
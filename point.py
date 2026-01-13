# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 00:40:09 2025

@author: Allie
"""
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def __sub__(self, other):
        return (abs(self.x - other.x), abs(self.y - other.y))
    
    def __str__(self):
        return f'Point({self.x}, {self.y})'
        
class Shape:
    
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def area(self):
        return 0
    
    def __str__(self):
        return f'Shape({self.p1}, {self.p2})'
    
class Line(Shape):

    def __init__(self, p1, p2):
        super().__init__(p1, p2)
    
    def length(self):
        dx, dy = self.p1 - self.p2
        #hypotenuse
        return (dx**2 + dy**2) ** 0.5
    
    def __str__(self):
        return f'Line({self.p1}, {self.p2})'
        
class Rectangle(Shape):
    
    def __init__(self, p1, p2):
        super().__init__(p1, p2)
        
    def area(self):
        width, height = (self.p1 - self.p2)
        return (width * height)
        
    def perimeter(self):
        width, height = (self.p1 - self.p2)
        return ((width * 2) + (height * 2))
        
    def __str__(self):
        return f'Rectangle({self.p1}, {self.p2})'
        
        
        
        
    
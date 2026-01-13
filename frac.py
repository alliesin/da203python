# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 00:14:53 2025

@author: Allie
"""
from math import gcd

def lcm(a, b):
    if a == 0 or b == a:
        return 0
    return abs(a * b) // gcd(a, b)

def simplify(a, b):
    lcd = lcm(a, b)
    f1 = lcd / a
    f2 = lcd / b
    return lcd, f1, f2

class Fraction:
    
    def __init__(self, num, denom):
        if denom < 0:
            num *= -1
            denom *= -1
        self.num = num
        self.denom = denom
                
    def __str__(self):
        return f'{self.num}/{self.denom}'
    
    #override math
    
    def __add__(self, other):
        if self.denom != other.denom:
            lcd, f1, f2 = simplify(self.denom, other.denom)
            return Fraction(int(self.num * f1 + other.num * f2), lcd)
        else:
            return Fraction(self.num + other.num, self.denom)
    
    def __sub__(self, other):
        if self.denom != other.denom:
            lcd, f1, f2 = simplify(self.denom, other.denom)
            return Fraction(int((self.num * f1) - (other.num * f2)), lcd)
        else:
            return Fraction(self.num - other.num, self.denom)
        
    def __mul__(self, other):
        num = self.num * other.num
        denom = self.denom * other.denom
        g = gcd(num, denom)
        return Fraction(num // g, denom // g)
    
    def __truediv__(self, other):
        num = self.num * other.denom
        denom = self.denom * other.num
        g = gcd(num, denom)
        return Fraction(num // g, denom // g)
    
    def __eq__(self, other):
        firstnum = self.num * other.denom
        secondnum = other.num * self.denom
        return firstnum == secondnum
    
with open("C:\\Users\\Pinea\\Downloads\\fractions.txt", 'rt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split()
        f1 = Fraction(int(line[0][0]), int(line[0][2]))
        f2 = Fraction(int(line[2][0]), int(line[2][2]))
        match line[1]:
            case '+':
                ans = f1 + f2
            case '-':
                ans = f1 - f2
            case '*':
                ans = f1 * f2
            case '/':
                ans = f1 / f2
            case _:
                print("something went wrong")
        print(ans)
        
        
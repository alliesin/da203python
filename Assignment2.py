# -*- coding: utf-8 -*-
"""
Spyder Editor

DA 203/MDA 600 Assignment 2

For Problems 2 to 7, define functions and call the functions as
test cases. For Problem 7, use the sample.txt file associated with
this assignment.

"""

# %% Level 1
"""
Problem 1. Mike has decided to take out a 30-year fixed rate 
mortgage of $500,000. The interest rate (APR) is 8%.  (a) How much 
is the monthly payment? (b) If Mike plans to pay an extra $200 per 
month for the first 18 months of the mortgage, how many months in total
will he need to pay off the mortgage? How much is the payment that 
he will make in the last month? 
   
"""
P = 500000
r = 0.08/12
n  = 360
M = P*(r*(1+r)**n)/((1+r)**n-1)
print(f'The monthly payment will be ${round(M, 2)}.')
month = 0
for i in range(1, 19):
    month += 1
    interest = P * r
    payment = M + 200
    if payment > P + interest:
        payment = P + interest
    P -= (payment - interest)
while P >= M:
    month += 1
    interest = P * r
    payment = M
    if payment > P + interest:   # last payment
        payment = P + interest
    P -= (payment - interest)
print(f'If Mike plans to pay an extra $200 per month for the first 18 months, it will take him {month} months. His last payment will be ${round(P, 2)}.')



# %% Level 1
"""
Problem 2. Define a function revsubStr(a, b, c) that reverses all  
characters in a string after replacing all instances of character b 
with character c. Sample: revsubStr('ABCqdefq', 'q', 'k') will return 
'kfedkCBA'.  
       
"""
def revsubStr(a, b, c):
    text = a.replace(b, c)
    revText = text[::-1]
    print(revText)


# %% Level 1
"""
Problem 3. In number theory, a perfect number is a positive integer 
that is equal to the sum of its proper positive divisors, that is, 
the sum of its positive divisors excluding the number itself. Define 
a function isPerfect(n) that returns True if n is a perfect number 
or False otherwise. Sample: isPerfect(6) will return True and 
isPerfect(10) will return False.
   
"""
def isPerfect(n):
    total = 0
    for div in range (1, n):
        if n % div == 0:
            total += div
    if n == total:
        return True
    else:
        return False
    

# %% Level 1
"""
Problem 4. Define a function isPangrams(s) that checks whether a string 
s is a pangram or not. Pangrams are words or sentences containing every 
letter of the alphabet at least once. Hint: consider using the 
constant ascii_letters defined in the string module.
   
"""
import string
def isPangrams(s):
    for x in string.ascii_letters[:26]:
        if s.lower().count(x) == 0:
            return False
    return True

# %% Level 1
"""
Problem 5. Define a function cumTotal(a) that returns a list of 
cumulative totals of list a. Sample: cumTotal([2, 3, 5]) will return
[2, 5, 10]. 
   
"""
def cumTotal(a):
    newAList = []
    total = 0
    for num in a:
        total += num
        newAList.append(total)
    return newAList
    

# %% Level 1
"""
Problem 6. Define a function sortedList(aLst) that returns a list of 
distinct numbers in an integer list aLst in ascending order. Sample: 
sortedList([5, 2, 3, 2, 6, 1, 9]) will return [1, 2, 3, 5, 6, 9].
   
"""
def sortedList(aLst):
    aSet = set(aLst)
    print(sorted(aSet))

# %% Level 1
"""
Problem 7. Define a function lines(fname) that returns the number of lines
in a text file. Sample: Lines('sample.txt') will return 5.
   
"""
fname = 'C:\\Users\\Pinea\\Downloads\\sample.txt'
def lines(fname):
    ctr = 0
    with open(fname, 'r') as file:
        for line in file:
            ctr += 1
    print(ctr)
    

# -*- coding: utf-8 -*-
"""
Spyder Editor

DA 203 Assignment 1
"""

# %% Level 1
"""
Problem 1. Write a for loop to output the following pattern:

********
*******
******
*****
****
***
**
*    
   
"""

for i in range (8, 0, -1):
    print("*" * i)


# %% Level 1
"""
Problem 2. Write a for loop to output the following pattern:

***********
 *********
  *******
   *****
    ***
     *
       
"""
star = 11
print ("*" * star)
for i in range (5):
    star -= 2
    print (" " * i,"*" * (star)," " * i)

        

# %% Level 1
"""
Problem 3. Write a for loop to output the following pattern:

*******
 *****
  ***
   *
  ***
 *****
*******
   
"""
star = 7
print ("*" * star)
for i in range(3):
    star -= 2
    print (" " * i, "*" * star, " " * i)
for i in range(3, 1 ,-1):
    star += 2
    print (" " * (i-2), "*" * star, " " * i)
print ("*" * 7)
    

# %% Level 1
"""
Problem 4. Write a while loop to find the smallest integer n such 
that 1 + 2 + 3 + ... + n > 2000.
   
"""
n = 1
total = 0

while total <= 2000:
    total += n
    n += 1
print(n - 1)

# %% Level 1
"""
Problem 5. A rubber ball is dropped from a height of 150 meters 
and each time it hits the ground, it bounces back up to 3/5 the 
height it fell. Write a code snippet to compute the number of 
bounces after which its height will drop below 10 meters forever.
   
"""
height = 150
bounce = 0
while height > 10:
    height *= 0.6
    bounce += 1
print ("After", bounce, "bounces, the ball will bounce below 10 meters.")
    

# %% Level 1
"""
Problem 6. How many integers between 100 and 500 are divisible 
by 11 but not by 2?
   
"""
intCt = 0
for i in range(100, 501):
    if i % 11 == 0:
        if not(i % 2 == 0):
            intCt += 1
print(intCt, "integers")

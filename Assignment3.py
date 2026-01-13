# -*- coding: utf-8 -*-
"""
DA 203/MDA 600 Assignment 3

"""
# %% Level 1
"""
1. Write a function sum_digits(aLst) that returns
the sum of the number digits in a list. Sample: 
sum_digits([12, 234, 56, 4]) returns 27.

"""
def sum_digits(lst):
    stringLst = []
    for d in lst:
        stringLst.append(str(d))
    string = ''.join(stringLst)
    digitsLst = []
    for digit in string:
        digitsLst.append(int(digit))
    return sum(digitsLst)

# %% Level 1
"""
2. Write a function ind_nth_largest(aLst, n = 1) 
that returns the index of the n_th largest number
in a list. If there are multiple occurrences, 
the index of the first occurrence should be returned. 
The function returns a warning message if the n_th 
largest number does not exist. 

Sample: ind_nth_largest([1, 2, 2, 5, 6, 6], 2) returns
3. 

Sample: ind_nth_largest([1, 2, 2, 5, 6, 6], 7) returns
'Fewer than 7 distinct values'.

"""
def ind_nth_largest(lst, n = 1):
    sortLst = sorted(set(lst), reverse=True)
    if n > len(sortLst):
        return f"Warning: Fewer than {n} distinct values."
    nth_largest_value = sortLst[n-1]
    return lst.index(nth_largest_value)
    

# %% Level 1
"""
3. Write a function value_counts(aLst) that 
returns a list of tuples [(a_1, f_1), (a_2, f_2), 
...], where a_i is a distinct number in aLst,
f_i is the corresponding frequency. a_i's are sorted
in descending order of frequency. If two or more numbers
have the same frequency, then they will be 
sorted in descending order of their magnitude. 

Sample: value_counts([1, 3, 3, 4, 5]) returns
[(3, 2), (5, 1), (4, 1), (1, 1)]

"""
from collections import Counter, OrderedDict
def value_counts(aLst):
    countDict = Counter(aLst)
    orderedCountDict = OrderedDict(sorted(countDict.items(), reverse = True))
    revSort = {k: v for k, v in sorted(orderedCountDict.items(), key=lambda item: item[1], reverse=True)}
    tupled = list(revSort.items())
    return(tupled)

# %% Level 1
"""
4. Write a function key_max_unique(aDict) that accepts 
a dictionary consisting of key-list pairs and returns 
the key that has the highest number of distinct values in
its list. Return a list of the max keys if there are ties.

Sample: 
aDict = {'a': [1, 2, 3, 3, 6],
         'b': [1, 4, 4],
         'c': [3, 4, 4, 5]}
key_max_unique(aDict) returns 'a'.

Sample: 
aDict = {'a': [1, 2, 3, 3],
         'b': [1, 4, 4],
         'c': [3, 4, 4, 5]}
key_max_unique(aDict) returns ['a', 'c'].

"""

def key_max_unique(aDict):
    uniqueNums = {key: len(set(values)) for key, values in aDict.items()}
    maxNums = max(uniqueNums.values())
    return [key for key, count in uniqueNums.items() if count == maxNums]
    


# %% Level 1
"""
5. Use the python file handling tool to read 
the data in portfolio.csv (in the python-practical-main 
repository), store the data in a list of tuples, and 
then convert it into a list of dictionaries with name, 
shares, price and value as the keys. Finally, 
use pprint.pprint to output the resulting list.
Use the zip and dict functions to create
dictionaries. Note: value = price * shares.

"""
import csv
with open('portfolio.csv', 'rt') as f:
    data = csv.reader(f)
    row_ind = 0
    lst = []
    for row in data:
        if row_ind == 0:
            header = row
            header.append("value")
            row_ind += 1
        else:
            lst.append((row[0], int(row[1]), float(row[2]), (int(row[1])*float(row[2]))))
            row_ind += 1
    dict_lst = [dict(zip(header, y)) for y in lst]
    print(dict_lst)
    

# %% Level 1
"""
6. Use csv.reader to read the data in portfoliodate.csv, 
and store the data in a dictionary with key-list pairs.
There is a key per stock. Each transaction including 
date, time, shares and price is stored as a tuple in 
the corresponding list. Finally, use pprint.pprint to 
output the resulting dictionary. You don't have to
cast shares and price into numeric types. Note: the list 
for IBM or MSFT has two tuples.

"""
import csv
aDict = {}
with open('portfoliodate.csv', 'rt') as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        name = row[0]
        date = row[1]
        time = row[2]
        shares = row[3]
        price = row[4]
        tupled = (date, time, shares, price)
        if name in aDict:
            aDict[name].append(tupled)
        else:
            aDict[name] = [tupled]
print(aDict)
    
    
    
    

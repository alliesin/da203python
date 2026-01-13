# -*- coding: utf-8 -*-
"""
# Assignment 6
"""

# %%
'''
1. Define a calculator function that can handle 
variable number of arguments, operations 'add', 
'multiply' and 'average', and the following options:
- 'round_digits': number of decimal places to round to
- 'ignore_negative': if True, ignore negative numbers

Sample code:
calculator('add', 1, 2, 3) → 6
calculator('multiply', 2, 3, 4) → 24
calculator('average', 1, 2, 3, round_digits=2) → 2.0
calculator('add', 1, -2, 3, -4, ignore_negative=True) → 4
'''

def calculator(function, *nums, ignore_negative = False, round_digits=5):
    match function:
        case 'add':
            if ignore_negative == True:
                    nums = [num for num in nums if num > 0]
            return sum(nums)
        case 'multiply':
            if ignore_negative == True:
                    nums = [num for num in nums if num > 0]
            res = 1
            for num in nums:
                res = res * num
            return res
        case 'average':
            avg = sum(nums) / len(nums)
            return round(avg, round_digits)

# %%
'''
2. Create a counter function 
`create_counter(initial_value=0, step=1)` that remembers 
its state using closure. The returned function should:
- When called with no arguments, return the state after incrementing
- When called with 'reset', reset the state to initial_value
- When called with 'set', set the state to provided value
- When called with 'get', return current state without incrementing
    
Sample code:
counter = create_counter(10, 2)
counter() → 12
counter() → 14
counter('get') → 14
counter('reset') → 10
counter('set', 5) → 5
'''

def create_counter(initial_value=0, step=1):
    state = [initial_value]
    def counter(*grs):
        if len(grs) > 0:
            match grs[0]:
                case 'get':
                    return state[0]
                case 'reset':
                    state[0] = initial_value
                    return state[0]
                case 'set':
                    state[0] = grs[1]
                    return state[0]
        else:
            state[0] += step
        return state[0]
    return counter
        
# %%
'''
3. Create a function decorator `call_logger(func)` that logs 
function calls with their arguments and return values.
Requirements:
- Log function name when called
- Log arguments and keyword arguments
- Log return value
- Use a consistent format

Sample output:
"Call: multiply(5, y=3)"
"RETURN: multiple -> 15"

'''

def call_logger(func):
    def wrapper(*args, **kwargs):
        print('Call:', func.__name__, '(arguments:', *args, 'keyword arguments:', kwargs, ')')
        value = func(*args, **kwargs)
        print('RETURN:', func.__name__, '-> ', value)
    return wrapper

# %%
'''
4. Create a BankAccount class with the following 
requirements:
- Define a constructor to initialize the 
  _account_holder property and the _balance property.
- Implement property decorators for account_holder (read-only),
  balance (read-only), and account_status (a computed property
  that returns "Active" if balance > 0 and "Inactive" 
  otherwise).
  
Then extend the BankAccount class to create a
SecureBankAccount class with password protection. 
- Define a constructor to call the base class's constructor
  and initialize the _password property.
- Implement a property decorator for password:
  -- Getter returns "********" instead of actual password
  -- Setter validates password length (min. 8 characters)
  -- Deleter handles password deletion
  
  
Sample:
ACT1 = BankAccount('John', 500)
print(ACT1.account_holder) → John
print(ACT1.balance) → 500
print(ACT1.account_status) → Active
ACT2 = BankAccount('Mary', 0)
print(ACT2.account_status) → Inactive
ACT3 = SecureBankAccount('Bill', 2000, 'security')
print(ACT3.account_holder) → Bill
print(ACT3.account_status) → Active
print(ACT3.password) → ********
ACT3.password = 'SECURITY'
print(ACT3.password) → ********
del ACT3.password
print(ACT3.password) → The attribute does not exist!   
    
'''

class BankAccount:
    def __init__(self, hold, bal):
        self._account_holder = hold
        self._balance = bal

    @property
    def account_holder(self):
        return self._account_holder
        
    @property
    def balance(self):
        return self._balance
    
    @property
    def account_status(self):
        if self._balance > 0:
            return "Active"
        return "Inactive"
    
class SecureBankAccount(BankAccount):
    def __init__(self, hold, bal, pw):
        super().__init__(hold, bal)
        self._password = pw
        
    @property
    def password(self):
        try:
            p = self._password
            return "********"
        except AttributeError:
            return "This attribute does not exist!"
    
    @password.setter
    def password(self, pw):
        if (len(pw) < 8):
            raise ValueError("Your password is not strong enough.")
        self._password = pw
    
    @password.deleter
    def password(self):
        del self._password

ACT3 = SecureBankAccount('Bill', 2000, 'security')
print(ACT3.password)
del ACT3.password
print(ACT3.password)


    
# %%
'''
5. Create an Employee class that satisfies the following
requirements:
- There are two class variables: `company_name` is "TechCorp",
  while `employees` is a list of employees.
- Implement a constructor to set up the name, position, and 
  salary of an employee and add the instance to the 
  `employees` list.
- Implement an instance method `get_annual_bonus` to 
  return 10% of the salary as bonus.
- Implement a class method `from_string` to create and return 
  a new Employee instance using a given employee_string in the 
  format "John Doe, Manager, 70000".
- Implement a class method `get_average_salary` to 
  compute and return the average salary of all employees in 
  the `employees` list.
- Implement a static method `is_valid_salary(salary)` that 
  returns True if salary is positive and False otherwise.
- Implement a static method `calculate_tax(salary, tax_rate)`
  that calculates and returns the tax amount. The default tax
  rate is 20%.  
  
Sample:
emp1 = Employee('Mike', 'Manager', 95000) 
emp2 = Employee('Betty', 'Staff', 65000)
emp3 = Employee('Mary', 'Manager', 80000)
print(emp1.get_annual_bonus()) → 9500.0
Employee.from_string('Cindy, Technician, 70000')
print(Employee.get_average_salary()) → 77500.0
print(emp1.is_valid_salary(-65000)) → False
print(emp3.calculate_tax(100000, 0.3)) → 30000.0
'''    

class Employee:
    company_name = 'TechCorp'
    employees = []
    tax_rate = 0.2
    
    def __init__(self, name, pos, sal):
        self.name = name
        self.pos = pos
        self.sal = sal
        self.employees.append(self)
        
    def get_annual_bonus(self):
        return 0.1 * self.sal
    
    @classmethod
    def from_string(cls, empstr):
        x = empstr.split(", ")
        return Employee(x[0], x[1], x[2])
    
    @classmethod
    def get_average_salary(employees):
        saltotal = 0
        for e in Employee.employees:
            saltotal += int(e.sal)
        return saltotal / len(Employee.employees)
    
    @staticmethod
    def is_valid_salary(salary):
        if salary < 0:
            return False
        return True
    
    @staticmethod
    def calculate_tax(salary, tax_rate):
        return salary * tax_rate
'''Implement a class called BankAccount that represents a bank account.
The class should have private attributes for account number, account holder,and account balance.
Include methods to deposit money,withdraw money,and display the account balance.
Ensure that the account balance cannot be accessed directly from outside the class.
Write a program to creative an Instance os the BankAccount class and test the deposit and withdrawal functionality.'''


class BankAccount:

  def__init__(self,account_number, account_holder_name,intial_balance=0.0) 
self. __account_number=account_number
self.__account_holder_name=account_holder_name
self. __account_balance=initial_balance

def__init__deposit(self, amount) 
if amount > 0:
  self. __account_balance +=amount
  print("Deposited ₹{}.New balance:₹{}".format(amount,self__account_balance))
else:
  print("Invalid deposit amount.")

def__init__withdraw (self,amount)
if amount > 0 and amount <= self. __account_balance :
  self.__account_balance -=amount
  print("withdraw ₹{}.New balance:₹{}.".format(amount,self__account_balance))
else:
  print ("Invalid withdrawal amount or Insufficient balance. ")

def__init__display_balance (self)
print(" Account balance for {} (Account #{}): ₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))

# Create an instances of the BankAccount class

account=BankAccount(account_number="123456789",account_holder_name="Priya",initial_balance=5000.0)

# Test deposit and withdrawal functionality
account. display_balance() 
account. deposit(500.0)
account. withdrawal(200.0)
account. display_balance() 
  

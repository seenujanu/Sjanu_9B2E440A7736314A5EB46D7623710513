"""Implement a class called BankAccount that represents a bank account. The class should have private 

attributes for account number, account holder name, and account balance. Include methods to 

deposit money, withdraw money, and display the account balance. Ensure that the account balance 

cannot be accessed directly from outside the class. Write a program to create an instance of the 

BankAccount class and test the deposit and withdrawal functionality."""

class BankAccount:
  def __init__ (self,account_number, account_holder_name, initial_balance ):
    self.__account_number =account_number 
    self.__account_holder_name =account_holder_name 
    self.__account_balance =initial_balance 

  def deposit(self, amount):
    if amount >0:
     self.__account_balance+=amount 
     print("deposited ₹{}. new balance:₹{}".format(amount, self.__account_balance))

    else:
      print("invalid deposited amount")

  def withdraw (self, amount):
    if amount >0 and amount <=                 self.__account_balance:
     self.__account_balance-=amount 
     print("withdraw ₹{}.new balance:₹{}".format(amount, self.__account_balance))

    else:
       print ("invalid withdrawal amount ")

  def display_balance (self):
   print ("Account balance for {}(Account#{}) : ₹{}".format(self.__account_holder_name, self.__account_number, 
self.__account_balance,))

account =BankAccount(account_holder_name="janu", account_number="123456789",initial_balance=20000.0)

account.display_balance ()
account.deposit (5000.0)
account.withdraw (2000.0)
account.display_balance ()
  
  

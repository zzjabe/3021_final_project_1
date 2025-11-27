"""
Description: A client program written to verify implementation 
of the Observer Pattern.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Jianbin Zhang"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date, datetime
from client.client import Client

# 2. Create a Client object with data of your choice.
try:
    client_1 = Client(1234, "Jack", "Ma", "jackma@rrc.ca")
except Exception as e:
    print(e)

# 3a. Create a ChequingAccount object with data of your choice, using the client_number 
# of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in step 2.
try:
    chequing_account_1 = ChequingAccount(11001, 1234, 1000, date(2025, 1, 18), 2000, 0.03)
except Exception as e:
    print(e)
try:
    savings_account_1 = SavingsAccount(11002, 1234, 1000, date(2025, 1, 18), 499.99)
except Exception as e:
    print(e)

# 4 The ChequingAccount and SavingsAccount objects are 'Subject' objects.
# The Client object is an 'Observer' object.  
# 4a.  Attach the Client object (created in step 2) to the ChequingAccount object (created in step 3).
# 4a.  Attach the Client object (created in step 2) to the SavingsAccount object (created in step 3).
try:    
    chequing_account_1.attach(client_1)
except Exception as e:
    print(e)
try:    
    savings_account_1.attach(client_1)
except Exception as e:
    print(e)

# 5a. Create a second Client object with data of your choice.
# 5b. Create a SavingsAccount object with data of your choice, using the client_number 
# of the client created in this step.
try:
    client_2 = Client(1235, "Daisy", "Zhang", "daisyzhang@rrc.ca")
except Exception as e:
    print(e)
try:
    savings_account_2 = SavingsAccount(11003, 1235, 1000, date(2025, 1, 18), 499.99)
except Exception as e:
    print(e)

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions (deposits and withdraws) 
# which would cause the Subject (BankAccount) to notify the Observer 
# (Client) as well as transactions that would not 
# cause the Subject to notify the Observer.  Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
try:
    chequing_account_1.deposit(10000)
except Exception as e:
    print(e)

try:
    chequing_account_1.withdraw(10999)
except Exception as e:
    print(e)

try:
    chequing_account_1.deposit(50)
except Exception as e:
    print(e)

try:
    savings_account_1.deposit(10000)
except Exception as e:
    print(e)

try:
    savings_account_1.withdraw(10999)
except Exception as e:
    print(e)

try:
    savings_account_1.deposit(50)
except Exception as e:
    print(e)

try:
    savings_account_2.deposit(10000)
except Exception as e:
    print(e)

try:
    savings_account_2.withdraw(10999)
except Exception as e:
    print(e)

try:
    savings_account_2.deposit(50)
except Exception as e:
    print(e)
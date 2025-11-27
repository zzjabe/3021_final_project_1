"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Jianbin Zhang"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your
# choice including a balance which is below the overdraft limit. 
chequing_account = None
try:
    chequing_account = ChequingAccount(11001, 123456, 1000, date(2025, 1, 18), 2000, 0.03)
except ValueError as e:
    print(e)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
if chequing_account:
    print(chequing_account)
    print(f"Service charges: ${chequing_account.get_service_charges():,.2f}\n")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
    try:
        chequing_account.deposit(2000)
        print(chequing_account)
        print(f"Service charges: ${chequing_account.get_service_charges():,.2f}")
    except ValueError as e:
        print(e)

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = None
try:
    savings_account = SavingsAccount(11001, 123456, 1000, date(2025, 1, 18), 499.99)
except ValueError as e:
    print(e)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
if savings_account:
    print(savings_account)
    print(f"Service charges: ${savings_account.get_service_charges():,.2f}\n")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
    try:
        savings_account.withdraw(600)
        print(savings_account)
        print(f"Service charges: ${savings_account.get_service_charges():,.2f}")
    except ValueError as e:
        print(e)

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_account_1 = None
try:
    investment_account_1 = InvestmentAccount(11001, 123456, 1000, date(2025, 1, 18), 1.50)
except ValueError as e:
    print(e)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
if investment_account_1:
    print(investment_account_1)
    print(f"Service charges: ${investment_account_1.get_service_charges():,.2f}\n")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_account_2 = None
try:
    investment_account_2 = InvestmentAccount(11001, 123456, 1000, date(2015, 1, 18), 1.50)
except ValueError as e:
    print(e)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
if investment_account_2:
    print(investment_account_2)
    print(f"Service charges: ${investment_account_2.get_service_charges():,.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
if chequing_account:
    chequing_account.withdraw(chequing_account.get_service_charges())
if savings_account:
    savings_account.withdraw(savings_account.get_service_charges())
if investment_account_1:
    investment_account_1.withdraw(investment_account_1.get_service_charges())
if investment_account_2:
    investment_account_2.withdraw(investment_account_2.get_service_charges())


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
if chequing_account:
    print(f"{chequing_account}\n")
if savings_account:
    print(f"{savings_account}\n")
if investment_account_1:
    print(f"{investment_account_1}\n")
if investment_account_2:
    print(f"{investment_account_2}")


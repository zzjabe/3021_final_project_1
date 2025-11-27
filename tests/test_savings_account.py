__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from bank_account.savings_account import SavingsAccount
from bank_account.bank_account import BankAccount
from datetime import date, timedelta
import unittest

class TestSavingsAccount(unittest.TestCase):

    def setUp(self):
        self.savings_account = SavingsAccount(11001, 123456, 1000, 
                                                date(2025, 1, 18), 499.99)
        
    def test_init_valid_arguments_attributes_set(self):

        self.assertEqual(11001, self.savings_account._BankAccount__account_number)
        self.assertEqual(123456, self.savings_account._BankAccount__client_number)
        self.assertEqual(1000, self.savings_account._BankAccount__balance)

        self.assertEqual(date(2025, 1, 18), self.savings_account._date_created)

        self.assertEqual(499.99, self.savings_account._SavingsAccount__minimum_balance)

    def test_invalid_minimum_balance_set_default_amount(self):
        savings_account = SavingsAccount(11001, 123456, 1000, 
                                                date(2025, 1, 18), "Invalid")
        self.assertEqual(50, savings_account._SavingsAccount__minimum_balance)
    
    def test_balance_greater_than_minimum_balance_return_base_service_charge(self):
        self.assertEqual(0.50, self.savings_account.get_service_charges())
        
    def test_balance_equal_to_minimum_balance_return_calculated_service_charge(self):
        savings_account = SavingsAccount(11001, 123456, 1000, date(2025, 1, 18), 1000.00)
        self.assertEqual(0.50, savings_account.get_service_charges())

    def test_balance_less_than_minimum_balance_return_calculated_charge(self):
        savings_account = SavingsAccount(11001, 123456, 1000, date(2025, 1, 18), 2000.00)
        self.assertEqual(1.00, savings_account.get_service_charges())

    def test_str_date_created_more_than_ten_years_ago_return_formtted_string(self):
        expected = ("Account Number: 11001 Balance: $1,000.00\n"
                    +"Minimum Balance: $499.99 Account Type: Savings")
        self.assertEqual(expected, str(self.savings_account))

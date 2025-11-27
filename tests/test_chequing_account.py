__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from bank_account.chequing_account import ChequingAccount
from bank_account.bank_account import BankAccount
from datetime import date
import unittest

class TestChequingAccount(unittest.TestCase):

    def setUp(self):
        self.chequing_account = ChequingAccount(11001, 123456, 1000, 
                                                date(2025, 1, 18), 500, 0.03)
        
    def test_init_valid_arguments_attributes_set(self):

        self.assertEqual(11001, self.chequing_account._BankAccount__account_number)
        self.assertEqual(123456, self.chequing_account._BankAccount__client_number)
        self.assertEqual(1000, self.chequing_account._BankAccount__balance)

        self.assertEqual(date(2025, 1, 18), self.chequing_account._date_created)

        self.assertEqual(500, self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(0.03, self.chequing_account._ChequingAccount__overdraft_rate)

    def test_invalid_overdraft_limit_set_default_amount(self):
        chequing_account = ChequingAccount(11001, 123456, 1000, 
                                                date(2025, 1, 18), "Invalid", 0.03)
        self.assertEqual(-100, chequing_account._ChequingAccount__overdraft_limit)
    
    def test_invalid_overdraft_rate_set_default_rate(self):
        chequing_account = ChequingAccount(11001, 123456, 1000, 
                                                date(2025, 1, 18), 500, "Invalid")

        self.assertEqual(0.05, chequing_account._ChequingAccount__overdraft_rate)

    def test_invalid_date_created_set_default_date(self):
        chequing_account = ChequingAccount(11001, 123456, 1000, 
                                                "Invalid", 500, 0.03)
        self.assertEqual(date.today(), chequing_account._date_created)

    def test_balance_greater_than_overdraft_limit_return_base_service_charge(self):
        self.assertEqual(0.50, self.chequing_account.get_service_charges())


    def test_balance_less_than_overdraft_limit_return_calculated_charge(self):
        chequing_account = ChequingAccount(11001, 123456, 100, 
                                                date(2025, 1, 18), 500, 0.03)
        self.assertEqual(12.50, chequing_account.get_service_charges())

    def test_balance_equal_to_overdraft_limit_return_base_service_charge(self):
        chequing_account = ChequingAccount(11001, 123456, 500, 
                                                date(2025, 1, 18), 500, 0.03)
        self.assertEqual(0.50, chequing_account.get_service_charges())

    def test_str_valid_value_return_formtted_string(self):
        expected = ("Account Number: 11001 Balance: $1,000.00\n"
                    + "Overdraft Limit: $500.00 Overdraft "
                    + "Rate: 3.00% Account Type: Chequing")
        self.assertEqual(expected, str(self.chequing_account))
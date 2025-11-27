__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount
from datetime import date, timedelta
import unittest

class TestInvestmentAccount(unittest.TestCase):

    def setUp(self):
        self.investment_account = InvestmentAccount(11001, 123456, 1000, 
                                                date(2025, 1, 18), 1.50)
        
    def test_init_valid_arguments_attributes_set(self):

        self.assertEqual(11001, self.investment_account._BankAccount__account_number)
        self.assertEqual(123456, self.investment_account._BankAccount__client_number)
        self.assertEqual(1000, self.investment_account._BankAccount__balance)

        self.assertEqual(date(2025, 1, 18), self.investment_account._date_created)

        self.assertEqual(1.50, self.investment_account._InvestmentAccount__management_fee)

    def test_invalid_management_fee_set_default_amount(self):
        investment_account = InvestmentAccount(11001, 123456, 1000, 
                                                date(2025, 1, 18), "Invalid")
        self.assertEqual(2.55, investment_account._InvestmentAccount__management_fee)
    
    def test_date_created_more_than_ten_years_ago_return_base_service_charge(self):
        investment_account = InvestmentAccount(11001, 123456, 1000, date(2015, 1, 18), 1.50)
        self.assertEqual(0.50, investment_account.get_service_charges())
        
    def test_date_created_exactly_ten_years_ago_return_calculated_service_charge(self):
        # investment_account = InvestmentAccount(11001, 123456, 1000, date.today() - timedelta(days = 10 * 365.25), 1.50)
        investment_account = InvestmentAccount(11001, 123456, 1000, InvestmentAccount.TEN_YEARS_AGO, 1.50)
        self.assertEqual(2.00, investment_account.get_service_charges())

    def test_date_created_within_last_ten_years_return_calculated_charge(self):
        self.assertEqual(2.00, self.investment_account.get_service_charges())

    def test_str_date_created_more_than_ten_years_ago_return_formtted_string(self):
        investment_account = InvestmentAccount(11001, 123456, 1000, date(2015, 1, 18), 1.50)
        expected = ("Account Number: 11001 Balance: $1,000.00\n"
                    +"Date Created: 2015-01-18 Management Fee: Waived "
                    +"Account Type: Investment")
        self.assertEqual(expected, str(investment_account))

    def test_str_date_created_within_last_ten_years_return_formtted_string(self):
        expected = ("Account Number: 11001 Balance: $1,000.00\n"
                    +"Date Created: 2025-01-18 Management Fee: $1.50 "
                    +"Account Type: Investment")
        self.assertEqual(expected, str(self.investment_account))
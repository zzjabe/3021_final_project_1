"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.bank_account = BankAccount(1010, 2222, 1234.56)
    
    def test_init_valid_arguments_attributes_set(self):
        # Arrange Act & Assert
        self.assertEqual(1010, self.bank_account._BankAccount__account_number)
        self.assertEqual(2222, self.bank_account._BankAccount__client_number)
        self.assertEqual(1234.56, self.bank_account._BankAccount__balance)

    def test_init_invalid_balance_set_balance_to_zero(self):
        # Arrange
        bank_account = BankAccount(1010, 2222, "Invalid")

        # Act & Assert
        self.assertEqual(1010, bank_account._BankAccount__account_number)
        self.assertEqual(2222, bank_account._BankAccount__client_number)
        self.assertEqual(0, bank_account._BankAccount__balance)

    def test_init_invalid_account_number_raises_valueerror(self):
        # Arrange Act & Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount("Invalid", 2222, 1234.56)

    def test_init_invalid_client_number_raises_valueerror(self):
        # Arrange Act & Assert
        with self.assertRaises(ValueError):
            bank_account = BankAccount(1010, "Invalid", 1234.56)
    
    def test_account_number_accessor_valid_account_number_returned(self):
        # Arrange Act & Assert
        self.assertEqual(1010, self.bank_account.account_number)

    def test_client_number_accessor_valid_client_number_returned(self):
        # Arrange Act & Assert
        self.assertEqual(2222, self.bank_account.client_number)
        
    def test_balance_accessor_valid_balance_returned(self):
        # Arrange Act & Assert
        self.assertEqual(1234.56, self.bank_account.balance)

    def test_positive_amount_return_correct_update_balance(self):
        # Arrange
        amount = 500.00

        # Act
        self.bank_account.update_balance(amount)

        # Assert
        self.assertEqual(1734.56, self.bank_account.balance)

    def test_negative_amount_return_correct_update_balance(self):
        # Arrange
        amount = -500.00

        # Act
        self.bank_account.update_balance(amount)

        # Assert
        self.assertEqual(734.56, self.bank_account.balance)

    def test_invalid_amount_return_unchanged_balance(self):
        # Arrange
        amount = "Invalid"

        # Act
        self.bank_account.update_balance(amount)

        # Assert
        self.assertEqual(1234.56, self.bank_account.balance)

    def test_positive_deposit_amount_return_correct_balance(self):
        # Arrange
        amount = 500.00

        # Act
        self.bank_account.deposit(amount)

        # Assert
        self.assertEqual(1734.56, self.bank_account.balance)
    
    def test_negative_deposit_amount_raises_valueerror(self):
        # Arrange Act & Assert
        with self.assertRaises(ValueError):
            self.bank_account.deposit(-500.00)

    def test_positive_withdraw_amount_return_correct_balance(self):
        # Arrange
        amount = 500.00

        # Act
        self.bank_account.withdraw(amount)

        # Assert
        self.assertEqual(734.56, self.bank_account.balance)

    def test_negative_withdraw_amount_raises_valueerror(self):
        # Arrange Act & Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(-500.00)

    def test_exceed_balance_withdraw_amount_raises_valueerror(self):
        # Arrange Act & Assert
        with self.assertRaises(ValueError):
            self.bank_account.withdraw(5000.00)

    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = ("Account Number: 1010 Balance: $1,234.56\n")

        # Act & Assert
        self.assertEqual(expected, str(self.bank_account))
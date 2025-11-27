"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""

import unittest
from client.client import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client(1010, "Jack", "Ma", "jackma@rrc.ca")

    def test_init_valid_arguments_attributes_set(self):
        # Arrange Act & Assert
        self.assertEqual(1010, self.client._Client__client_number)
        self.assertEqual("Jack", self.client._Client__first_name)
        self.assertEqual("Ma", self.client._Client__last_name)
        self.assertEqual("jackma@rrc.ca", self.client._Client__email_address)

    def test_init_invalid_client_number_raises_valueerror(self):
        # Arrange Act & Assert
        with self.assertRaises(ValueError):
            client = Client("Invalid", "Jack", "Ma", "jackma@rrc.ca")

    def test_init_blank_first_name_raises_valueerror(self):
        # Arrange Act & Assert
        with self.assertRaises(ValueError):
            client = Client(1010, "", "Ma", "jackma@rrc.ca")
    
    def test_init_blank_last_name_raises_valueerror(self):
        # Arrange Act & Assert
        with self.assertRaises(ValueError):
            client = Client(1010, "Jack", "", "jackma@rrc.ca")
    
    def test_init_invalid_email_address_return_default_email(self):
        # Arrange 
        client = Client(1010, "Jack", "Ma", "Invalid")

        # Act & Assert
        self.assertEqual("email@pixell-river.com", client._Client__email_address)

    def test_client_number_accessor_valid_client_number_returned(self):
        # Arrange Act & Assert
        self.assertEqual(1010, self.client.client_number)

    def test_first_name_accessor_valid_first_name_returned(self):
        # Arrange Act & Assert
        self.assertEqual("Jack", self.client.first_name)

    def test_last_name_accessor_valid_last_name_returned(self):
        # Arrange Act & Assert
        self.assertEqual("Ma", self.client.last_name)

    def test_email_address_accessor_valid_email_address_returned(self):
        # Arrange Act & Assert
        self.assertEqual("jackma@rrc.ca", self.client.email_address)

    def test_str_valid_inputs_returns_formatted_string(self):
        # Arrange
        expected = ("Ma, Jack [1010] - jackma@rrc.ca\n")

        # Act & Assert
        self.assertEqual(expected, str(self.client))

    
__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    SavingsAccount class: Maintains savings account data.
    """

    def __init__(self, account_number: int, 
                 client_number: int, 
                 balance: float, 
                 date_created: date, 
                 minimum_balance: float):
        """
        Initializes the class attributes with the argument values.
        Args:
            account_number (int): The account number of the bank account.
            client_number (int): The client_number 0f the bank account.
            balance (float): The balance of the bank account.
            date_created (date): The date of the bank account.
            minimum (float): The minimum value a balance can be before further
            service charges are applied.

        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__minimum_balance = float(minimum_balance)
        except:
            self.__minimum_balance = 50

        self.__strategy = MinimumBalanceStrategy(
            minimum_balance = self.__minimum_balance
        )
    
    def __str__(self) -> str:
        """
        Returns a string representation of a SavingsAccount object.

        Returns:
            str: Savings account formatted as a string.
        
        """
        return_value = super().__str__()
        return_value += (f"Minimum Balance: ${self.__minimum_balance:,.2f} "
                            + f"Account Type: Savings")
        return return_value
    
    def get_service_charges(self) -> float:
        """
        Returns the service charges of the savings account.

        Returns:
            float: The service charges of the savings account.

        """
        return self.__strategy.calculate_service_charges(self)

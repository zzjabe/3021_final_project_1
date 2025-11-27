__author__ = "Jianbin Zhang"
__version__ = "1.1.0"

from bank_account.bank_account import BankAccount
from datetime import date
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    ChequingAccount class: Maintains chequing account data.
    """

    def __init__(self, account_number: int, 
                 client_number: int, 
                 balance: float, 
                 date_created: date, 
                 overdraft_limit: float, 
                 overdraft_rate: float
                 ):
        """
        Initializes the class attributes with the argument values.
        Args:
            account_number (int): The account number of the bank account.
            client_number (int): The client_number 0f the bank account.
            balance (float): The balance of the bank account.
            date_created (date): The date of the bank account.
            overdraft_limit (float): The maximum amount a balance can be 
            overdrawn(below 0.00) before overdraft fees are applied.
            overdraft_rate: The rate to which overdraft fess will be applied.

        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__overdraft_limit = float(overdraft_limit)      
        except:
            self.__overdraft_limit = -100
        
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except:
            self.__overdraft_rate = 0.05

        self.__strategy = OverdraftStrategy(
            overdraft_limit = self.__overdraft_limit,
            overdraft_rate = self.__overdraft_rate
        )
        
    def __str__(self) -> str:
        """
        Returns a string representation of a ChequingAccount object.

        Returns:
            str: Chequing account formatted as a string.
        
        """
        return_value = super().__str__()
        return_value += (f"Overdraft Limit: ${self.__overdraft_limit:,.2f} "
                        + f"Overdraft Rate: {self.__overdraft_rate:.2%} "
                        + "Account Type: Chequing")
        return return_value

    def get_service_charges(self) -> float:
        """
        Returns the service charges of the chequing account.

        Returns:
            float: The service charges of the chequing account.
        
        """
        return self.__strategy.calculate_service_charges(self)
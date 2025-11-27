__author__ = "Jianbin Zhang"
__version__ = "1.1.0"

from bank_account.bank_account import BankAccount
from datetime import date, timedelta
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Maintains investment account data.
    """

    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, account_number: int, 
                 client_number: int, 
                 balance: float, 
                 date_created: date, 
                 management_fee: float):
        """
        Initializes the class attributes with the argument values.
        Args:
            account_number (int): The account number of the bank account.
            client_number (int): The client_number 0f the bank account.
            balance (float): The balance of the bank account.
            date_created (date): The date of the bank account.
            management_fee (float): A float which stores a flat-rate fee the 
            bank charge for managing an InvestmentAccount.

        """

        super().__init__(account_number, client_number, balance, date_created)

        try:
            self.__management_fee = float(management_fee)
        except:
            self.__management_fee = 2.55

        self.__strategy = ManagementFeeStrategy(
            date_created = self._date_created,
            management_fee = self.__management_fee
        )
    
    def __str__(self) -> str:
        """
        Returns a string representation of a InvestmentAccount object.

        Returns:
            str: Investment account formatted as a string.
        
        """
        return_value = super().__str__()

        if self._date_created < self.TEN_YEARS_AGO:
            return_value += (f"Date Created: {self._date_created} "
                            + f"Management Fee: Waived "
                            + f"Account Type: Investment")
        else:            
            return_value += (f"Date Created: {self._date_created} "
                            + f"Management Fee: ${self.__management_fee:.2f} "
                            + f"Account Type: Investment")
        return return_value
    
    def get_service_charges(self) -> float:
        """
        Returns the service charges of the investment account.

        Returns:
            float: The service charges of the investment account.

        """
        return self.__strategy.calculate_service_charges(self)

    

    
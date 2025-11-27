__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Minimum balance strategy: This strategy applies a service 
    charge fee to the bank account.

    """

    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initializes the class attributes with the argument values.

        Args:
            minimum balance (float): The minimum balance of the bank account.

        """
        if isinstance(minimum_balance, (int, float)):
            self.__minimum_balance = minimum_balance
        else:
            raise ValueError("Minimum balance must be numeric.")
    
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charge based on management fee strategy.
    
        Args:
            account (BankAccount): The bank account instance.
        Returns:
            float: The calculated service charge.
        """
        if account.balance >= self.__minimum_balance:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM
        return service_charge
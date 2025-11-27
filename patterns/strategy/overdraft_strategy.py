__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Overdraft strategy: This strategy applies a service 
    charge fee to the bank account.

    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the class attributes with the argument values.

        Args:
            overdraft_limit (float): The overdraft limit of the bank account.
            overdraft_rate (float): The overdraft rate of the bank account.

        """
        # if isinstance(overdraft_limit, (int, float)):
        #     self.__overdraft_limit = overdraft_limit
        # else:
        #     raise ValueError("Overdraft_limit must be numeric.")
        
        # if isinstance(overdraft_rate, (int, float)):
        #     self.__overdraft_rate = overdraft_rate
        # else:
        #     raise ValueError("Overdraft_rate must be numeric.")
        
        try:
            self.__overdraft_limit = float(overdraft_limit)
            self.__overdraft_rate = float(overdraft_rate)
        except ValueError:
            raise ValueError("Invalid overdraft limit or overdraft rate.")
        
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charge based on overdraft strategy.
    
        Args:
            account (BankAccount): The bank account instance.
        Returns:
            float: The calculated service charge.
        """
        if account.balance >= self.__overdraft_limit:
            service_charges = self.BASE_SERVICE_CHARGE
        else:
            service_charges = (self.BASE_SERVICE_CHARGE + (self.__overdraft_limit
                                         - account.balance) * self.__overdraft_rate)
        return(service_charges)

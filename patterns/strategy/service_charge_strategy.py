__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """
    Interface to be applied to the service charge strategy class.
    In python defined as an abstract class.

    """
    
    BASE_SERVICE_CHARGE : float = 0.5

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Abstract process service charges method to be implemented in subclasses.

        Args:
            account (BankAccount): The bank account for which the service charge
            needs to be calculated.
        
        Returns:
            float: The calculated service charge amount.
        """
        pass
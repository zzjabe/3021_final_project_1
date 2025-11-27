__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Management fee strategy: This strategy applies a service 
    charge fee to the bank account.

    """

    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the class attributes with the argument values.

        Args:
            date_created (date): The date created of the bank account.
            management_fee (float): The management fee of the bank account.
        
        """
        if isinstance(date_created, date):
            self.__date_created = date_created
        else:
            raise ValueError("Invalid date.")
        
        if isinstance(management_fee, (int, float)):
            self.__management_fee = management_fee
        else:
            raise ValueError("Management fee must be numeric.")
    
    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculate the service charge based on management fee strategy.
    
        Args:
            account (BankAccount): The bank account instance.

        Returns:
            float: The calculated service charge.
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            service_charge = self.BASE_SERVICE_CHARGE
        else:
            service_charge = self.BASE_SERVICE_CHARGE + self.__management_fee
        return service_charge
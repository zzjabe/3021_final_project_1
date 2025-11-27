"""
Description: A class to manage bank account objects.
"""

__author__ = "Jianbin Zhang"
__Version__ = "1.2.0"

from datetime import date
from abc import ABC, abstractmethod
from patterns.observer.observer import Observer
from patterns.observer.subject import Subject

class BankAccount(Subject, ABC):
    """
    BankAccount class: Maintains bank account data.
    """

    LARGE_TRANSACTION_THRESHOLD: float = 9999.99
    LOW_BALANCE_LEVEL: float = 50.0

    def __init__(self, account_number: int, 
                 client_number: int, 
                 balance: float, 
                 date_created: date):
        """
        Initializes the class attributes with argument values.

        Args:
            account_number (int): The account number of the bank account.
            client_number (int): The client_number 0f the bank account.
            balance (float): The balance of the bank account.
            date_created (date): The date of the bank account.

        Raises:
            ValueError: When the account number is nonnumeric, the client number is
            nonnumberic.
        """
        super().__init__()
        if isinstance(account_number, int):
            self.__account_number = account_number
        else:
            raise ValueError("Account number must be numeric.")
        
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client number must be numeric.")
        
        try:
            self.__balance = float(balance)
        except:
            self.__balance = 0

        if isinstance(date_created, date):
            self._date_created = date_created
        else:
            self._date_created = date.today()
        
    @property
    def account_number(self) -> int:
        """
        Accessor for account number attribute.

        Returns:
            int: Account number of the bank account.

        """
        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """
        Accessor for client number attribute.

        Returns:
            int: Client number of the bank account.

        """
        return self.__client_number
    
    @property
    def balance(self) -> float:
        """
        Accessor for balance attribute.

        Returns:
            float: Balance of the bank account.
        
        """
        return self.__balance
    
    def update_balance(self, amount: float):
        """
        Update the balance by adding the given amount.

        Args:
            amount (float): The amount changed in the balance.
        
        Raises:
            ValueError: When results in a negative balance.

        """
        try:
            amount = float(amount)
            if self.__balance + amount >= 0:
                self.__balance += amount
        except:
            pass

        if self.__balance < self.LOW_BALANCE_LEVEL:
            message = (f"Low balance warning ${self.__balance:,.2f}: "
                    + f"on account {self.__account_number}.")
            self.notify(message)

        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            message = (f"Large transaction ${amount:,.2f}: "
                    + f"on account {self.__account_number}.")
            self.notify(message)

    def deposit(self, amount: float):
        """
        Deposit a positive amount into the bank account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: When the amount is nonnumeric or is negative.

        """
        try:
            amount = float(amount)           
        except ValueError:
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        if amount <= 0:
                raise ValueError(f"Deposit amount: ${amount:,.2f} must be positive.")
        self.update_balance(amount)

    def withdraw(self, amount: float):
        """
        Withdraw a positive amount from the bank account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
        ValueError: When the amount is nonnumeric, the amount is negative, 
                    or the amount exceed the account balance.
        
        """
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        if amount < 0:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must be positive.")
        
        if self.__balance < amount:
            raise ValueError(f"Withdrawal amount: ${amount:,.2f} must not exceed "
                             + f"the account balance: ${self.__balance:,.2f}")
        self.update_balance(-amount)
        
    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The bank account instance formatted as a string.
        
        """
        return (f"Account Number: {self.account_number} "
                + f"Balance: ${self.balance:,.2f}\n")
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Calculates the service charges in the bank account instance. 
        Implemented in subclass.

        """
        pass

    def attach(self, observer: Observer) -> None:
        """
        Adds an observer to the list of observers if it 
        is not already present.

        Args:
            observer (Observer): The observer instance that will be 
            added to the notification list.

        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the list of observers if it exists.

        Args:
            observer (Observer): The observer instance to be 
            removed from the notification list.

        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message:str) -> None:
        """
        Sends a notification message to all registered observers.

        Args:
            message (str): The message to be sent to all observers.

        """
        for observer in self._observers:
            observer.update(message)

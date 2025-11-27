__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Interface to be applied to the observer class.
    In python defined as an abstract class.

    """

    @abstractmethod
    def update(self, message:str):
        """
        Abstract process payment method to be implemented in subclasses.

        Args:
            message (str): The notification message containing 
            details about the update.
        """
        pass
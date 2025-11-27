__author__ = "Jianbin Zhang"
__version__ = "1.0.0"

from patterns.observer.observer import Observer
from abc import ABC, abstractmethod
from typing import List

class Subject(ABC):
    """
    An abstract base class for implementing the Subject in the Observer pattern.
    """
    def __init__(self):
        """
        Initializes the Subject with an empty list of observers.

        """

        self._observers: List[Observer] = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attaches an observer to the subject.

        Args:
            observer (Observer): The observer instance to be 
            added to the notification list.
            
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detaches an observer from the subject.

        Args:
            observer (Observer): The observer instance to be 
            removed from the notification list.

        """
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """
        Notifies all registered observers with a message.

        Args:
            message (str): The notification message to be 
            sent to all observers.
            
        """
        pass

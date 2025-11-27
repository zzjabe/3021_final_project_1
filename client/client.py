"""
Description: A class to manage client objects.
"""

__author__ = "Jianbin Zhang"
__Version__ = "1.1.0"

from email_validator import validate_email, EmailNotValidError
from patterns.observer.observer import Observer
from utility.file_utils import simulate_send_email
from datetime import date, timedelta, datetime

class Client(Observer):
    """
    Client class: Maintains client data.
    """
    def __init__(self, client_number: int, first_name: str, 
                 last_name: str, email_address: str):
        """
        Initializes the class attributes with argument values.

        Args:
            client_number: A number to uniquely identify the client.
            first_name: The first name of the client.
            last_name: The last name of the client
            email_address: The email address of the client
        
        Raises:
            ValueError: When the client number is nonnumeric, the first name 
            is blank, the last name is blank, the email address is not valid.

        """
        if isinstance(client_number, int):
            self.__client_number = client_number
        else:
            raise ValueError("Client Number must be numeric.")
        
        if len(first_name.strip()) > 0:
            self.__first_name = first_name
        else:
            raise ValueError("First name cannot be blank.")
        
        if len(last_name.strip()) > 0:
            self.__last_name = last_name
        else:
            raise ValueError("Last name cannot be blank.")
        
        try:
            validated_email = validate_email(email_address, 
                                             check_deliverability = False)
            self.__email_address = email_address
        except EmailNotValidError as e:           
            self.__email_address = "email@pixell-river.com"

    @property
    def client_number(self) -> int:
        """
        Accessor for the client number attribute.

        Returns:
            int: Client Number of the client.

        """
        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """
        Accessor for the first name attribute.

        Returns:
            str: First name of the client.

        """
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """
        Accessor for the last name attribute.

        Returns:
            str: Last name of the client.

        """
        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """
        Accessor for the email address attribute.

        Returns:
            str: Email address of the client.

        """
        return self.__email_address
    
    def __str__(self) -> str:
        """
        Returns a string representation of the class instance.

        Returns:
            str: The client instance formatted as a string.

        """
        return (f"{self.__last_name}, {self.__first_name} "
                + f"[{self.__client_number}] - {self.__email_address}\n")
    
    def update(self, message: str):
        """
        Implements the update method from the Observer class.
        Simulates sending an email to the client with the given message.

        Args:
            message (str): The message to include in the email notification.

        """

        current_time = datetime.now()

        subject = (f"ALERT: Unusual Activity: {current_time}")

        body = (f"Notification for {self.__client_number}: "
                + f"{self.__first_name} {self.__last_name}: {message}")
        
        simulate_send_email(self.__email_address, subject, body)

    

        

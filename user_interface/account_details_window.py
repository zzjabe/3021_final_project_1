__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Jianbin Zhang"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    balance_updated = Signal(object)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):        
            self.__account = copy.deepcopy(account)

            self.account_number_label.setText(f"{self.__account.account_number}")
            self.balance_label.setText(f"${self.__account.balance:,.2f}")

            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        
        else:
            self.reject()
            return
        


    @Slot()
    def __on_apply_transaction(self):
        """
        Handle deposit or withdraw transactions when the deposit 
        or withdraw button is clicked.
        """
        amount_text = self.transaction_amount_edit.text().strip()

        # if not amount_text:
        #     QMessageBox.information(self, "Invalid Input", "Please enter "
        #                             + "an amount.",  QMessageBox.Ok)
        #     self.transaction_amount_edit.setFocus()
        #     return
        
        try:
            amount = eval(amount_text)
        except:
            QMessageBox.information(self, "Invalid Data", "Amount must "
                                    + "be numeric.",  QMessageBox.Ok)
            self.transaction_amount_edit.setFocus()
            return
        
        sender = self.sender()
        transaction = "Deposit" if sender == self.deposit_button else "Withdraw"

        try:
            if transaction == "Deposit":
                self.__account.deposit(amount)
            
            else:
                self.__account.withdraw(amount)

            self.balance_label.setText(f"${self.__account.balance:,.2f}")

            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        except Exception as e:

            QMessageBox.information(self, f"{transaction} Failed", f"{e}", 
                                    QMessageBox.Ok)
            
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        self.balance_updated.emit(self.__account)

    @Slot()
    def __on_exit(self):
        """
        Handle the exit button click event to close the dialog window.
        """
        self.close()


    





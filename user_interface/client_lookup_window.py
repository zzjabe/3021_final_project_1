__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Jianbin Zhang"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account import *

class ClientLookupWindow(LookupWindow):
    """
    A class for looking up client information and their associated accounts.
    """
    def __init__(self):
        """
        Initialize the ClientLookupWindow.
        """
        super().__init__()

        self.__client_listing, self.__accounts = load_data()

        self.lookup_button.clicked.connect(self.__on_lookup_client)

        self.client_number_edit.textChanged.connect(self.__on_text_changed)

        self.account_table.cellClicked.connect(self.__on_select_account)

    @Slot()
    def __on_lookup_client(self):
        """
        Handle the client lookup action when the lookup button is clicked.
        """
        try:
            client_number = int(self.client_number_edit.text())
        except:
            QMessageBox.information(self, "Input Error", "The client number "
                                    + "must be a numeric value.",  QMessageBox.Ok)
            self.client_number_edit.setFocus()
            self.reset_display()
            return
        
        if client_number not in self.__client_listing:
            QMessageBox.information(self, "Not Found", f"Client number: "
                                    + f"{client_number} not found.", QMessageBox.Ok)
            self.client_number_edit.setFocus()
            self.reset_display()
            return

        client = self.__client_listing[client_number]
        first_name = client.first_name
        last_name = client.last_name
        full_name = f"{first_name} {last_name}"
        
        self.client_info_label.setText(f"Client Name: {full_name}")

        self.account_table.setRowCount(0)

        row = 0

        for account in self.__accounts.values():
            if account.client_number == client_number:

                self.account_table.setRowCount(row + 1)

                account_number_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created_item = QTableWidgetItem(str(account._date_created))
                account_type_item = QTableWidgetItem(account.__class__.__name__)

                account_number_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                date_created_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                account_type_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    
                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_created_item)
                self.account_table.setItem(row, 3, account_type_item)

                row += 1
        
        self.account_table.resizeColumnsToContents()

    @Slot()
    def __on_text_changed(self):
        """
        Handle changes in the client number input field.
        """
        self.client_info_label.setText("")
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) ->None:
        """
        Handle the selection of an account from the account table.

        Args:
            row (int): The row number of the clicked cell.
            column (int): The column number of the clicked cell.
        """
        account_number_item = self.account_table.item(row, 0)

        if account_number_item is None:
            QMessageBox.information(self, "Invalid Selection", "Please select a "
                                    + "valid record.", QMessageBox.Ok)
            return

        account_number = int(account_number_item.text())
           
        if account_number not in self.__accounts:
            QMessageBox.information(self, "No Bank Account", "Bank Account selected "
                                    + "does not exist.", QMessageBox.Ok)
            return
        
        bank_account = self.__accounts[account_number]

        details_window = AccountDetailsWindow(bank_account)

        details_window.balance_updated.connect(self.__update_data)

        details_window.exec_()

    @Slot(object)
    def __update_data(self, account: BankAccount):
        """
        Handle the balance_updated signal from AccountDetailsWindow 
        to update the UI and data.
        """
        for row in range(self.account_table.rowCount()):
            table_account_number_item = self.account_table.item(row, 0)

            table_account_number = int(table_account_number_item.text())

            if table_account_number == account.account_number:
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.account_table.setItem(row, 1, balance_item)

        self.__accounts[account.account_number] = account

        update_data(account)










        

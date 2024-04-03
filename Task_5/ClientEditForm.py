from PyQt6.QtWidgets import QLineEdit
from EditForm import editForm
from ClientTable import ClientTable


class clientEditForm(editForm):
    def __init__(self, parent=None, travel=None):
        editForm.__init__(self, tablewidget=ClientTable(travel=travel), parent=parent, travel=travel)

        self.__surnameEdit = QLineEdit()
        self.__nameEdit = QLineEdit()
        self.__middlenameEdit = QLineEdit()
        self.__addressEdit = QLineEdit()
        self.__phoneEdit = QLineEdit()

        self.addLabel(u'surname', 0, 0)
        self.addNewWidget(self.__surnameEdit, 0, 1)
        self.addLabel(u'name', 1, 0)
        self.addNewWidget(self.__nameEdit, 1, 1)
        self.addLabel(u'middlename', 2, 0)
        self.addNewWidget(self.__middlenameEdit, 2, 1)
        self.addLabel(u'address', 3, 0)
        self.addNewWidget(self.__addressEdit, 3, 1)
        self.addLabel(u'phone', 4, 0)
        self.addNewWidget(self.__phoneEdit, 4, 1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getTravel().getClientCodes():
            self.__surnameEdit.setText(self.getTravel().getClient(self.getCurrentCode()).getSurname())
            self.__nameEdit.setText(self.getTravel().getClient(self.getCurrentCode()).getName())
            self.__middlenameEdit.setText(self.getTravel().getClient(self.getCurrentCode()).getMiddlename())
            self.__addressEdit.setText(self.getTravel().getClient(self.getCurrentCode()).getAddress())
            self.__phoneEdit.setText(self.getTravel().getClient(self.getCurrentCode()).getPhone())

    def editClick(self):
        self.getTravel().getClient(self.getCurrentCode()).setSurname(self.__surnameEdit.text())
        self.getTravel().getClient(self.getCurrentCode()).setName(self.__nameEdit.text())
        self.getTravel().getClient(self.getCurrentCode()).setMiddlename(self.__middlenameEdit.text())
        self.getTravel().getClient(self.getCurrentCode()).setAddress(self.__addressEdit.text())
        self.getTravel().getClient(self.getCurrentCode()).setPhone(self.__phoneEdit.text())
        self.tableUpdate()

    def newClick(self):
        code = self.getTravel().getClientNewCode()
        self.getTravel().createClient(code)
        self.getTravel().getClient(code).setSurname(self.__surnameEdit.text())
        self.getTravel().getClient(code).setName(self.__nameEdit.text())
        self.getTravel().getClient(code).setMiddlename(self.__middlenameEdit.text())
        self.getTravel().getClient(code).setAddress(self.__addressEdit.text())
        self.getTravel().getClient(code).setPhone(self.__phoneEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getTravel().removeClient(self.getCurrentCode())
        self.tableUpdate()


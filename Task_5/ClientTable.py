from PyQt6.QtWidgets import QTableWidgetItem
from dbTableWidget import dbTableWidget


class ClientTable(dbTableWidget):
    def __init__(self, travel, parent=None):
        dbTableWidget.__init__(self, travel=travel,
                               header=[u'surname', u'name', u'middlename', u'address', u'phone'],
                               parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getTravel().getClientCodes()))
        r = 0
        for a in self.getTravel().getClientCodes():
            self.setItem(r, 0, QTableWidgetItem(self.getTravel().getClient(a).getSurname()))
            self.setItem(r, 1, QTableWidgetItem(self.getTravel().getClient(a).getName()))
            self.setItem(r, 2, QTableWidgetItem(self.getTravel().getClient(a).getMiddlename()))
            self.setItem(r, 3, QTableWidgetItem(self.getTravel().getClient(a).getAddress()))
            self.setItem(r, 4, QTableWidgetItem(self.getTravel().getClient(a).getPhone()))

            self.appendRowCode(r, a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0, 0)


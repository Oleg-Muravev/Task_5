from PyQt6.QtWidgets import QTableWidgetItem
from dbTableWidget import dbTableWidget


class TravelTable(dbTableWidget):
    def __init__(self, travel, parent=None):
        dbTableWidget.__init__(self, travel=travel,
                               header=[u'route', u'clients', u'date', u'quantity', u'discount'],
                               parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getTravel().getTravelCodes()))
        r = 0
        for a in self.getTravel().getTravelCodes():
            self.setItem(r, 0, QTableWidgetItem(self.getTravel().getTravel(a).getRoute().getCountryNames()))
            self.setItem(r, 1, QTableWidgetItem(self.getTravel().getTravel(a).getClient().getClientSurnames()))
            self.setItem(r, 2, QTableWidgetItem(self.getTravel().getTravel(a).getDate()))
            self.setItem(r, 3, QTableWidgetItem(str(self.getTravel().getTravel(a).getQuantity())))
            self.setItem(r, 4, QTableWidgetItem(str(self.getTravel().getTravel(a).getDiscount())))
            self.appendRowCode(r, a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0, 0)


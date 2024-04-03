from PyQt6.QtWidgets import QTableWidgetItem
from dbTableWidget import dbTableWidget


class RouteTable(dbTableWidget):
    def __init__(self, travel, parent=None):
        dbTableWidget.__init__(self, travel=travel,
                               header=[u'country', u'climate', u'duration', u'hotel', u'cost'],
                               parent=parent)

    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getTravel().getRouteCodes()))
        r = 0
        for a in self.getTravel().getRouteCodes():
            self.setItem(r, 0, QTableWidgetItem(self.getTravel().getRoute(a).getCountry()))
            self.setItem(r, 1, QTableWidgetItem(self.getTravel().getRoute(a).getClimate()))
            self.setItem(r, 2, QTableWidgetItem(str(self.getTravel().getRoute(a).getDuration())))
            self.setItem(r, 3, QTableWidgetItem(self.getTravel().getRoute(a).getHotel()))
            self.setItem(r, 4, QTableWidgetItem(str(self.getTravel().getRoute(a).getCost())))

            self.appendRowCode(r, a)
            r += 1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0, 0)


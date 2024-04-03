from PyQt6.QtWidgets import QTableWidget
from RowCode import RowCode
from TravelWidget import travelWidget


class dbTableWidget(QTableWidget, travelWidget):
    def __init__(self, travel, parent=None, header=[]):
        QTableWidget.__init__(self)
        travelWidget.__init__(self, travel)
        self.__rowCode = RowCode()
        self.setHeader(header)
        self.update()

    def setHeader(self, value):
        self.setColumnCount(len(value))
        self.setHorizontalHeaderLabels(value)

    def clearContents(self):
        self.__rowCode.clear()
        QTableWidget.clearContents(self)

    def getCodes(self):
        return self.__rowCode.getCodes()

    def getCurrentCode(self):
        return self.__rowCode.getCode(self.currentRow())

    def appendRowCode(self, row, code):
        self.__rowCode.appendRowCode(row, code)

    def update(self,code=0):
        self.clearContents()
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCode(code)
        
    def setData(self):pass

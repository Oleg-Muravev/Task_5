from PyQt6.QtWidgets import QListWidget
from RowCode import RowCode
from TravelWidget import travelWidget


class dbListWidget(QListWidget, travelWidget):
    def __init__(self, parent=None, travel=None):
        QListWidget.__init__(self, parent)
        travelWidget.__init__(self, travel)
        self.__rowCode = RowCode()

    def clear(self):
        self.__rowCode.clear()
        QListWidget.clear(self)

    def addItem(self, code, text):
        self.__rowCode.appendRowCode(self.count(), code)
        QListWidget.addItem(self, str(text))

    def removeSelected(self):
        self.__rowCode.removeRow(self.currentRow())
        for item in self.selectedItems():
            self.takeItem(self.row(item))

    def getCurrentCode(self):
        return self.__rowCode.getCode(self.currentRow())

    def setCurrentRec(self, value):
        self.__currentRec = value
        self.update()

    def getCurrentRec(self):
        return self.__currentRec

    def getCodes(self):
        return self.__rowCode.getCodes()

    def update(self):
        pass


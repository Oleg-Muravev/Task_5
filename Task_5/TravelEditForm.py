from PyQt6.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QLabel, QSpinBox, QFileDialog
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap
from EditForm import editForm
from dbListWidget import dbListWidget
from dbComboBox import dbComboBox
from RouteCombo import routeCombo
from ClientCombo import clientCombo
from RouteListWidget import routeListWidget
from ClientListWidget import clientListWidget
from TravelTable import TravelTable


class travelEditForm(editForm):
    def __init__(self, parent=None, travel=None):
        editForm.__init__(self, tablewidget=TravelTable(travel=travel), parent=parent, travel=travel)

        self.__routeListWidget = routeListWidget(travel=travel)
        self.__routeCombo = routeCombo(travel=travel)
        self.__routeRemoveButton = QPushButton(u'delete')
        self.__routeAppendButton = QPushButton(u'add')

        self.__clientListWidget = clientListWidget(travel=travel)
        self.__clientCombo = clientCombo(travel=travel)
        self.__clientRemoveButton = QPushButton(u'delete')
        self.__clientAppendButton = QPushButton(u'add')
        

        self.__dateEdit = QLineEdit()
        self.__quantityEdit = QLineEdit()
        self.__discountEdit = QLineEdit()
  

        self.addLabel(u'route', 0, 0)
        self.addNewWidget(self.__routeListWidget, 0, 1)
        self.addNewWidget(self.__routeRemoveButton, 0, 2)
        self.addNewWidget(self.__routeCombo, 1, 1)
        self.addNewWidget(self.__routeAppendButton, 1, 2)

        self.addLabel(u'client', 2, 0)
        self.addNewWidget(self.__clientListWidget, 2, 1)
        self.addNewWidget(self.__clientRemoveButton, 2, 2)
        self.addNewWidget(self.__clientCombo, 3, 1)
        self.addNewWidget(self.__clientAppendButton, 3, 2)

        self.addLabel(u'date', 4, 0)
        self.addNewWidget(self.__dateEdit, 4, 1)
        self.addLabel(u'quantity', 5, 0)
        self.addNewWidget(self.__quantityEdit, 5, 1)
        self.addLabel(u'discount', 6, 0)
        self.addNewWidget(self.__discountEdit, 6, 1)

        self.__routeRemoveButton.clicked.connect(self.removeRoute)
        self.__routeAppendButton.clicked.connect(self.appendRoute)

        self.__clientRemoveButton.clicked.connect(self.removeClient)
        self.__clientAppendButton.clicked.connect(self.appendClient)

        self.setCurrentCode()

    def removeRoute(self):
        code = self.__routeListWidget.getCurrentCode()
        if code:
            self.__routeListWidget.removeSelected()
            self.__routeCombo.addItem(code, self.getTravel().getRoute(code).getCountry())

    def appendRoute(self):
        code = self.__routeCombo.getCurrentCode()
        if code:
            self.__routeCombo.removeItem(self.__routeCombo.currentIndex())
            self.__routeListWidget.addItem(code, self.getTravel().getRoute(code).getCountry())

    def removeClient(self):
        code = self.__clientListWidget.getCurrentCode()
        if code:
            self.__clientListWidget.removeSelected()
            self.__clientCombo.addItem(code, self.getTravel().getClient(code).getSurname())

    def appendClient(self):
        code = self.__clientCombo.getCurrentCode()
        if code:
            self.__clientCombo.removeItem(self.__routeCombo.currentIndex())
            self.__clientListWidget.addItem(code, self.getTravel().getClient(code).getSurname())

    def update(self):
        if self.getCurrentCode() in self.getTravel().getTravelCodes():
            # self.__routeEdit.setText(self.getTravel().getTravel(self.getCurrentCode()).getRoute())
            # self.__clientEdit.setText(self.getTravel().getTravel(self.getCurrentCode()).getClient())
            self.__dateEdit.setText(self.getTravel().getTravel(self.getCurrentCode()).getDate())
            self.__quantityEdit.setText(str(self.getTravel().getTravel(self.getCurrentCode()).getQuantity()))
            self.__discountEdit.setText(str(self.getTravel().getTravel(self.getCurrentCode()).getDiscount()))

            self.__routeCombo.setCurrentRec(self.getCurrentCode())
            self.__routeListWidget.setCurrentRec(self.getCurrentCode())

            self.__clientCombo.setCurrentRec(self.getCurrentCode())
            self.__clientListWidget.setCurrentRec(self.getCurrentCode())

    def editClick(self):
        self.getTravel().getTravel(self.getCurrentCode()).setDate(self.__dateEdit.text())
        self.getTravel().getTravel(self.getCurrentCode()).setQuantity(self.__quantityEdit.text())
        self.getTravel().getTravel(self.getCurrentCode()).setDiscount(self.__discountEdit.text())

        self.getTravel().getTravel(self.getCurrentCode()).removeRoutes()
        for route in self.__routeListWidget.getCodes():
            self.getTravel().getTravel(self.getCurrentCode()).appendRoute(self.getTravel().findRouteByCode(route))

        self.getTravel().getTravel(self.getCurrentCode()).removeClients()
        for client in self.__clientListWidget.getCodes():
            self.getTravel().getTravel(self.getCurrentCode()).appendClient(self.getTravel().findClientByCode(client))

        self.tableUpdate()

    def newClick(self):
        code = self.getTravel().getTravelNewCode()
        self.getTravel().createTravel(code)

        for route in self.__routeListWidget.getCodes():
            self.getTravel().getTravel(code).appendRoute(self.getTravel().findRouteByCode(route))

        for client in self.__clientListWidget.getCodes():
            self.getTravel().getTravel(code).appendClient(self.getTravel().findClientByCode(client))

        self.getTravel().getTravel(code).setDate(self.__dateEdit.text())
        self.getTravel().getTravel(code).setQuantity(self.__quantityEdit.text())
        self.getTravel().getTravel(code).setDiscount(self.__discountEdit.text())

        self.tableUpdate()

    def delClick(self):
        self.getTravel().removeTravel(self.getCurrentCode())
        self.tableUpdate()


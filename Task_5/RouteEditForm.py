from PyQt6.QtWidgets import QLineEdit
from EditForm import editForm
from RouteTable import RouteTable


class routeEditForm(editForm):
    def __init__(self, parent=None, travel=None):
        editForm.__init__(self, tablewidget=RouteTable(travel=travel), parent=parent, travel=travel)

        self.__countryEdit = QLineEdit()
        self.__climateEdit = QLineEdit()
        self.__durationEdit = QLineEdit()
        self.__hotelEdit = QLineEdit()
        self.__costEdit = QLineEdit()

        self.addLabel(u'country', 0, 0)
        self.addNewWidget(self.__countryEdit, 0, 1)
        self.addLabel(u'climate', 1, 0)
        self.addNewWidget(self.__climateEdit, 1, 1)
        self.addLabel(u'duration', 2, 0)
        self.addNewWidget(self.__durationEdit, 2, 1)
        self.addLabel(u'hotel', 3, 0)
        self.addNewWidget(self.__hotelEdit, 3, 1)
        self.addLabel(u'cost', 4, 0)
        self.addNewWidget(self.__costEdit, 4, 1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getTravel().getRouteCodes():
            self.__countryEdit.setText(self.getTravel().getRoute(self.getCurrentCode()).getCountry())
            self.__climateEdit.setText(self.getTravel().getRoute(self.getCurrentCode()).getClimate())
            self.__durationEdit.setText(str(self.getTravel().getRoute(self.getCurrentCode()).getDuration()))
            self.__hotelEdit.setText(self.getTravel().getRoute(self.getCurrentCode()).getHotel())
            self.__costEdit.setText(str(self.getTravel().getRoute(self.getCurrentCode()).getCost()))

    def editClick(self):
        self.getTravel().getRoute(self.getCurrentCode()).setCountry(self.__countryEdit.text())
        self.getTravel().getRoute(self.getCurrentCode()).setClimate(self.__climateEdit.text())
        self.getTravel().getRoute(self.getCurrentCode()).setDuration(self.__durationEdit.text())
        self.getTravel().getRoute(self.getCurrentCode()).setHotel(self.__hotelEdit.text())
        self.getTravel().getRoute(self.getCurrentCode()).setCost(self.__costEdit.text())
        self.tableUpdate()

    def newClick(self):
        code = self.getTravel().getRouteNewCode()
        self.getTravel().createRoute(code)
        self.getTravel().getRoute(code).setCountry(self.__countryEdit.text())
        self.getTravel().getRoute(code).setClimate(self.__climateEdit.text())
        self.getTravel().getRoute(code).setDuration(self.__durationEdit.text())
        self.getTravel().getRoute(code).setHotel(self.__hotelEdit.text())
        self.getTravel().getRoute(code).setCost(self.__costEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getTravel().removeRoute(self.getCurrentCode())
        self.tableUpdate()


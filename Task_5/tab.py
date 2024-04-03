from PyQt6.QtWidgets import QTabWidget
import sys, os
from RouteEditForm import routeEditForm
from ClientEditForm import clientEditForm
from TravelEditForm import travelEditForm


class tabWidget(QTabWidget):
    def __init__(self, travel, parent=None):
        QTabWidget.__init__(self, parent)
        self.__routeEditForm = routeEditForm(travel=travel)
        self.addTab(self.__routeEditForm, u"routes")
        self.__clientEditForm = clientEditForm(travel=travel)
        self.addTab(self.__clientEditForm, u"clients")
        self.__travelEditForm = travelEditForm(travel=travel)
        self.addTab(self.__travelEditForm, u"travels")

    def update(self):
        self.__routeEditForm.tableUpdate()
        self.__clientEditForm.tableUpdate()
        self.__travelEditForm.tableUpdate()


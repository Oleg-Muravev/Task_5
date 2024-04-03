from PyQt6.QtWidgets import QApplication
import sys

sys.path.insert(0, "./travel")
from TravelCompany import TravelCompany
from DataXML import DataXML
from TravelTable import TravelTable
from RouteTable import RouteTable
from ClientTable import ClientTable
from RouteEditForm import routeEditForm
from ClientEditForm import clientEditForm
from TravelEditForm import travelEditForm


app = QApplication(sys.argv)

tr = TravelCompany()
dat1 = DataXML(tr, 'old.xml')
dat1.read()

w1 = TravelTable(tr)
w1 = RouteTable(tr)
w1 = ClientTable(tr)
w1 = routeEditForm(travel=tr)
w1 = clientEditForm(travel=tr)
w1 = travelEditForm(travel=tr)
w1.update()
w1.show()

sys.exit(app.exec())


from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QIcon, QAction
import sys, os

sys.path.insert(0, "./travel")

from TravelCompany import TravelCompany
from DataXML import DataXML
from TravelTable import TravelTable
from RouteTable import RouteTable
from ClientTable import ClientTable
from RouteEditForm import routeEditForm
from ClientEditForm import clientEditForm
from TravelEditForm import travelEditForm

from DataSQL import DataSQL
from DataXML import DataXML
from DataJSON import DataJSON
from TravelCompany import TravelCompany
from tab import tabWidget

app = QApplication(sys.argv)

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(u"Travel Agency")
        self.travel = TravelCompany()
        self.dataxml = DataXML(self.travel)
        self.datasql = DataSQL(self.travel)
        self.tabWidget = tabWidget(self.travel, self)
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.update()

        self.new = QAction(QIcon(), 'New', self)
        self.new.setStatusTip('New databsae')
        self.new.triggered.connect(self.newAction)

        self.openxml = QAction(QIcon(), 'Open XML', self)
        self.openxml.setStatusTip('Open data from XML')
        self.openxml.triggered.connect(self.openXMLAction)

        self.opensql = QAction(QIcon(), 'Open SQL', self)
        self.opensql.setStatusTip('Open data from SQL')
        self.opensql.triggered.connect(self.openSQLAction)

        self.savexml = QAction(QIcon(), 'Save XML', self)
        self.savexml.setStatusTip('Save data to XML')
        self.savexml.triggered.connect(self.saveXMLAction)

        self.savesql = QAction(QIcon(), 'Save SQL', self)
        self.savesql.setStatusTip('Save data to SQL')
        self.savesql.triggered.connect(self.saveSQLAction)

        self.menubar = self.menuBar()
        self.menufile = self.menubar.addMenu("&File")
        self.menufile.addAction(self.new)
        self.menufile.addSeparator()
        self.menufile.addAction(self.openxml)
        self.menufile.addAction(self.opensql)
        self.menufile.addSeparator()
        self.menufile.addAction(self.savexml)
        self.menufile.addAction(self.savesql)
        self.statusBar()

    def newAction(self):
        self.travel.clear()
        self.tabWidget.update()

    def openXMLAction(self):
        filename = QFileDialog.getOpenFileName(self, u'Open XML', os.getcwd(), u"*.xml")[0]
        if filename:
            self.travel.clear()
            self.dataxml.readFile(filename)
            self.tabWidget.update()

    def openSQLAction(self):
        filename = QFileDialog.getOpenFileName(self, u'Open SSQL', os.getcwd(), u"*.sqlite")[0]
        if filename:
            self.travel.clear()
            self.datasql.readFile(filename)
            self.tabWidget.update()

    def saveXMLAction(self):
        filename = QFileDialog.getSaveFileName(self, u'Save XML', os.getcwd(), u'*.xml')[0]
        if filename:
            self.dataxml.writeFile(filename)

    def saveSQLAction(self):
        filename = QFileDialog.getSaveFileName(self, u'Save SQL', os.getcwd(), u'*.sqlite')[0]
        if filename:
            self.datasql.writeFile(filename)


mw = mainWindow()
mw.show()
sys.exit(app.exec())


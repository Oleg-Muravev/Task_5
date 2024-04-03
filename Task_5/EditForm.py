from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from TravelWidget import travelWidget


class editForm(QWidget, travelWidget):
    def __init__(self, tablewidget=None, parent=None, travel=None):
        QWidget.__init__(self, parent=parent)
        travelWidget.__init__(self, travel)
        self.__tablewidget = tablewidget
        self.__mainvbox = QVBoxLayout()
        self.__mainvbox.addWidget(self.__tablewidget)
        self.__grid = QGridLayout()
        self.__vbox = QVBoxLayout()
        self.__hbox = QHBoxLayout()
        self.__vbox.addLayout(self.__grid)
        self.__vbox.addStretch(1)
        self.__hbox.addLayout(self.__vbox)
        self.__buttonsVBox = QVBoxLayout()
        self.__hbox.addLayout(self.__buttonsVBox)
        self.__newButton = QPushButton(u"add")
        self.__editButton = QPushButton(u"edit")
        self.__delButton = QPushButton(u"delete")
        self.__buttonsVBox.addWidget(self.__newButton)
        self.__buttonsVBox.addWidget(self.__editButton)
        self.__buttonsVBox.addWidget(self.__delButton)
        self.__buttonsVBox.addStretch(1)
        self.__mainvbox.addLayout(self.__hbox)
        self.setLayout(self.__mainvbox)
        self.__newButton.clicked.connect(self.newClick)
        self.__editButton.clicked.connect(self.editClick)
        self.__delButton.clicked.connect(self.delClick)
        self.__tablewidget.currentCellChanged.connect(self.tableClick)

    def getGreed(self):
        return self.__grid

    def addLabel(self, text, x, y):
        self.__grid.addWidget(QLabel(text), x, y)

    def addNewWidget(self, widget, x, y):
        self.__grid.addWidget(widget, x, y)

    def addLeftLayout(self, layout):
        self.__hbox.insertLayout(0, layout)

    def setCurrentCode(self):
        self.__currentCode = self.__tablewidget.getCurrentCode()
        self.update()

    def getCurrentCode(self):
        return self.__currentCode

    def decode(self, qstring): return str(qstring.toUtf8()).decode('utf - 8')

    def newClick(self): pass

    def editClick(self): pass

    def delClick(self): pass

    def update(self): pass

    def tableClick(self):
        self.setCurrentCode()

    def tableUpdate(self):
        self.__tablewidget.update()


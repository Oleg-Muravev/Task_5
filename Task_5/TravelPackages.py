from ClientList import ClientList
from General import General
from RouteList import RouteList

class Packages(General):
    def __init__(self, code=0, date='', quantity=0, discount=0):
        General.__init__(self, code)
        self.__clientList = ClientList()
        self.__routeList = RouteList()
        self.setDate(date)
        self.setQuantity(quantity)
        self.setDiscount(discount)

    def setDate(self, value):
        self.__date = value
    def setQuantity(self, value):
        self.__quantity = value
    def setDiscount(self, value):
        self.__discount = value
    def getRoute(self):
        return self.__routeList
    def getClient(self):
        return self.__clientList
    def getDate(self):
        return self.__date
    def getQuantity(self):
        return self.__quantity
    def getDiscount(self):
        return self.__discount

    def appendClient(self, value):
        self.__clientList.appendItem(value)
    def removeClient(self, value):
        self.__clientList.removeItem(value)
    def removeClients(self):
        self.__clientList.clear()
    def appendRoute(self, value):
        self.__routeList.appendItem(value)
    def removeRoute(self, value):
        self.__routeList.removeItem(value)
    def removeRoutes(self):
        self.__routeList.clear()
    
    def getClientCodes(self):
        return self.__clientList.getCodes()
    def getRouteCodes(self):
        return self.__routeList.getCodes()

    def getPackageInf(self):
        s = 'Information about travel package:\n'
        s += f'Clients => {self.__clientList.getStr()}\n'
        s += f'Route => {self.__routeList.getStr()}\n'
        s += f'Data => {self.__date}\n'
        s += f'Discount => {self.__discount}\n'
        return s



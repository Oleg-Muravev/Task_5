from ClientList import ClientList
from RouteList import RouteList
from TravelList import TravelList

class TravelCompany:
    def __init__(self):
        self.__routeList = RouteList()
        self.__clientList = ClientList()
        self.__travelList = TravelList()
        
    def clear(self):
        self.__routeList.clear()
        self.__clientList.clear()
        self.__travelList.clear()
      
    def createRoute(self, code, country='', climate='', duration=0, hotel='', cost=0):
        self.__routeList.createItem(code, country, climate, duration, hotel, cost)
    def newRoute(self, country='', climate='', duration=0, hotel='', cost=0):
        self.__routeList.newItem(country, climate, duration, hotel, cost)
    def removeRoute(self, value):
        self.__routeList.removeItem(value)
    def getRoute(self, code):
        return self.__routeList.findByCode(code)
    def getRouteList(self):
        return self.__routeList.getItems()
    def getRouteCodes(self):
        return self.__routeList.getCodes()
    def getRouteNewCode(self):
        return max(self.getRouteCodes()) + 1 if self.getRouteCodes() != [] else 0   
    def findRouteByCode(self, code):
        return self.__routeList.findByCode(code)
    
    def createClient(self, code, surname='', name='', middlename='', address='', phone=''):
        self.__clientList.createItem(code, surname, name, middlename, address, phone)
    def newClient(self, surname='', name='', middlename='', address='', phone=''):
        self.__clientList.newItem(surname, name, middlename, address, phone)
    def removeClient(self, value):
        self.__clientList.removeItem(value)
    def getClient(self, code):
        return self.__clientList.findByCode(code)
    def getClientList(self):
        return self.__clientList.getItems()
    def getClientCodes(self):
        return self.__clientList.getCodes()
    def getClientNewCode(self):
        return max(self.getClientCodes()) + 1 if self.getClientCodes() != [] else 0
    def findClientByCode(self, code):
        return self.__clientList.findByCode(code)
    

    def createTravel(self, code, date='', quantity=0, discount=0):
        self.__travelList.createItem(code, date, quantity, discount)
    def newTravel(self, date='', quantity=0, discount=0):
        self.__travelList.newItem(date, quantity, discount)
    def removeTravel(self, value):
        self.__travelList.removeItem(value)
    def getTravel(self, code):
        return self.__travelList.findByCode(code)
    def getTravelList(self):
        return self.__travelList.getItems()
    def getTravelCodes(self):
        return self.__travelList.getCodes()
    def getTravelNewCode(self):
        return max(self.getTravelCodes()) + 1 if self.getTravelCodes() != [] else 0
    def getTravelRouteCodes(self, code):
        return self.getTravel(code).getRoute().getCodes()
    def getTravelClientCodes(self, code):
        return self.getTravel(code).getClient().getCodes()
    
    def getStr(self, code):
        s = 'Information about travel package:\n'
        s += f'Clients => {self.getTravel(code).getClient().getStr()}\n'
        s += f'Route => {self.getTravel(code).getRoute().getStr()}\n'
        s += f'Data => {self.getTravel(code).getDate()}\n'
        s += f'Discount => {self.getTravel(code).getDiscount()}\n'
        return s


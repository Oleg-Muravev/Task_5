from GeneralList import GeneralList
from Routes import Routes

class RouteList(GeneralList):
    def createItem(self, code, country='', climate='', duration=0, hotel='', cost=0):
        if code in self.getCodes():
            print(f'The route with the code {code} already exists!!!')
        else:
            GeneralList.appendItem(self, Routes(code, country, climate, duration, hotel, cost))
            
    def newItem(self, country='', climate='', duration=0, hotel='', cost=0):
        GeneralList.appendItem(self, Routes(self.getNewCode(), country, climate, duration, hotel, cost))


    def getStr(self):
        s = ''
        for i in self.getItems():
            s += i.getRouteInf() + ' ||| '
        return s
    
    def getCountryNames(self):
        s = ''
        for i in self.getItems():
            s += ' --> ' + i.getCountry() 

        return s



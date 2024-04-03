from GeneralList import GeneralList
from TravelPackages import Packages

class TravelList(GeneralList):
    def createItem(self, code, date='', quantity=0, discount=0):
        if code in self.getCodes():
            print(f'The entry with the code {code} already exists!!!')
        else:
            GeneralList.appendItem(self, Packages(code, date, quantity, discount))
            
    def newItem(self, date='', quantity=0, discount=0):
        GeneralList.appendItem(self, Packages(self.getNewCode(), date, quantity, discount))
    
        
    def getStr(self):
        s = ''
        for i in self.getItems():
            s += i.getClientStr() + ' ||| '
        return s


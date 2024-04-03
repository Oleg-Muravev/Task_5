from General import General

class GeneralList(General):
    def __init__(self):
        self.__list = []
    def clear(self):
        self.__list = []
        
    def findByCode(self, code):
        for i in self.__list:
            if i.getCode() == code:
                return i
    def getNewCode(self):
        if not self.__list:
            return 1
        return max(self.getCodes()) + 1
    def getCodes(self):
        return [s.getCode() for s in self.__list]
    def getItems(self):
        return [i for i in self.__list]
    
    def appendItem(self, value):
        self.__list.append(value)
    def removeItem(self, value):
        if isinstance(value, General):
            self.__list.remove(value)
        if isinstance(value, int):
            self.__list.remove(self.findByCode(value))

    def getStr(self):
        pass


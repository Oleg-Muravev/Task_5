from General import General

class Client(General):
    def __init__(self, code=0, surname='', name='', middlename='', address='', phone=''):
        General.__init__(self, code)
        self.setSurname(surname)
        self.setName(name)
        self.setMiddlename(middlename)
        self.setAddress(address)
        self.setPhone(phone)

    def setSurname(self, value):
        self.__surname = value
    def setName(self, value):
        self.__name = value
    def setMiddlename(self, value):
        self.__middlename = value
    def setAddress(self, value):
        self.__address = value
    def setPhone(self, value):
        self.__phone = value
    def getSurname(self):
        return self.__surname
    def getName(self):
        return self.__name
    def getMiddlename(self):
        return self.__middlename
    def getAddress(self):
        return self.__address
    def getPhone(self):
        return self.__phone

    def getClientInf(self):
        return self.__name + ' ' + self.__surname + ' ' + self.__phone



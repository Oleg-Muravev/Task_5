from GeneralList import GeneralList
from Client import Client

class ClientList(GeneralList):
    def createItem(self, code, surname='', name='', middlename='', address='', phone=''):
        if code in self.getCodes():
            print(f'The client with the code {code} already exists!!!')
        else:
            GeneralList.appendItem(self, Client(code, surname, name, middlename, address, phone))
            
    def newItem(self, surname='', name='', middlename='', address='', phone=''):
        GeneralList.appendItem(self, Client(self.getNewCode(), surname, name, middlename, address, phone))


    def getStr(self):
        s = ''
        for i in self.getItems():
            s += i.getClientInf() + ' ||| '
        return s

    def getClientSurnames(self):
        s = ''
        for i in self.getItems():
            s += i.getSurname() + ' | '
        return s

     

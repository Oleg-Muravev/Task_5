class Data:
    def __init__(self, data=None, inp='', out=''):
        self.setData(data)
        self.setInp(inp)
        self.setOut(out)
        
    def setData(self, data):
        self.__data = data
    def setInp(self, inp):
        self.__inp = inp
    def setOut(self, out):
        self.__out = out
    def getData(self):
        return self.__data
    def getInp(self):
        return self.__inp
    def getOut(self):
        return self.__out
    
    def readFile(self, filename):
        self.setInp(filename)
        self.read()
    def writeFile(self, filename):
        self.setOut(filename)
        self.write()
    def read(self):
        pass
    def write(self):
        pass


from General import General

class Routes(General):
    def __init__(self, code=0, country='', climate='', duration=0, hotel='', cost=0):
        General.__init__(self, code)
        self.setCountry(country)
        self.setClimate(climate)
        self.setDuration(duration)
        self.setHotel(hotel)
        self.setCost(cost)

    def setCountry(self, value):
        self.__country = value
    def setClimate(self, value):
        self.__climate = value
    def setDuration(self, value):
        self.__duration = value
    def setHotel(self, value):
        self.__hotel = value
    def setCost(self, value):
        self.__cost = value
    def getCountry(self):
        return self.__country
    def getClimate(self):
        return self.__climate
    def getDuration(self):
        return self.__duration
    def getHotel(self):
        return self.__hotel
    def getCost(self):
        return self.__cost

    def getRouteInf(self):
        return self.__country + ' ' + str(self.__duration) + ' ' + str(self.__cost)



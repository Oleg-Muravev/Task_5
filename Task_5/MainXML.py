from TravelCompany import TravelCompany
from DataXML import DataXML

travel = TravelCompany()
data = DataXML(travel, 'old.xml', 'new.xml')

data.read()
data.write()

for k in travel.getTravelCodes():
    print(travel.getStr(k))


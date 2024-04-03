from TravelCompany import TravelCompany
from DataJSON import DataJSON

travel = TravelCompany()
data = DataJSON(travel, 'old.json', 'new.json')

data.read()
data.write()

for k in travel.getTravelCodes():
    print(travel.getStr(k))

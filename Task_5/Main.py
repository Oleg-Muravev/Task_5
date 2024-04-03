from Client import Client
from Routes import Routes
from TravelPackages import Packages

Client_1 = Client(surname='M.', name='Oleg', middlename='D.', address='Home', phone='+79999999')
route_1 = Routes(country='Russia', climate='Cold', duration=3, hotel='Volga Hotel', cost=10000)
package_1 = Packages(date='27.10.2023', quantity=1, discount=0)
package_1.appendRoute(route_1)
package_1.appendClient(Client_1)
print(package_1.getPackageInf())

route_2 = Routes(country='Thailand', climate='Tropical', duration=12, hotel='Sea Hotel', cost=150000)
package_2 = Packages(date='15.01.2024', quantity=1, discount=0)
package_2.appendRoute(route_2)
package_2.appendClient(Client_1)
print(package_2.getPackageInf())



import os, xml.dom.minidom
from Data import Data

class DataXML(Data):
    def read(self):
        dom = xml.dom.minidom.parse(self.getInp()) # открытие файла
        dom.normalize() # нормализация структуры XML-документа
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'client'):
                code, surname, name, middlename, address, phone = 0, '', '', '', '', ''
                for t in node.attributes.items():
                    if t[0] == 'code':
                        code = int(t[1])
                    if t[0] == 'surname':
                        surname = t[1]
                    if t[0] == 'name':
                        name = t[1]
                    if t[0] == 'middlename':
                        middlename = t[1]
                    if t[0] == 'address':
                        address = t[1]
                    if t[0] == 'phone':
                        phone = t[1]
                self.getData().createClient(code, surname, name, middlename, address, phone)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'route'):
                code, country, climate, duration, hotel, cost = 0, '', '', 0, '', 0
                for t in node.attributes.items():
                    if t[0] == 'code':
                        code = int(t[1])
                    if t[0] == 'country':
                        country = t[1]
                    if t[0] == 'climate':
                        climate = t[1]
                    if t[0] == 'duration':
                        duration = int(t[1])
                    if t[0] == 'hotel':
                        hotel = t[1]
                    if t[0] == 'cost':
                        cost = int(t[1])
                self.getData().createRoute(code, country, climate, duration, hotel, cost)
            if (node.nodeType == node.ELEMENT_NODE) and (node.nodeName == 'travel'):
                code, date, quantity, discount = 0, '', 0, 0
                for t in node.attributes.items():
                    if t[0] == 'code':
                        code = int(t[1])
                    if t[0] == 'date':
                        date = t[1]
                    if t[0] == 'quantity':
                        quantity = int(t[1])
                    if t[0] == 'discount':
                        discount = int(t[1])
                self.getData().createTravel(code, date, quantity, discount)
                travel_data = self.getData().getTravel(code)
                for n in node.childNodes:
                    if (n.nodeType == n.ELEMENT_NODE) and (n.nodeName == 'client'):
                        for t in n.attributes.items():
                            if t[0] == "code":
                                client = self.getData().getClient(int(t[1]))
                                travel_data.appendClient(client)
                    if (n.nodeType == n.ELEMENT_NODE) and (n.nodeName == 'route'):
                        for t in n.attributes.items():
                            if t[0] == "code":
                                route = self.getData().getRoute(int(t[1]))
                                travel_data.appendRoute(route)
                                
    def write(self):
        dom = xml.dom.minidom.Document()
        root = dom.createElement('data')
        dom.appendChild(root)
        for a in self.getData().getClientList():
            client = dom.createElement('client')
            client.setAttribute('code', str(a.getCode()))
            client.setAttribute('surname', str(a.getSurname()))
            client.setAttribute('name', str(a.getName()))
            client.setAttribute('middlename', str(a.getMiddlename()))
            client.setAttribute('address', str(a.getAddress()))
            client.setAttribute('phone', str(a.getPhone()))
            root.appendChild(client)
        for p in self.getData().getRouteList():
            route = dom.createElement('route')
            route.setAttribute('code', str(p.getCode()))
            route.setAttribute('country', str(p.getCountry()))
            route.setAttribute('climate', str(p.getClimate()))
            route.setAttribute('duration', str(p.getDuration()))
            route.setAttribute('hotel', str(p.getHotel()))
            route.setAttribute('cost', str(p.getCost()))
            root.appendChild(route)
        for i in self.getData().getTravelList():
            travel = dom.createElement('investment')
            travel.setAttribute('code', str(i.getCode()))
            travel.setAttribute('date', str(i.getDate()))
            travel.setAttribute('quantity', str(i.getQuantity()))
            travel.setAttribute('discount', str(i.getDiscount()))
            for p in i.getClient().getItems():
                client = dom.createElement('client')
                client.setAttribute('code', str(p.getCode()))
                travel.appendChild(client)
            for p in i.getRoute().getItems():
                route = dom.createElement('route')
                route.setAttribute('code', str(p.getCode()))
                travel.appendChild(route)
            root.appendChild(travel)
        f = open(self.getOut(), "w")
        f.write(dom.toprettyxml())


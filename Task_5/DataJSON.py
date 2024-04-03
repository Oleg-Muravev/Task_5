from Data import Data
import json


class DataJSON(Data):
    def read(self):
        with open(self.getInp(), "r") as read_file:
            data = json.load(read_file)
        for k in data.keys():
            if k == 'clients':
                for a in data[k]:
                    code, surname, name, middlename, address, phone = 0, '', '', '', '', ''
                    for ak in a.keys():
                        if ak == 'code':
                            code = a[ak]
                        if ak == 'surname':
                            surname = a[ak]
                        if ak == 'name':
                            name = a[ak]
                        if ak == 'middlename':
                            middlename = a[ak]
                        if ak == 'address':
                            address = a[ak]
                        if ak == 'phone':
                            phone = a[ak]
                    self.getData().createClient(code, surname, name, middlename, address, phone)

            if k == 'routes':
                for a in data[k]:
                    code, country, climate, duration, hotel, cost = 0, '', '', 0, '', 0
                    for ak in a.keys():
                        if ak == 'code':
                            code = a[ak]
                        if ak == 'country':
                            country = a[ak]
                        if ak == 'climate':
                            climate = a[ak]
                        if ak == 'duration':
                            duration = a[ak]
                        if ak == 'hotel':
                            hotel = a[ak]
                        if ak == 'cost':
                            cost = a[ak]
                    self.getData().createRoute(code, country, climate, duration, hotel, cost)

            if k == 'travels':
                for a in data[k]:
                    code, date, quantity, discount, clients, routes = 0, '', 0, 0, [], []
                    for ak in a.keys():
                        if ak == 'code':
                            code = a[ak]
                        if ak == 'date':
                            date = a[ak]
                        if ak == 'quantity':
                            quantity = a[ak]
                        if ak == 'discount':
                            discount = a[ak]
                        if ak == 'clients':
                            clients = a[ak]
                        if ak == 'routes':
                            routes = a[ak]
                    self.getData().createTravel(code, date, quantity, discount)
                    travel_data = self.getData().getTravel(code)
                    if clients:
                        for c in clients:
                            travel_data.appendClient(self.getData().getClient(c))
                    if routes:
                        for r in routes:
                            travel_data.appendRoute(self.getData().getRoute(r))

    def write(self):
        data = {'clients': [], 'routes': [], 'travels': []}
        for a in self.getData().getClientList():
            cd = {}
            cd['code'] = a.getCode()
            cd['surname'] = a.getSurname()
            cd['name'] = a.getName()
            cd['middlename'] = a.getMiddlename()
            cd['address'] = a.getAddress()
            cd['phone'] = a.getPhone()
            data['clients'].append(cd)

        for r in self.getData().getRouteList():
            rt = {}
            rt['code'] = r.getCode()
            rt['country'] = r.getCountry()
            rt['climate'] = r.getClimate()
            rt['duration'] = r.getDuration()
            rt['hotel'] = r.getHotel()
            rt['cost'] = r.getCost()
            data['routes'].append(rt)

        for t in self.getData().getTravelList():
            tr = {}
            tr['code'] = t.getCode()
            tr['date'] = t.getDate()
            tr['quantity'] = t.getQuantity()
            tr['discount'] = t.getDiscount()
            tr['clients'] = t.getClientCodes()
            tr['routes'] = t.getRouteCodes()
            data['travels'].append(tr)

        with open(self.getOut(), "w") as write_file:
            json.dump(data, write_file, ensure_ascii=False)

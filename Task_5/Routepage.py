class routepage:
    def __init__(self, travel):
        self.__travel = travel

    def index(self):
        s = '<a href=..>%s</a>/<a href=addform>%s</a>' % (u'назад', u'добавить')
        s += '<table><th bgcolor=gray></th>' \
             '<th bgcolor=gray>%s</th>' \
             '<th bgcolor=gray>%s</th>' \
             '<th bgcolor=gray>%s</th>' \
             '<th bgcolor=gray>%s</th>' \
             '<th bgcolor=gray>%s</th><th bgcolor=gray></th><th bgcolor=gray></th>' \
             % (u'Страна', u'Климат', u'Длительность', u'Отель', u'Стоимость')
        r = 1
        bg = ''
        for c in self.__travel.getRouteCodes():
            s += '<tr%s><td>%d</td>' % (bg, r)
            s += '<td>%s</td>' % self.__travel.getRoute(c).getCountry()
            s += '<td>%s</td>' % self.__travel.getRoute(c).getClimate()
            s += '<td>%s</td>' % self.__travel.getRoute(c).getDuration()
            s += '<td>%s</td>' % self.__travel.getRoute(c).getHotel()
            s += '<td>%s</td>' % self.__travel.getRoute(c).getCost()
            s += '<td><a href=editform?code=%s>%s</a></td>' % (c, u'редактировать')
            s += '<td><a href=delr?code=%s>%s</a></td></tr>' % (c, u'удалить')
            r += 1
            if bg:
                bg = ''
            else:
                bg = ' bgcolor = silver'
        s += '</table>'
        return s

    index.exposed = True

    def routeform(self, code=0, add=True):
        country, climate, duration, hotel, cost = '', '', 0, '', 0
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s' % code
        if code in self.__travel.getClientCodes():
            country = self.__travel.getClient(code).getSurname()
            climate = self.__travel.getClient(code).getName()
            duration = self.__travel.getClient(code).getMiddlename()
            hotel = self.__travel.getClient(code).getAddress()
            cost = self.__travel.getClient(code).getPhone()
        s = '''
            <form action=%s method=post>
            <table>
                <tr><td>%s</td><td><input type=text name=country value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=climate value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=duration value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=hotel value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=cost value=%s></td></tr>
                <tr><td><input type=submit></td><td></td></tr>
            </table>
            </form>''' % (
            a, u'Страна', country, u'Климат', climate, u'Длительность', duration, u'Отель', hotel, u'Стоимость', cost)

        return s

    def addaction(self, country, climate, duration, hotel, cost):
        code = self.__travel.getRouteNewCode()
        self.__travel.createRoute(code, country, climate, duration, hotel, cost)
        return 'Маршрут добавлен<br><a href = index>назад</a>'

    addaction.exposed = True

    def addform(self):
        s = u'Добавить маршрут'
        s += self.routeform(0)
        return s

    addform.exposed = True

    def editform(self, code):
        s = u'Редактировать маршрут<br>'
        s += self.routeform(int(code), False)
        return s

    editform.exposed = True

    def editaction(self, code, country, climate, duration, hotel, cost):
        self.__travel.getRoute(int(code)).setCountry(country)
        self.__travel.getRoute(int(code)).setClimate(climate)
        self.__travel.getRoute(int(code)).setDuration(duration)
        self.__travel.getRoute(int(code)).setHotel(hotel)
        self.__travel.getRoute(int(code)).setCost(cost)
        return 'Маршрут изменен<br><a href=index>Назад</a>'

    editaction.exposed = True

    def delr(self, code):
        self.__travel.removeRoute(int(code))
        return "Маршрут удален<br><a href=index>Назад</a>"

    delr.exposed = True
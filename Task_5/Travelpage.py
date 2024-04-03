class travelpage:
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
             % (u'Клиент', u'Маршрут', u'Дата', u'Количество', u'Скидка')
        r = 1
        bg = ''
        for c in self.__travel.getTravelCodes():
            s += '<tr%s><td>%d</td>' % (bg, r)
            s += '<td>%s</td>' % self.__travel.getTravel(c).getClient().getClientSurnames()
            s += '<td>%s</td>' % self.__travel.getTravel(c).getRoute().getCountryNames()
            s += '<td>%s</td>' % self.__travel.getTravel(c).getDate()
            s += '<td>%s</td>' % self.__travel.getTravel(c).getQuantity()
            s += '<td>%s</td>' % self.__travel.getTravel(c).getDiscount()
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

    def clientCombo(self, code=0):
        s = '<select name = client>'
        for c in self.__travel.getClientCodes():
            if not (c in self.__travel.getTravelClientCodes(code)):
                s += '<option value = %s>%s</option>' % (str(c), self.__travel.getClient(c).getName())
        s += '</select>'
        return s

    def routeCombo(self, code=0):
        s = '<select name = route>'
        for c in self.__travel.getRouteCodes():
            if not (c in self.__travel.getTravelRouteCodes(code)):
                s += '<option value = %s>%s</option>' % (str(c), self.__travel.getRoute(c).getCountry())
        s += '</select>'
        return s

    def clientList(self, code=0):
        s = '<table>'
        for c in self.__travel.getTravelClientCodes(code):
            s += '<tr><td>%s</td><td><a href = delclient?code=%s&acode=%s>%s</td></tr>' % (
                self.__travel.getClient(c).getName(), str(code), str(c), u'удалить')
        s += '</table>'
        return s

    def routetList(self, code=0):
        s = '<table>'
        for c in self.__travel.getTravelRouteCodes(code):
            s += '<tr><td>%s</td><td><a href = delroute?code=%s&acode=%s>%s</td></tr>' % (
                self.__travel.getRoute(c).getCountry(), str(code), str(c), u'удалить')
        s += '</table>'
        return s

    def travelform(self, code=0, add=True):
        date, quantity, discount = '', 0, 0
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s' % code
        if code in self.__travel.getTravelCodes():
            date = self.__travel.getTravel(code).getDate()
            quantity = self.__travel.getTravel(code).getQuantity()
            discount = self.__travel.getTravel(code).getDiscount()
        s = ''' <form action = %s method = post>
                <table>
                    <tr><td>%s</td><td><input type = text name = date value ='%s'></td></tr>
                    <tr><td>%s</td><td><input type = number name = quantity value = %s></td></tr>
                    <tr><td>%s</td><td><input type = number name = discount value = %s></td></tr>
                    <tr><td><input type = submit></td><td></td></tr>
                </table>
                </form>''' % (a, u'дата', date, u'количество', quantity, u'скидка', discount)
        return s

    def addaction(self, date, quantity, discount):
        code = self.__travel.getTravelNewCode()
        self.__travel.createTravel(code, date, quantity, discount)
        return 'Путевка добавлена<br><a href = index>назад</a>'

    addaction.exposed = True

    def addform(self):
        s = u'Добавить новую путевку<br>'
        s += self.travelform(0)
        return s

    addform.exposed = True

    def editform(self, code):
        s = u'Редактировать путевку<br>'
        s += self.travelform(int(code), False)
        s += ''' %s
                <form action=addclient?code=%s method=post>
                <table>
                <tr><td>%s</td><td><input type=submit value=%s></td>
                </tabe>
                </form>
        ''' % (u'клиенты', str(code), self.clientCombo(int(code)), u'добавить')
        s += self.clientList(int(code))
        s += ''' %s
                <form action=addroute?code=%s method=post>
                <table>
                <tr><td>%s</td><td><input type=submit value=%s></td>
                </tabe>
                </form>
        ''' % (u'маршруты', str(code), self.routeCombo(int(code)), u'добавить')
        s += self.routetList(int(code))
        return s

    editform.exposed = True

    def editaction(self, code, date, quantity, discount):
        self.__travel.getTravel(int(code)).setDate(date)
        self.__travel.getTravel(int(code)).setQuantity(quantity)
        self.__travel.getTravel(int(code)).setDiscount(discount)
        return 'Путевка изменена<br><a href = index>назад</a>'

    editaction.exposed = True

    def addclient(self, code, client):
        self.__travel.getTravel(int(code)).appendClient(self.__travel.findClientByCode(int(client)))
        return '%s<br><a href=editform?code=%s>%s</a>' % (u'Клиент добавлен', code, u'назад')

    addclient.exposed = True

    def addroute(self, code, route):
        self.__travel.getTravel(int(code)).appendRoute(self.__travel.findRouteByCode(int(route)))
        return '%s<br><a href=editform?code=%s>%s</a>' % (u'Маршрут добавлен', code, u'назад')

    addroute.exposed = True

    def delclient(self, code, acode):
        self.__travel.getTravel(int(code)).removeClient(int(acode))
        return '%s<br><a href = editform?code=%s>%s</a>' % (u'Клиент удален', str(code), u'назад')

    delclient.exposed = True

    def delroute(self, code, acode):
        self.__travel.getTravel(int(code)).removeRoute(int(acode))
        return '%s<br><a href = editform?code=%s>%s</a>' % (u'Маршрут удален', str(code), u'назад')

    delroute.exposed = True

    def delr(self, code):
        self.__travel.removeTravel(int(code))
        return 'Путевка удалена<br><a href = index>назад</a>'

    delr.exposed = True

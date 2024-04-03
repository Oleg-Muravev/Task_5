class clientpage:
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
             % (u'Фамилия', u'Имя', u'Отчество', u'Адрес', u'Телефон')
        r = 1
        bg = ''
        for c in self.__travel.getClientCodes():
            s += '<tr%s><td>%d</td>' % (bg, r)
            s += '<td>%s</td>' % self.__travel.getClient(c).getSurname()
            s += '<td>%s</td>' % self.__travel.getClient(c).getName()
            s += '<td>%s</td>' % self.__travel.getClient(c).getMiddlename()
            s += '<td>%s</td>' % self.__travel.getClient(c).getAddress()
            s += '<td>%s</td>' % self.__travel.getClient(c).getPhone()
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

    def clientform(self, code=0, add=True):
        surname, name, middlename, address, phone = '', '', '', '', ''
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s' % code
        if code in self.__travel.getClientCodes():
            surname = self.__travel.getClient(code).getSurname()
            name = self.__travel.getClient(code).getName()
            middlename = self.__travel.getClient(code).getMiddlename()
            address = self.__travel.getClient(code).getAddress()
            phone = self.__travel.getClient(code).getPhone()
        s = '''
            <form action=%s method=post>
            <table>
                <tr><td>%s</td><td><input type=text name=surname value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=name value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=middlename value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=address value=%s></td></tr>
                <tr><td>%s</td><td><input type=text name=phone value=%s></td></tr>
                <tr><td><input type=submit></td><td></td></tr>
            </table>
            </form>''' % (
            a, u'Фамилия', surname, u'Имя', name, u'Отчество', middlename, u'Адрес', address, u'Телефон', phone)

        return s

    def addaction(self, surname, name, middlename, address, phone):
        code = self.__travel.getClientNewCode()
        self.__travel.createClient(code, surname, name, middlename, address, phone)
        return 'Клиент добавлен<br><a href = index>назад</a>'

    addaction.exposed = True

    def addform(self):
        s = u'Добавить клиента'
        s += self.clientform(0)
        return s

    addform.exposed = True

    def editform(self, code):
        s = u'Редактировать клиента<br>'
        s += self.clientform(int(code), False)
        return s

    editform.exposed = True

    def editaction(self, code, surname, name, middlename, address, phone):
        self.__travel.getClient(int(code)).setSurname(surname)
        self.__travel.getClient(int(code)).setName(name)
        self.__travel.getClient(int(code)).setMiddlename(middlename)
        self.__travel.getClient(int(code)).setAddress(address)
        self.__travel.getClient(int(code)).setPhone(phone)
        return 'Клиент изменен<br><a href=index>Назад</a>'

    editaction.exposed = True

    def delr(self, code):
        self.__travel.removeClient(int(code))
        return "Клиент удален<br><a href=index>Назад</a>"

    delr.exposed = True
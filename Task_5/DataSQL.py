import os
import sqlite3 as db
from Data import Data
emptydb = """
    PRAGMA foreign_keys = ON;
    create table client
    (code integer primary key,
    surname text,
    name text,
    middlename text,
    address text,
    phone text);
    create table routes
    (code integer primary key,
    country text,
    climate text,
    duration integer,
    hotel text,
    cost integer);
    create table package
    (code integer primary key,
    date text,
    quantity integer,
    discount integer);
    create table package_client_route
    (code integer primary key autoincrement,
    package integer references package(code) on update cascade on delete cascade,
    client integer references client(code) on update cascade on delete cascade,
    routes integer references routes(code) on update cascade on delete cascade,
    unique(package, client, routes));
"""
class DataSQL(Data):
    def read(self):
        conn = db.connect(self.getInp())
        curs = conn.cursor()
        curs.execute('select code, surname, name, middlename, address, phone from client')
        data = curs.fetchall()
        for r in data:
            self.getData().createClient(r[0], r[1], r[2], r[3], r[4], r[5])
        curs.execute('select code, country, climate, duration, hotel, cost from routes')
        data = curs.fetchall()
        for r in data:
            self.getData().createRoute(r[0], r[1], r[2], r[3], r[4], r[5])
        curs.execute('select code, date, quantity, discount from package')
        data = curs.fetchall()
        for r in data:
            self.getData().createTravel(r[0], r[1], r[2], r[3])
        curs.execute('select package, client, routes from package_client_route')
        data = curs.fetchall()
        for r in data:
            if r[1] != None:
                self.getData().getTravel(r[0]).appendClient(self.getData().getClient(r[1]))
            if r[2] != None:
                self.getData().getTravel(r[0]).appendRoute(self.getData().getRoute(r[2]))
        conn.close()
        
    def write(self):
        conn = db.connect(self.getOut())
        curs = conn.cursor()
        curs.executescript(emptydb)
        for c in self.getData().getClientList():
            curs.execute("insert into client(code, surname, name, middlename, address, phone) values('%s','%s','%s','%s','%s','%s')"%(c.getCode(), c.getSurname(), c.getName(),c.getMiddlename(), c.getAddress(), c.getPhone()))
        for s in self.getData().getRouteList():
            curs.execute("insert into routes(code, country, climate, duration, hotel, cost) values('%s','%s','%s','%s','%s','%s')"%(s.getCode(), s.getCountry(), s.getClimate(), s.getDuration(), s.getHotel(), s.getCost()))
        for i in self.getData().getTravelList():
            curs.execute("insert into package(code, date, quantity, discount) values('%s','%s','%s','%s')"%(i.getCode(), i.getDate(), i.getQuantity(), i.getDiscount()))
            for cl in i.getClient().getItems():
                curs.execute("insert into package_client_route(package, client) values('%s', '%s')"%(i.getCode(), cl.getCode()))
            for rt in i.getRoute().getItems():
                curs.execute("insert into package_client_route(package, routes) values('%s', '%s')"%(i.getCode(), rt.getCode()))
        conn.commit()
        conn.close()

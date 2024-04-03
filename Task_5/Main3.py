from TravelCompany import TravelCompany
from DataSQL import DataSQL
from DataXML import DataXML
import os

t1 = TravelCompany()
t2 = TravelCompany()

xml1 = DataXML(t1, 'old.xml', 'new.xml')
xml2 = DataXML(t2, 'old.xml', 'new.xml')
sql1 = DataSQL(t1, 'new.sqlite', 'new.sqlite')
sql2 = DataSQL(t2, 'new.sqlite', 'new.sqlite')

xml1.read()
if os.path.isfile(sql1.getOut()):
    os.remove(sql1.getOut())
sql1.write()
sql2.read()
xml2.write()

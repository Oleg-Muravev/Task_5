import cherrypy
import sys

sys.path.insert(0, "./travel")
from TravelCompany import TravelCompany
from DataXML import DataXML
from Clientpage import clientpage
from Routepage import routepage
from Travelpage import travelpage


class start:
    def __init__(self):
        self.__travel = TravelCompany()

        self.__dataxml = DataXML(self.__travel)
        self.__dataxml.readFile('old.xml')
        self.clientpage = clientpage(self.__travel)
        self.routepage = routepage(self.__travel)
        self.travelpage = travelpage(self.__travel)

    def index(self):
        return """
            <a href=clientpage\>клиенты</a><br>
            <a href=routepage\>маршуты</a><br>
            <a href=travelpage\>путевки</a><br>
        """

    index.exposed = True


root = start()
cherrypy.config.update({
    'log.screen': True,
    "server.socket_port": 8000
})
cherrypy.tree.mount(root)

if __name__ == '__main__':
    cherrypy.engine.start()
    cherrypy.engine.block()

from dbListWidget import dbListWidget


class clientListWidget(dbListWidget):
    def update(self):
        self.clear()
        for a in self.getTravel().getTravelClientCodes(self.getCurrentRec()):
            self.addItem(a, self.getTravel().getClient(a).getSurname())
        if self.getTravel().getTravelClientCodes(self.getCurrentRec()):
            self.setCurrentRow(0)


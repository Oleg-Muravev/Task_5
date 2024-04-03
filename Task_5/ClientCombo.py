from dbComboBox import dbComboBox


class clientCombo(dbComboBox):
    def update(self):
        self.clear()
        for a in self.getTravel().getClientCodes():
            if not (a in self.getTravel().getTravelClientCodes(self.getCurrentRec())):
                self.addItem(a, self.getTravel().getClient(a).getSurname())


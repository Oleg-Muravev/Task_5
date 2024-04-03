from dbComboBox import dbComboBox


class routeCombo(dbComboBox):
    def update(self):
        self.clear()
        for a in self.getTravel().getRouteCodes():
            if not (a in self.getTravel().getTravelRouteCodes(self.getCurrentRec())):
                self.addItem(a, self.getTravel().getRoute(a).getCountry())


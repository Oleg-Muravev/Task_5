from dbListWidget import dbListWidget


class routeListWidget(dbListWidget):
    def update(self):
        self.clear()
        for a in self.getTravel().getTravelRouteCodes(self.getCurrentRec()):
            self.addItem(a, self.getTravel().getRoute(a).getCountry())
        if self.getTravel().getTravelRouteCodes(self.getCurrentRec()):
            self.setCurrentRow(0)


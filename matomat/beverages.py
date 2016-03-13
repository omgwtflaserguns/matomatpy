import npyscreen

class BeverageList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(BeverageList, self).__init__(*args, **keywords)

    def display_value(self, vl):
        return "%s - %s" % (vl["name"], vl["price"])

class BeverageListDisplay (npyscreen.FormMutt):

    MAIN_WIDGET_CLASS = BeverageList

    def beforeEditing(self):
        self.update_list()

    def update_list(self):
        self.wMain.values = list(self.parentApp.beverage.find())
        self.wMain.display()

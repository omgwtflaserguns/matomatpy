import npyscreen
import constants


class BeverageList(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(BeverageList, self).__init__(*args, **keywords)

    def display_value(self, vl):
        return "%s - %s" % (vl["name"], vl["price"])


class BeverageListDisplay (npyscreen.FormMutt):

    MAIN_WIDGET_CLASS = BeverageList

    def __init__(self, *args, **keywords):
        super(BeverageListDisplay, self).__init__(*args, **keywords)
        self.add_handlers({
            "q": self.when_quit
        })

    def when_quit(self, *args, **keywords):
        self.parentApp.switchForm(constants.Forms.MENU_FORM)

    def beforeEditing(self):
        self.update_list()
        self.wStatus1.value = 'Manage Beverages'
        self.wStatus2.value = 'Press q to return to the menu'

    def update_list(self):
        self.wMain.values = list(self.parentApp.db.connection.Beverage.find())
        self.wMain.display()

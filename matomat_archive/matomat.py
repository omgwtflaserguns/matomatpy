class Matomat(npyscreen.NPSAppManaged):

    def __init__(self, *args, **keywords):
        super(Matomat, self).__init__(*args, **keywords)
        self.config = config.Config()
        self.db = None

    def initialize(self):
        self.db = db.db(self.config.options.get(constants.Options.MONGODB_URI).value)

    def register_forms(self):
        self.addForm(constants.Forms.LOGIN_FORM, login.LoginDisplay)
        self.addForm(constants.Forms.MENU_FORM, menu.MenuDisplay)
        self.addForm(constants.Forms.BEVERAGE_FORM, beverages.BeverageListDisplay)
        self.addForm(constants.Forms.CONFIG_FORM, options.OptionsDisplay)

        if(self.config.read_config()):
            self.addForm(constants.Forms.MAIN_FORM, login.LoginDisplay)
            self.initialize()
        else:
            self.addForm(constants.Forms.MAIN_FORM, options.OptionsDisplay)

    def onStart(self):
        self.register_forms()

def main():
    matomat = Matomat()
    matomat.run()

if __name__ == '__main__':
    main()

import npyscreen
import constants
import pyfiglet
import db

class MenuDisplay (npyscreen.Form):

    def __init__(self, *args, **keywords):
        super(MenuDisplay, self).__init__(*args, **keywords)
        self.add_handlers({
            "q": self.when_quit
        })

    def register_widgets(self):
        figlet = pyfiglet.Figlet()
        header = figlet.renderText("Menu")

        self.wgHeader = self.add_widget(npyscreen.MultiLineEdit, value=header, editable=False)
        self.wgFooter = self.add_widget(npyscreen.MultiLineEdit, value='q to quit', editable=False, rely=-3)
        self.wgBuy = self.add_widget(npyscreen.TitleSelectOne, name='Buy', rely=10)

    def create(self):
        self.register_widgets()
        beverages = db.connection.Beverage.find()
        self.wgBuy.values = ["%s - %s" % (bev["price"], bev["name"]) for bev in beverages]

    def when_quit(self, *args, **keywords):
        self.parentApp.current_user = ''
        self.parentApp.switchForm(constants.Forms.LOGIN_FORM)

    def beforeEditing(self):
        self.update_list()

    def update_list(self):
        # TODO evaluate rights and fill menu accordingly
        if not self.parentApp.current_user:
            self.parentApp.switchForm(constants.Forms.LOGIN_FORM)


import npyscreen
import pyfiglet
import constants
import db


class LoginDisplay (npyscreen.Form):

    def reset_form(self):
        self.wgUser.value = ''
        self.wgPass.value = ''

    def add_header(self):
        figlet = pyfiglet.Figlet()
        header = figlet.renderText("Matomat")

        self.add_widget(npyscreen.MultiLineEdit, value=header, editable=False)

    def register_widgets(self):
        self.add_header()

        self.wgUser = self.add_widget(npyscreen.TitleText, name='User:', max_height=1, rely=-5)
        self.wgPass = self.add_widget(npyscreen.TitlePassword, name='Password:', max_height=1, rely=-3)

    def create(self):
        self.register_widgets()

    def beforeEditing(self):
        self.reset_form()

    def afterEditing(self):

        # TODO: Login Logic here
        user = db.connection.User.one({'username': self.wgUser.value, 'password': self.wgPass.value})

        if user:
            self.parentApp.current_user = user
            self.parentApp.switchForm(constants.Forms.MENU_FORM)
        else:
            npyscreen.notify_confirm('Wrong Username or Password', 'Login incorrect')


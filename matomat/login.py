import npyscreen
import pyfiglet

class LoginDisplay (npyscreen.Form):

    def addHeader(self):
        figlet = pyfiglet.Figlet()
        header = figlet.renderText("Matomat")

        self.add_widget(npyscreen.MultiLineEdit, value=header, editable=False)

    def create(self):
        self.addHeader()

        self.wgUser = self.add_widget(npyscreen.TitleText, name='User:', max_height=1, rely=-5)
        self.wgPass = self.add_widget(npyscreen.TitlePassword, name='Password:', max_height=1, rely=-3)

    def beforeEditing(self):
        self.wgUser.value = ''
        self.wgPass.value = ''

    def afterEditing(self):

        # TODO: Login Logic here
        user = self.parentApp.user.one({'username': self.wgUser.value, 'password': self.wgPass.value})

        if user:
            self.parentApp.currentUser = user
            self.parentApp.switchForm("MENU")
        else:
            npyscreen.notify_confirm('Wrong Username or Password', 'Login incorrect')


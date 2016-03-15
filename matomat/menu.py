import npyscreen
import constants

class MenuDisplay (npyscreen.FormMutt):

    def __init__(self, *args, **keywords):
        super(MenuDisplay, self).__init__(*args, **keywords)
        self.add_handlers({
            "q": self.when_quit
        })

    def when_quit(self, *args, **keywords):
        self.parentApp.current_user = ''
        self.parentApp.switchForm(constants.Forms.LOGIN_FORM)

    def beforeEditing(self):
        self.update_list()
        self.wStatus1.value = 'Matomat'
        self.wStatus2.value = 'Logged in as ' + str(self.parentApp.current_user['username']) + ' - press q to quit'

    def update_list(self):
        # TODO evaluate rights and fill menu accordingly

        if not self.parentApp.current_user:
            self.parentApp.switchForm(constants.Forms.LOGIN_FORM)

        self.wMain.values = ["", "Mate", "see todo"]
        self.wMain.display()
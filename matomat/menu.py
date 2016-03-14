import npyscreen

class MenuDisplay (npyscreen.FormMutt):

    def __init__(self, *args, **keywords):
        super(MenuDisplay, self).__init__(*args, **keywords)
        self.add_handlers({
            "q": self.when_quit
        })

    def when_quit(self, *args, **keywords):
        self.parentApp.currentUser = ''
        self.parentApp.switchForm("MAIN")

    def beforeEditing(self):
        self.update_list()
        self.wStatus1.value = 'Matomat'
        self.wStatus2.value = 'Logged in as ' + str(self.parentApp.currentUser['username']) + ' - press q to quit'

    def update_list(self):
        # TODO evaluate rights and fill menu accordingly
        self.wMain.values = ["Beer", "Mate", "see todo"]
        self.wMain.display()
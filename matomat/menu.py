# -*- coding: utf-8 -*-
import npyscreen
import constants
import db

class MenuList (npyscreen.MultiLineAction):

    def actionHighlighted(self, act_on_this, key_press):
        npyscreen.notify_confirm('Chosen: ' + str(act_on_this), '')

class MenuDisplay (npyscreen.FormMutt):

    MAIN_WIDGET_CLASS = MenuList
    MAIN_WIDGET_CLASS_START_LINE = 3

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

    def update_list(self):
        # TODO evaluate rights and fill menu accordingly
        if not self.parentApp.current_user:
            self.parentApp.switchForm(constants.Forms.LOGIN_FORM)

        self.wStatus1.value = "Logged on as %s" % (self.parentApp.current_user["username"])
        self.wStatus2.value = "Press q to Logout"

        beverages = db.connection.Beverage.find()
        self.wMain.values = ["-- BUY"]
        self.wMain.values += ["%s for %s" % (bev["name"], bev["price"]) for bev in beverages]
        self.wMain.values += ["", "--META"]
        self.wMain.values += ["Manage beverages", "Manage accounts", "Open fridge", "Show stats", "Deposit credits", "Show History", "Change Password"]


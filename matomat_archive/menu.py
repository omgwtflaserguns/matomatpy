# -*- coding: utf-8 -*-
import npyscreen
import constants
import permissions


class MenuList (npyscreen.MultiLineAction):

    def display_value(self, vl):
        return vl.name

    def actionHighlighted(self, act_on_this, key_press):
        if act_on_this.on_select:
            act_on_this.on_select()


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
        self.fill_form()

    def fill_form(self):
        if not self.parentApp.current_user:
            self.parentApp.switchForm(constants.Forms.LOGIN_FORM)

        self.wMain.values = []
        self.fill_status()
        self.fill_menu()

    def fill_status(self):
        self.wStatus1.value = "Logged on as %s" % (self.parentApp.current_user["username"])
        self.wStatus2.value = "Press q to Logout"

    def fill_menu(self):
        rights = self.parentApp.current_user['rights']

        if permissions.Permissions.RIGHT_BUY_BEVERAGE.key in rights:
            self.fill_beverages()
            self.add_menu_entry("", None)

        self.add_menu_entry("-- META", None)

        if permissions.Permissions.RIGHT_MANAGE_BEVERAGES.key in rights:
            self.add_menu_entry(permissions.Permissions.RIGHT_MANAGE_BEVERAGES.name, lambda: self.parentApp.switchForm(constants.Forms.BEVERAGE_FORM))

    def fill_beverages(self):
        beverages = self.parentApp.db.connection.Beverage.find()
        self.add_menu_entry("-- BUY", None)

        for bev in beverages:
            self.add_menu_entry("%s for %s" % (bev["name"], bev["price"]), None)

    def add_menu_entry(self, name, on_select):
        self.wMain.values += [MenuItem(name, on_select)]


class MenuItem:

    def __init__(self, name, on_select):
        self.name = name
        self.on_select = on_select

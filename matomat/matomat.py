import npyscreen
import beverages
import login
import menu
import constants

'''
    def insert_beverage(self):
        Beverage = db.connection.Beverage()
        Beverage["name"] = unicode("BIER")
        Beverage["price"] = 1.0
        Beverage.save()

    def insert_user(self):
        User = db.connection.User()
        User["username"] = unicode("muchwow")
        User["password"] = unicode("suchpass")
        User["rights"] = ["not", "yet", "implemented"]
        User.save()
'''


class Matomat(npyscreen.NPSAppManaged):

    def register_forms(self):
        self.addForm(constants.Forms.LOGIN_FORM, login.LoginDisplay)
        self.addForm(constants.Forms.MENU_FORM, menu.MenuDisplay)
        self.addForm(constants.Forms.BEVERAGE_FORM, beverages.BeverageListDisplay)

    def onStart(self):
        self.register_forms()


def main():
    matomat = Matomat()
    matomat.run()

if __name__ == '__main__':
    main()

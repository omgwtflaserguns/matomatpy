import npyscreen
import db
import beverages
import login
import menu

class Matomat(npyscreen.NPSAppManaged):

    def insertBeverage(self):
        Beverage = db.connection.Beverage()
        Beverage["name"] = unicode("BIER")
        Beverage["price"] = 1.0
        Beverage.save()

    def insertUser(self):
        User = db.connection.User()
        User["username"] = unicode("muchwow")
        User["password"] = unicode("suchpass")
        User["rights"] = ["not", "yet", "implemented"]
        User.save()

    def onStart(self):
        self.beverage = db.connection.Beverage
        self.user = db.connection.User

        self.addForm("MAIN", login.LoginDisplay)
        self.addForm("MENU", menu.MenuDisplay)
        self.addForm("BEVERAGES", beverages.BeverageListDisplay)

def main():
    matomat = Matomat()
    matomat.run()

if __name__ == '__main__':
    main()

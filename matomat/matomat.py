import npyscreen
import db
import beverages

class Matomat(npyscreen.NPSAppManaged):

    def insertBeverage(self):
        Beverage = db.connection.Beverage()
        Beverage["name"] = unicode("BIER")
        Beverage["price"] = 1.0
        Beverage.save()

    def onStart(self):
        self.beverage = db.connection.Beverage
        self.addForm("MAIN", beverages.BeverageListDisplay)

def main():
    matomat = Matomat()
    matomat.run()

if __name__ == '__main__':
    main()

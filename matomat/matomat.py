import curses
import pyfiglet
import db

figlet = pyfiglet.Figlet()

def initialize(window):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    window.clear()

def showLogin(window):
    window.clear()
    window.addstr(3, 0, figlet.renderText('Matomat'), curses.color_pair(1))
    window.addstr(curses.LINES - 5, 5, 'Login:')
    curses.setsyx(curses.LINES - 5, 12)
    window.refresh()
    curses.echo(1)
    login = window.getstr()
    curses.echo(0)
    window.clear()
    window.addstr(3, 0, figlet.renderText('Matomat'), curses.color_pair(1))
    window.addstr(curses.LINES - 5, 5, 'Password:')
    curses.setsyx(curses.LINES - 5, 12)
    window.refresh()
    password = window.getstr()
    return login, password

def showMenu(window):
    window.clear()
    window.addstr(3, 0, figlet.renderText('Menu'), curses.color_pair(1))
    window.addstr(12, 5, 'Buy Beer')
    window.addstr(13, 5, 'Buy Mate')
    window.addstr(14, 5, 'Etc')
    window.getch()

def showBeverage(window):
    Beverage = db.Beverage()
    window.clear()

    Beverage["name"] = "BIER"
    Beverage["price"] = 1
    Beverage.save()
    c = 5
    for beverage in Beverage.find({}):
        c += 1
        window.addstr(c, 5, beverage["name"])
    c = 5
    window.getch()
    return True


def matomat(window):

    initialize(window)


    while True:
        user, password = showLogin(window)

        if user == '':
            break;
        else:
            showBeverage(window)
            showMenu(window)

def main():
    curses.wrapper(matomat)

if __name__ == '__main__':
    main()

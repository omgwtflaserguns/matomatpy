import pyfiglet
import curses
from matomat.ui.form import FormBase
from matomat.models.point import Point


class MenuForm (FormBase):

    HEADER_POSITION = Point(3, 3)
    MENU_POSITION = Point(10, 5)

    def __init__(self, colors):
        self.figlet = pyfiglet.Figlet()
        self.colors = colors
        self.menuitems = None
        self.currentItem = 0

    def set_items(self, menu_items):
        self.menuitems = menu_items

    def _draw_header(self, screen):
        y = MenuForm.HEADER_POSITION.y
        for line in self.figlet.renderText('Matomat').splitlines():
            screen.addstr(y, MenuForm.HEADER_POSITION.x, line, self.colors.color_header())
            y += 1

    def _draw_menu(self, screen):
        y = MenuForm.MENU_POSITION.y
        index = 0
        for item in self.menuitems:
            if index == self.currentItem:
                screen.addstr(y, MenuForm.MENU_POSITION.x, item.title, curses.A_STANDOUT)
            else:
                screen.addstr(y, MenuForm.MENU_POSITION.x, item.title)
            y += 1
            index += 1

    def list_up(self):
        if self.currentItem == 0:
            self.currentItem = len(self.menuitems) - 1
        else:
            self.currentItem -= 1

    def list_down(self):
        if self.menuitems:
            if self.currentItem == len(self.menuitems) - 1:
                self.currentItem = 0
            else:
                self.currentItem += 1

    def show(self, screen):
        self.currentItem = 0

        while True:
            screen.clear()
            curses.curs_set(0)
            self._draw_header(screen)
            self._draw_menu(screen)
            key = screen.getch()

            if key == curses.KEY_ENTER:
                return self.menuitems[self.currentItem]
            elif key == ord('q'):
                return None
            elif key == curses.KEY_DOWN:
                self.list_down()
            elif key == curses.KEY_UP:
                self.list_up()










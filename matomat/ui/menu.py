import curses
import logging
from matomat.ui.form import FormBase
from matomat.models.point import Point


class MenuForm (FormBase):

    HEADER_POSITION = Point(3, 3)
    MENU_POSITION = Point(10, 5)

    def __init__(self, colors, figlet):
        self.figlet = figlet
        self.colors = colors
        self.menuitems = None
        self.currentItem = 0

    def set_items(self, menu_items):
        """sets the Menu to display by the show method"""
        self.menuitems = menu_items

    def show(self, screen):
        """Displays the Menu given with set_items, returns the key of the selected item"""
        self.currentItem = 0

        while True:
            screen.clear()
            curses.curs_set(0)
            self._draw_header(screen)
            self._draw_menu(screen)
            key = screen.getch()

            if key == curses.KEY_ENTER or key == 10:
                return self.menuitems[self.currentItem].key
            elif key == ord('q'):
                return None
            elif key == curses.KEY_DOWN:
                self._list_down()
            elif key == curses.KEY_UP:
                self._list_up()

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
                screen.addstr(y, MenuForm.MENU_POSITION.x, item.title, self.colors.color_selected_menu_entry())
            else:
                screen.addstr(y, MenuForm.MENU_POSITION.x, item.title)
            y += 1
            index += 1

    def _list_up(self):
        if self.currentItem == 0:
            self.currentItem = len(self.menuitems) - 1
        else:
            self.currentItem -= 1

    def _list_down(self):
        if self.menuitems:
            if self.currentItem == len(self.menuitems) - 1:
                self.currentItem = 0
            else:
                self.currentItem += 1












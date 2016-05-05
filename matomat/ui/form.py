import abc
import curses
from matomat.models.point import Point


class FormBase(object):
    __metaclass__ = abc.ABCMeta

    HEADER_POSITION = Point(3, 3)
    MENU_POSITION = Point(10, 5)
    INPUT_POSITION = Point(10, 5)

    menuitems = None
    currentItem = 0

    def __init__(self, figlet, colors):
        self.figlet = figlet
        self.colors = colors

    def _read_string_noecho(self, screen, point):
        curses.curs_set(1)
        value = screen.getstr(point.y, point.x).decode('utf-8')
        curses.curs_set(0)
        return value


    def _read_string(self, screen, point):
        curses.echo()
        result = self._read_string_noecho(screen, point)
        curses.noecho()
        return result

    def _read_float(self, screen, point):
        while True:
            try:
                return float(self._read_string(screen, point))
            except ValueError:
                continue

    def set_items(self, menu_items):
        """sets the Menu to display by the show method"""
        self.menuitems = menu_items

    def get_menu_input(self, screen):
        while True:
            curses.curs_set(0)

            self._draw_menu(screen)
            key = screen.getch()

            if key == curses.KEY_ENTER or key == 10:
                return self.menuitems[self.currentItem]
            elif key == ord('q'):
                return None
            elif key == curses.KEY_DOWN:
                self._list_down()
            elif key == curses.KEY_UP:
                self._list_up()

    def _draw_header(self, screen, text):
        y = self.HEADER_POSITION.y
        for line in self.figlet.renderText(text).splitlines():
            screen.addstr(y, self.HEADER_POSITION.x, line, self.colors.color_header())
            y += 1

    def _draw_menu(self, screen):
        y = self.MENU_POSITION.y
        index = 0
        for item in self.menuitems:
            if index == self.currentItem:
                screen.addstr(y, self.MENU_POSITION.x, item.title, self.colors.color_selected_menu_entry())
            else:
                screen.addstr(y, self.MENU_POSITION.x, item.title)
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

    @abc.abstractmethod
    def show(self, screen):
        return

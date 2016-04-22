import curses
import logging
from matomat.ui.form import FormBase
from matomat.models.point import Point


class MenuForm (FormBase):

    HEADER_POSITION = Point(3, 3)

    def __init__(self, figlet, colors):
        super().__init__(figlet, colors)

    def show(self, screen):
        """Displays the Menu given with set_items, returns the key of the selected item"""

        screen.clear()
        self._draw_header(screen, 'Menu')
        return FormBase.get_menu_input(self, screen).key















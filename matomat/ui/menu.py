import curses
import logging
from matomat.ui.form import FormBase
from matomat.models.point import Point


class MenuForm (FormBase):

    HEADER_POSITION = Point(3, 3)

    def __init__(self, colors, figlet):
        self.figlet = figlet
        self.colors = colors
        self.menuitems = None
        self.currentItem = 0

    def show(self, screen):
        """Displays the Menu given with set_items, returns the key of the selected item"""

        screen.clear()
        self._draw_header(screen)
        return FormBase.get_menu_input(self, screen)

    def _draw_header(self, screen):
        y = MenuForm.HEADER_POSITION.y
        for line in self.figlet.renderText('Matomat').splitlines():
            screen.addstr(y, MenuForm.HEADER_POSITION.x, line, self.colors.color_header())
            y += 1














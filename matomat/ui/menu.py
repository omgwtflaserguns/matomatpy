import pyfiglet
from .form import FormBase
from ..models.point import Point


class MenuForm (FormBase):

    HEADER_POSITION = Point(3, 3)
    MENU_POSITION = Point(10, 5)

    def __init__(self, colors):
        self.figlet = pyfiglet.Figlet()
        self.colors = colors
        self.menuitems = None

    def set_items(self, menu_items):
        self.menuitems = menu_items

    def _draw_header(self, screen):
        y = MenuForm.HEADER_POSITION.y
        for line in self.figlet.renderText('Matomat').splitlines():
            screen.addstr(y, MenuForm.HEADER_POSITION.x, line, self.colors.color_header())
            y += 1

    def _draw_menu(self, screen):
        y = MenuForm.MENU_POSITION.y
        for item in self.menuitems:
            screen.addstr(y, MenuForm.MENU_POSITION.x, item.title)
            y += 1

    def show(self, screen):
        screen.clear()
        self._draw_header(screen)
        self._draw_menu(screen)
        screen.getch()









from matomat.ui.form import FormBase
from matomat.models.point import Point
from matomat.models.menu import MenuEntry, MenuKey


class BeveragesForm(FormBase):

    HEADER_POSITION = Point(3, 3)

    def __init__(self, colors, figlet, db):
        self.figlet = figlet
        self.colors = colors
        self.db = db
        self.set_items(self._create_menu())

    def _create_menu(self):
        menu = [MenuEntry(MenuKey.add, 'New')]

        for beverage in self.db.beverages.find():
            name = beverage['name']
            id = beverage['_id']
            menu.append(MenuEntry(id, 'Edit {}'.format(name)))

        menu.append(MenuEntry(MenuKey.quit, 'Exit'))
        return menu

    def _draw_header(self, screen):
        y = BeveragesForm.HEADER_POSITION.y
        for line in self.figlet.renderText('Beverages').splitlines():
            screen.addstr(y, BeveragesForm.HEADER_POSITION.x, line, self.colors.color_header())
            y += 1

    def show(self, screen):
        """Shows the form to manage beverages in the given screen"""

        while True:
            screen.clear()
            self._draw_header(screen)
            selection = FormBase.get_menu_input(self, screen)

            if selection == MenuKey.quit:
                return
            elif selection == MenuKey.add:
                pass



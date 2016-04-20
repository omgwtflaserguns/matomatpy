
import curses
from matomat.ui.form import FormBase
from matomat.models.point import Point
from matomat.models.menu import MenuEntry, MenuKey


class BeveragesListForm(FormBase):

    HEADER_POSITION = Point(3, 3)

    def __init__(self, colors, figlet, db, editform):
        self.figlet = figlet
        self.colors = colors
        self.db = db
        self.editform = editform

    def _create_menu(self):
        menu = [MenuEntry(MenuKey.add, 'New')]

        for beverage in self.db.beverages.find():
            menu.append(MenuEntry(beverage['_id'], 'Edit - {} {:.2}'.format(beverage['name'], beverage['price']), beverage))

        menu.append(MenuEntry(MenuKey.quit, 'Exit'))
        return menu

    def show(self, screen):
        """Shows the form to manage beverages in the given screen"""

        while True:
            screen.clear()
            self._draw_header(screen, 'Beverages')
            self.set_items(self._create_menu())
            selection = FormBase.get_menu_input(self, screen)

            if selection.key == MenuKey.quit:
                return
            elif selection.key == MenuKey.add:
                self.editform.show(screen, {'name': 'New', 'price': None})
            else:
                self.editform.show(screen, selection.item)


class BeverageEditForm(FormBase):

    def __init__(self, colors, figlet, db):
        self.figlet = figlet
        self.colors = colors
        self.db = db

    def _draw_labels(self, screen):
        y = BeverageEditForm.INPUT_POSITION.y
        screen.addstr(y, BeverageEditForm.INPUT_POSITION.x, 'Name:')
        screen.addstr(y + 2, BeverageEditForm.INPUT_POSITION.x, 'Price:')

    def _read_name(self, screen):
        curses.echo()
        return screen.getstr(BeverageEditForm.INPUT_POSITION.y, BeverageEditForm.INPUT_POSITION.x + 8).decode('utf-8')
        curses.noecho()

    def _read_price(self, screen):
        curses.echo()
        while True:
                try:
                    return float(screen.getstr(BeverageEditForm.INPUT_POSITION.y + 2, BeverageEditForm.INPUT_POSITION.x + 8))
                except ValueError:
                    continue
        curses.noecho()

    def show(self, screen, beverage):
        """Shows the form to edit the given beverage in the given screen"""
        screen.clear()
        self._draw_header(screen, 'Edit - {}'.format(beverage['name']))
        self._draw_labels(screen)

        beverage['name'] = self._read_name(screen)
        beverage['price'] = self._read_price(screen)

        if '_id' in beverage:
            self.db.beverages.update({'_id': beverage['_id']}, beverage)
        else:
            self.db.beverages.insert(beverage)







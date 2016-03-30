from matomat.ui.form import FormBase
from matomat.models.point import Point


class LoginForm(FormBase):

    HEADER_POSITION = Point(3, 3)
    INPUT_POSITION = Point(10, 5)

    def __init__(self, figlet):
        self.figlet = figlet

    def _draw_header(self, screen):
        y = LoginForm.HEADER_POSITION.y
        for line in self.figlet.renderText('Login').splitlines():
            screen.addstr(y, LoginForm.HEADER_POSITION.x, line, self.colors.color_header())
            y += 1

    def _draw_labels(self, screen):
        y = LoginForm.INPUT_POSITION.y
        screen.addstr(y, LoginForm.INPUT_POSITION.x, 'User:')
        screen.addstr(y + 3, LoginForm.INPUT_POSITION.x, 'Pass:')

    def show(self, screen):

        # TODO Draw Textboxes and  read the inputs
        return 'muchwow', 'suchpass'

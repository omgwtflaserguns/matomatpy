from matomat.ui.form import FormBase
from matomat.models.point import Point
import curses


class LoginForm(FormBase):

    HEADER_POSITION = Point(3, 3)
    INPUT_POSITION = Point(10, 5)

    def __init__(self, colors, figlet):
        self.figlet = figlet
        self.colors = colors

    def _draw_header(self, screen):
        y = LoginForm.HEADER_POSITION.y
        for line in self.figlet.renderText('Login').splitlines():
            screen.addstr(y, LoginForm.HEADER_POSITION.x, line, self.colors.color_header())
            y += 1

    def _draw_labels(self, screen):
        y = LoginForm.INPUT_POSITION.y
        screen.addstr(y, LoginForm.INPUT_POSITION.x, 'User:')
        screen.addstr(y + 2, LoginForm.INPUT_POSITION.x, 'Pass:')

    def _read_username(self, screen):
        curses.echo()
        return screen.getstr(LoginForm.INPUT_POSITION.y, LoginForm.INPUT_POSITION.x + 8)
        curses.noecho()

    def _read_password(self, screen):
        curses.echo()
        return screen.getstr(LoginForm.INPUT_POSITION.y + 2, LoginForm.INPUT_POSITION.x + 8)
        curses.noecho()

    def show(self, screen):
        """Shows the Login, returns username, password tuple"""
        screen.clear()
        self._draw_header(screen)
        self._draw_labels(screen)

        user = self._read_username(screen).decode('ascii')
        password = self._read_password(screen).decode('ascii')

        return user, password

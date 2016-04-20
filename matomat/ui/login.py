from matomat.ui.form import FormBase
from matomat.models.point import Point
import curses


class LoginForm(FormBase):

    def __init__(self, colors, figlet):
        self.figlet = figlet
        self.colors = colors

    def _draw_labels(self, screen):
        y = LoginForm.INPUT_POSITION.y
        screen.addstr(y, LoginForm.INPUT_POSITION.x, 'User:')
        screen.addstr(y + 2, LoginForm.INPUT_POSITION.x, 'Pass:')

    def _read_username(self, screen):
        curses.echo()
        return screen.getstr(LoginForm.INPUT_POSITION.y, LoginForm.INPUT_POSITION.x + 8).decode('utf-8')
        curses.noecho()

    def _read_password(self, screen):
        curses.echo()
        return screen.getstr(LoginForm.INPUT_POSITION.y + 2, LoginForm.INPUT_POSITION.x + 8).decode('utf-8')
        curses.noecho()

    def show(self, screen):
        """Shows the Login, returns username, password tuple"""
        screen.clear()
        self._draw_header(screen, 'Login')
        self._draw_labels(screen)

        user = self._read_username(screen)
        password = self._read_password(screen)

        return user, password

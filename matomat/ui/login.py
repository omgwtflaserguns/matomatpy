from matomat.ui.form import FormBase
from matomat.models.point import Point


class LoginForm(FormBase):

    def __init__(self, figlet, colors):
        super().__init__(figlet, colors)

    def _draw_labels(self, screen):
        y = LoginForm.INPUT_POSITION.y
        screen.addstr(y, LoginForm.INPUT_POSITION.x, 'User:')
        screen.addstr(y + 2, LoginForm.INPUT_POSITION.x, 'Pass:')

    def show(self, screen):
        """Shows the Login, returns username, password tuple"""
        screen.clear()
        self._draw_header(screen, 'Login')
        self._draw_labels(screen)

        user = self._read_string(screen, Point(LoginForm.INPUT_POSITION.y, LoginForm.INPUT_POSITION.x + 8))
        password = self._read_string_noecho(screen, Point(LoginForm.INPUT_POSITION.y + 2, LoginForm.INPUT_POSITION.x + 8))

        return user, password

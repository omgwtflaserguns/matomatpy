import curses


class Colors(object):

    def register(self):
        """Registers curses color pairs for later usage"""
        # Header
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    def color_header(self):
        """returns the curses color pair intended for header usage"""
        return curses.color_pair(1)

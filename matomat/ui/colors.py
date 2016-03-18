import curses


class Colors(object):

    def register(self):
        # Header
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    def color_header(self):
        return curses.color_pair(1)

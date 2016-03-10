import curses


def main(stdscr):
    stdscr.clear()

    stdscr.addstr("maeh?")
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
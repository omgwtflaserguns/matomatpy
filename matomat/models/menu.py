
from enum import Enum


class MenuKey(Enum):
    buy_beverage = 1
    open_fridge = 2
    manage_beverages = 3

    quit = 101
    add = 102
    delete = 103


class MenuEntry:

    def __init__(self, key, title):
        self.key = key
        self.title = title

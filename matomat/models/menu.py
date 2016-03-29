
from enum import Enum


class MenuKey(Enum):
    quit = 1
    buy_beverage = 2
    open_fridge = 3


class MenuEntry:

    def __init__(self, key, title):
        self.key = key
        self.title = title

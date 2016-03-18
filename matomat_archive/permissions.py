
class Right:
    def __init__(self, key, name):
        self.key = key
        self.name = name


class Permissions:

    RIGHT_BUY_BEVERAGE = Right('bb', 'Buy beverage')
    RIGHT_OPEN_FRIDGE = Right('of', 'Open fridge')
    RIGHT_SHOW_STATS = Right('ss', 'Show Stats')
    RIGHT_DEPOSIT_CREDITS = Right('dc', 'Deposit Credits')
    RIGHT_SHOW_HISTORY = Right('sh', 'Show History')
    RIGHT_CHANGE_PASSWORD = Right('cp', 'Change Password')
    RIGHT_MANAGE_ACCOUNTS = Right('ma', 'Manage Accounts')
    RIGHT_MANAGE_BEVERAGES = Right('mb', 'Manage Beverages')



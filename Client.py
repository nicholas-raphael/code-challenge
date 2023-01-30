#
#
#

from enum import Enum
class Type(Enum):
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'

MULTIPLIER = {
    'DEPOSIT': 1,
    'WITHDRAW': -1
}

class Client:
    def __init__(self, name, balance=0):
        self.balance = balance
        self.name = name

    def get_balance(self):
        return self.balance

    def update_balance(self, type, amount=0):
        if not isinstance(Type[type], Type):
            raise TypeError('Tipo no valido')

        self.balance = self.balance + (amount * MULTIPLIER[type])

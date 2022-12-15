import decimal
from dataclasses import field
from enum import Enum


class Account(Enum):
    USD = 'USD'
    RUB = 'RUB'
    KZT = 'KZT'
    EUR = 'EUR'


class BankAccount:
    name: str
    surname: str
    account: decimal.Decimal
    iin: str
    accounttype: Account
    fullname: str = field(init=False)

    def __init__(self, name: str, surname: str, iin: str, accounttype: Account = None, account: decimal.Decimal = None):
        self.name = name
        self.surname = surname
        self.account = account
        self.iin = iin
        self.accounttype = accounttype

    def __post_init__(self):
        self.fullname = f'{self.name} {self.surname}'

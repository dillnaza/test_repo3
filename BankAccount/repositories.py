import decimal
from typing import List, Optional

from BankAccount.models import BankAccount, Account


class BankAccRepositories:
    Accounts: List[BankAccount] = []

    def create_account(self, name: str, surname: str, iin: str) -> None:
        bankaccount = BankAccount(name=name, surname=surname, iin=iin)
        self.Accounts.append(bankaccount)

    def check_iin(self, iin: str) -> Optional[BankAccount]:
        bankaccount = next(
            (i for i in self.Accounts if iin == i.iin),
            None
        )
        if not bankaccount:
            print('Пользователь с таким ИИН не найден')
            return
        return bankaccount

    def toString(self, iin: str) -> str:
        bankaccount = next(
            (i for i in self.Accounts if iin == i.iin),
            None
        )
        if not bankaccount:
            print('Пользователь с таким ИИН не найден')
            return
        print(f'Имя и фамилия пользователя: {self.fullname}\n '
              f'Остаток на счету: {self.account}')

    def addToBankAccount(self, numeric: float) -> None:
        self.account += numeric

    def substractFromBankAccount(self, numeric: float) -> None:
        if self.account >= numeric:
            self.account -= numeric
        else:
            self.account = 0

    def moneyConversion(sum: float, str1: str) -> None:
        if (str1 == Account.USD):
            sum *= 470
        elif (str1 == Account.EUR):
            sum *= 495
        elif (str1 == Account.RUB):
            sum *= 7
        elif (str1 == Account.KZT):
            sum *= 1

import decimal
from typing import Optional, NamedTuple
from BankAccount.exeptions import IINnotFoundError, IINfound
from BankAccount.models import BankAccount
from BankAccount.interfaces import BankAccRepositoriesInterfaces


class BankAccServices(NamedTuple):
    repositories: BankAccRepositoriesInterfaces

    def create_account(self, name: str, surname: str, iin: str, account: str, accounttype: str) -> None:
        try:
            self.repositories.create_account(name=name, surname=surname, iin=iin, account=account, accounttype=accounttype)
            print(f'Пользователь {name} добавлен')
        except IINfound as e:
            print(e)

    def delete_account(self, iin: str) -> None:
        try:
            self.repositories.toString(iin=iin)
            print(f'Пользователь удален из списка')
        except IINnotFoundError as e:
            print(e)

    def check_iin(self, iin: str) -> Optional[BankAccount]:
        try:
            self.repositories.toString(iin=iin)
        except IINnotFoundError as e:
            print(e)

    def toString(self, iin: str) -> str:
        try:
            self.repositories.toString(iin=iin)
        except IINnotFoundError as e:
            print(e)

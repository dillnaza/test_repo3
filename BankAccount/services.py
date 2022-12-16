import decimal
from typing import Optional, NamedTuple

from BankAccount.models import BankAccount
from BankAccount.interfaces import BankAccRepositoriesInterfaces


class BankAccServices(NamedTuple):
    repositories: BankAccRepositoriesInterfaces

    def create_account(self, name: str, surname: str, iin: str, account:str, accounttype:str) -> None:
        self.repositories.create_account(name=name, surname=surname, iin=iin, account=account, accounttype=accounttype)
        print(f'Пользователь {name} добавлен')

    def delete_account(self, iin:str)->None:
        self.repositories.delete_account(iin=iin)
        print(f'Пользователь удален из списка')

    def check_iin(self, iin: str) -> Optional[BankAccount]:
        return self.repositories.check_iin(iin=iin)

    def toString(self, iin: str) -> str:
        return self.repositories.toString(iin=iin)

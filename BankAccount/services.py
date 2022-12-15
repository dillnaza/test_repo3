import decimal
from typing import Optional, NamedTuple

from BankAccount.models import BankAccount
from BankAccount.interfaces import BankAccRepositoriesInterfaces


class BankAccServices(NamedTuple):
    repositories: BankAccRepositoriesInterfaces

    def create_account(self, name: str, surname: str, iin: str) -> None:
        self.repositories.create_account(name=name, surname=surname, iin=iin)
        print(f'Пользователь {name} добавлен')

    def check_iin(self, iin: str) -> Optional[BankAccount]:
        return self.repositories.check_iin(iin=iin)

    def toString(self, iin: str) -> str:
        return self.repositories.toString(iin=iin)

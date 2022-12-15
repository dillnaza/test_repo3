from typing import  Optional, Protocol

from BankAccount.models import BankAccount


class BankAccRepositoriesInterfaces(Protocol):

    def create_account(self, name: str, surname: str, iin: str) -> None:
        raise NotImplementedError

    def check_iin(self, iin: str) -> Optional[BankAccount]:
        raise NotImplementedError

    def toString(self, iin: str) -> str:
        raise NotImplementedError

    def addToBankAccount(self, numeric: float) -> None:
        raise NotImplementedError

    def substractFromBankAccount(self, numeric: float) -> None:
        raise NotImplementedError

    def moneyConversion(sum: float, str1: str) -> None:
        raise NotImplementedError

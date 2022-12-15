import decimal
from typing import Optional
from BankAccount.models import BankAccount
from BankAccount.repositories import BankAccRepositories
from BankAccount.services import BankAccServices


class BankAccHandlers():
    services: BankAccRepositories

    def __init__(self, services: BankAccServices):
        self.services = services

    def sign_up(self, name: str, surname: str, iin: str) -> None:
        name = name.strip()
        surname = surname.strip()

        if len(iin) != 12:
            print('ИИН номер не может быть больше/меньше 12')
            return
        elif not iin.isdigit():
            print('ИИН номер должен состоять только цифр от 0 до 9')
            return

        iin = iin.strip()
        self.services.create_account(name=name, surname=surname, iin=iin)

    def get_bankacc(self, iin: str) -> Optional[BankAccount]:
        if len(iin) > 12:
            print('ИИН номер не может быть больше 12')
            return
        elif not (iin.isdigit()):
            print('ИИН номер должен состоять только цифр от 0 до 9')
            return

        iin = iin.strip()
        self.services.check_iin(iin=iin)

    def toString(self, iin: str) -> str:
        if len(iin) > 12:
            print('ИИН номер не может быть больше 12')
            return
        elif not (iin.isdigit()):
            print('ИИН номер должен состоять только цифр от 0 до 9')
            return

        iin = iin.strip()
        self.services.toString(iin=iin)

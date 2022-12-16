import sys

from BankAccount.handlers import BankAccHandlers
from BankAccount.repositories import BankAccRepositories
from BankAccount.services import BankAccServices


def init():
    bankAccRepositories = BankAccRepositories()
    bankAccServices = BankAccServices(repositories=bankAccRepositories)
    bankAcchandler = BankAccHandlers(services=bankAccServices)

    while True:
        print('''Введите ваше действие:
               1. Создание пользователя
               2. Изменить данные о пользователя
               3. Показать данные о пользователя
               4. Удалить данные о пользователя
               5. Выйти''')
        command = int(input())
        match command:
            case 1:
                name = input('Введите имя: ')
                surname = input('Введите фамилию: ')
                iin = input('Введите ИИН: ')
                print('''Выберите валюту счета: 
                        1. USD
                        2. RUB
                        3. KZT
                        4. EUR''')
                accounttypenumber = int(input())
                match accounttypenumber:
                    case 1:
                        accounttype = 'USD'
                    case 2:
                        accounttype = 'RUB'
                    case 3:
                        accounttype = 'KZT'
                    case 4:
                        accounttype = 'EUR'

                account = input('Введите остаток в счету: ')
                bankAcchandler.sign_up(name=name, surname=surname, iin=iin, account=account, accounttype=accounttype)

            case 2:
                iin = input('Введите ИИН пользователя:')
                bankAcchandler.get_bankacc(iin=iin)
                print('Что изменить в пользователя: ')
                print('1. Имя')
                print('2. Фамилия')
                print('3. ИИН')
                print('4. Добавление деньги на счет')
                print('5. Удаление деньги со счета')
                print('6. Перевод денег')
                check = input()

                match check:
                    case 1:
                        name = input('Введите новое значение ИМЯ: ')
                    case 2:
                        surname = input('Введите новое значение ФАМИЛИЯ: ')
                    case 3:
                        iin = input('')
                    case 4:
                        add = float(input('Сколько хотите добавить: '))
                        bankAccRepositories.addToBankAccount = add
                    case 5:
                        substract = float(input('Сколько хотите убавить: '))
                        bankAccRepositories.substractFromBankAccount = substract
                    case 6:
                        print('Введите данные другого пользователя: ')

            case 3:
                iin = input('Введите ИИН пользователя: ')
                print(bankAcchandler.toString(iin=iin))

            case 4:
                iin = input('Введите ИИН пользователя: ')
                bankAcchandler.delete_acc(iin)
            case 5:
                sys.exit(0)


if __name__ == '__main__':
    init()

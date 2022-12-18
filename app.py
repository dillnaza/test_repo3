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

                bankAcchandler.sign_up(name=name, surname=surname, iin=iin, account=0, accounttype=accounttype)

            case 2:
                iin = input('Введите ИИН пользователя: ')
                bankAcchandler.get_bankacc(iin=iin)
                print('''Что изменить в пользователя: 
        1. Имя
        2. Фамилия
        3. ИИН
        4. Пополнить баланс
        5. Снять деньги со счета
        6. Добавить новый счет
        7. Удалить счет
        8. Перевод денег''')
                check = input()

                match int(check):
                    case 1:
                        name = input('Введите новое значение ИМЯ: ')
                    case 2:
                        surname = input('Введите новое значение ФАМИЛИЯ: ')
                    case 3:
                        iin = input('Введите новое значение ИИН: ')
                    case 4:
                        print('''Какой счет хотите пополнить: 
        1. USD
        2. RUB
        3. KZT
        4. EUR''')
                        add = float(input())
                        bankAccRepositories.addToBankAccount = add
                    case 5:
                        print('''С какого счета хотите снять деньги: 
        1. USD
        2. RUB
        3. KZT
        4. EUR''')
                        substract = float(input())
                        bankAccRepositories.substractFromBankAccount = substract
                    case 6:
                        iin=input('Введите ИИН пользователя: ')
                    case 7:
                        iin=input('Введите ИИН пользователя: ')
                    case 8:
                        print('''Выберите действие:
        1. Перевод между своими счетами
        2. Перевод на счет другого пользователя''')
                        do=int(input())
                        match do:
                            case 1:
                                ot=input('Выберите от какого счета: ')
                                na=input('Выберите на какой счет: ')
                                count=float(input('Сколько перевести: '))
                            case 2:
                                print('Введите ИИН второго пользователя: ')
                                iin=input()
                                ot=input('Выберите от какого счета: ')
                                print('''Выберите счет другого пользователя: 
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
                        count=float(input('Сколько хотите перевести: '))

            case 3:
                iin = input('Введите ИИН пользователя: ')
                bankAcchandler.toString(iin=iin)
            case 4:
                iin = input('Введите ИИН пользователя: ')
                bankAcchandler.delete_acc(iin)
            case 5:
                sys.exit(0)


if __name__ == '__main__':
    init()

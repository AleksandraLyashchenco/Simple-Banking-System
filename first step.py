import random


def welcome():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    answer = input()
    return answer


answer = welcome()
account = []


class Account:

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0


Account.card_number = 0
Account.pin = 0
Account.balance = 0
all_account = []


def create_account():
    Account.card_number = int('400000' + str(int(random.random() * 1000000000)))
    Account.pin = random.randint(1111, 9999)
    account = [Account.card_number, Account.pin, Account.balance]
    all_account.append(account)
    print(all_account)
    return all_account, account


def look_account():
    print('Enter your card number:')
    card_number = input()
    print('Enter your PIN:')
    pin = input()
    for account in all_account:
        if [card_number, pin] in all_account:
            print(account)
        else:
            print('переписывай')


def exit():
    print('Bye!')


create_account()
look_account()

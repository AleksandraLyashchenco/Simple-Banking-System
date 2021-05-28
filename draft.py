import random

import sqlite3

conn = sqlite3.connect('card.s3db')

cursor = conn.cursor()

cursor.execute('DROP TABLE card')

cursor.execute('CREATE TABLE card ( id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
conn.commit()


print('INSERT INTO card (id, number, pin, balance) VALUES (' + 'str(id)' + ', ' + 'str(account.card_number)' + ', ' + 'str(account.pin)'  + ', ' + 'str(account.balance)' + ');')


def save_account(account):
    insert_into_card = cursor.execute('INSERT INTO card (id, number, pin, balance) VALUES (' + str(id) + ', ' + str(account.card_number) + ', ' + str(account.pin) + ', ' + str(account.balance) + ');')
    return insert_into_card



class Account:
    all_accounts = []

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0


def welcome():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    answer = int(input())
    return answer


answer = welcome()


def create():
    card_number = list('400000' + str(int(random.randint(100000000, 999999999))))
    c = list.copy(card_number)
    for i in range(len(c)):
        old_value = c[i]
        new_value = int(old_value)
        c[i] = new_value
    for index, i in enumerate(c):
        if index % 2 == 0:
            i = i * 2
        c[index] = i
        if c[index] > 9:
            c[index] = c[index] - 9
    a = 0
    if sum(c) % 10 > 0:
        a = abs(10 - (sum(c) % 10))
    card_number.append(a)
    card_number = int("".join(map(str, card_number)))
    pin = random.randint(1111, 9999)
    account = Account(card_number, pin)
    Account.all_accounts.append(account)
    save_account(account)
    print('')
    print('Your card has been created')
    print('Your card number:')
    print(account.card_number)
    print('Your card PIN:')
    print(account.pin)
    print('')


def account_menu():
    print('')
    print('1. Balance')
    print('2. Log out')
    print('0. Exit')
    a = int(input())
    return a


def view_account():
    print('Enter your card number:')
    card_number = int(input())
    print('Enter your PIN:')
    pin = int(input())
    print('')
    for account in Account.all_accounts:
        if card_number == account.card_number:
            if pin == account.pin:
                print('You have successfully logged in!')
                a = account_menu()
                while a != 0:
                    if a == 1:
                        print(account.balance)
                        a = account_menu()
                    elif a == 2:
                        print('You have successfully logged out!')
                        break
            else:
                print('Wrong card number or PIN!')
                a = 'wrong'
            return a
        else:
            print('Wrong card number or PIN!')
            a = 'wrong'
            return a


while answer != 0:
    if answer == 1:
        create()
        answer = welcome()
    elif answer == 2:
        a = view_account()
        if a == 0:
            break
        else:
            answer = welcome()
print('Bye!')


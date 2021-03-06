import random

import sqlite3


class Account:
    all_accounts = []

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

    def output(self, transfer):
        self.balance = self.balance - transfer

    def income(self, transfer):
        self.balance = self.balance + transfer

    def insert(self, conn):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO card (number, pin, balance) VALUES (' + str(self.card_number) + ', ' + str(self.pin) + ', ' + str(self.balance) + ')')
        conn.commit()

    def update(self, conn):
        cursor = conn.cursor()
        cursor.execute('UPDATE card SET balance = ' + str(self.balance) + ' WHERE number =' + str(self.card_number))
        conn.commit()

    def data_check(self, card_number, pin):
        for account in Account.all_accounts:
            if self.card_number == card_number and self.pin == pin:
                return True
            else:
                return False





def welcome():
    print('1. Create an account')
    print('2. Log into account')
    print('0. Exit')
    answer = int(input())
    return answer


def create_card_number():
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
    return card_number


def create_account(conn):
    card_number = create_card_number()
    pin = random.randint(1111, 9999)
    account = Account(card_number, pin)
    Account.all_accounts.append(account)
    account.insert(conn)
    print('')
    print('Your card has been created')
    print('Your card number:')
    print(account.card_number)
    print('Your card PIN:')
    print(account.pin)
    print('')
    print(Account.all_accounts)
    return account



def account_menu():
    print('')
    print('1. Balance')
    print('2. Add income')
    print('5. Log out')
    print('0. Exit')
    menu_item = int(input())
    return menu_item


def income(account):
    print("Enter income:")
    income = int(input())
    account.income(income)
    print(account.balance)
    account.update(conn)
    print('Income was added!')


def view_account():
    print('Enter your card number:')
    card_number = int(input())
    print('Enter your PIN:')
    pin = int(input())
    print('')
    for account in Account.all_accounts:
        if account.data_check(card_number, pin) is True:
            print('You have successfully logged in!')
            menu_item = account_menu()
            while menu_item != 0:
                if menu_item == 1:
                    print(account.balance)
                    menu_item = account_menu()
                elif menu_item == 2:
                    income(account)
                    menu_item = account_menu()
                elif menu_item == 5:
                    print('You have successfully logged out!')
                    break
        else:
            print('Wrong card number or PIN!')
            menu_item = 'wrong'
            return menu_item



conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()

cursor.execute('DROP TABLE card')
cursor.execute('CREATE TABLE card ( id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
conn.commit()

answer = welcome()

while answer != 0:
    if answer == 1:
        create_account(conn)
        answer = welcome()
    elif answer == 2:
        menu_item = view_account()
        if menu_item == 0:
            break
        else:
            answer = welcome()
print('Bye!')

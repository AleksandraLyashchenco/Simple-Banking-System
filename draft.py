import random

import sqlite3


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


def save_account(conn, cursor, account):
    insert = 'INSERT INTO card (number, pin, balance) VALUES (' + str(account.card_number) + ', ' + str(account.pin) + ', ' + str(account.balance) + ');'
    cursor.execute(insert)
    conn.commit()


def create(conn, cursor):
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
    save_account(conn, cursor, account)
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
    print('2. Add income')
    print('3. Do transfer')
    print('4. Close account')
    print('5. Log out')
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
        if account in Account.all_accounts:
            print('You have successfully logged in!')
            a = account_menu()
            while a != 0:
                if a == 1:
                    print(account.balance)
                    a = account_menu()
                elif a == 2:
                    print("Enter income:")
                    income = int(input())
                    account.balance = account.balance + income
                    print(account.balance)
                    cursor.execute('UPDATE card SET balance = ' + str(account.balance) + ' WHERE number =' + str(account.card_number))
                    conn.commit()
                    print('Income was added!')
                    a = account_menu()
                elif a == 3:
                    print("написать код transfer")
                    break
                elif a == 4:
                    cursor.execute('DELETE FROM card WHERE number =' + str(account.card_number))
                    conn.commit()
                    Account.all_accounts.remove(account)
                    print('The account has been closed!')
                    print('')
                    break
                elif a == 5:
                    print('You have successfully logged out!')
                    break
        else:
            print('Wrong card number or PIN!')
            print('')
            a = 'wrong'
            return a
    else:
        print('Wrong card number or PIN!')
        print('')
        a = 'wrong'
        return a


conn = sqlite3.connect('card.s3db')
cursor = conn.cursor()

cursor.execute('DROP TABLE card')
cursor.execute('CREATE TABLE card ( id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)')
conn.commit()

answer = welcome()

while answer != 0:
    if answer == 1:
        create(conn, cursor)
        answer = welcome()
    elif answer == 2:
        a = view_account()
        if a == 0:
            break
        else:
            answer = welcome()
print('Bye!')

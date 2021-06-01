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
    copy_card_number = list.copy(card_number)
    for i in range(len(copy_card_number)):
        old_value = copy_card_number[i]
        new_value = int(old_value)
        copy_card_number[i] = new_value
    for index, i in enumerate(copy_card_number):
        if index % 2 == 0:
            i = i * 2
        copy_card_number[index] = i
        if copy_card_number[index] > 9:
            copy_card_number[index] = copy_card_number[index] - 9
    last_number = 0
    if sum(copy_card_number) % 10 > 0:
        last_number = abs(10 - (sum(copy_card_number) % 10))
    card_number.append(last_number)
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
    selected_item = int(input())
    return selected_item


def luhn_chek(num_for_transf):
    card_number = list(str(num_for_transf))
    copy_card_number = list.copy(card_number)
    for i in range(len(copy_card_number)):
        old_value = copy_card_number[i]
        new_value = int(old_value)
        copy_card_number[i] = new_value
    for index, i in enumerate(copy_card_number):
        if index % 2 == 0:
            i = i * 2
        copy_card_number[index] = i
        if copy_card_number[index] > 9:
            copy_card_number[index] = copy_card_number[index] - 9
    if sum(copy_card_number) % 10 > 0:
        ans = 0
    else:
        ans = 1
    return ans

def transf_to_recipient_account(num_for_transf, transfer_funds):
    for account in Account.all_accounts:
        if card_number == num_for_transf:
            account.income(transfer_funds)
            account.update()
    cursor.execute('SELECT balance FROM card WHERE number = ' + str(num_for_transf))
    balance = cursor.fetchall()
    print(balance)


def transfer(card_number, account):
    print('Transfer')
    print('Enter card number:')
    num_for_transf = int(input())
    if num_for_transf == card_number:
        print("You can't transfer money to the same account!")
        account_menu()
    elif luhn_chek(num_for_transf) == 0:
        print('Probably you made a mistake in the card number. Please try again!')
        account_menu()
    elif luhn_chek(num_for_transf) == 1:
        cursor.execute('SELECT id FROM card WHERE number = ' + str(num_for_transf))
        id_exists = cursor.fetchall()
        if len(id_exists) == 0:
            print(id_exists)
            print('Such a card does not exist.')
        else:
            print(id_exists)
            print(id_exists[0][0])
            print('Enter how much money you want to transfer:')
            transfer_funds = int(input())
            if transfer_funds > account.balance:
                print('Not enough money!')
            else:
                account.output(transfer_funds)
                account.update()
                print('баланс изменен на счету отправителя')
                print('тут должен быть код перевода')
                transf_to_recipient_account(num_for_transf, transfer_funds)

    else:
        print("Пока что все ок")


def income(account):
    print("Enter income:")
    income = int(input())
    account.balance = account.balance + income
    print(account.balance)
    cursor.execute('UPDATE card SET balance = ' + str(account.balance) + ' WHERE number =' + str(account.card_number))
    conn.commit()
    print('Income was added!')


def delete_account(account):
    cursor.execute('DELETE FROM card WHERE number =' + str(account.card_number))
    conn.commit()
    Account.all_accounts.remove(account)
    print('The account has been closed!')
    print('')


def view_account():
    print('Enter your card number:')
    card_number = int(input())
    print('Enter your PIN:')
    pin = int(input())
    print('')
    for account in Account.all_accounts:
        if account in Account.all_accounts:
            print('You have successfully logged in!')
            selected_item = account_menu()
            while selected_item != 0:
                if selected_item == 1:
                    cursor.execute('SELECT balance FROM card WHERE number = ' + str(account.card_number))
                    balance = cursor.fetchall()
                    print(balance[0][0])
                    selected_item = account_menu()
                elif selected_item == 2:
                    income(account)
                    selected_item = account_menu()
                elif selected_item == 3:
                    transfer(selected_item, card_number,)
                    selected_item = account_menu()
                elif selected_item == 4:
                    delete_account(account)
                    break
                elif selected_item == 5:
                    print('You have successfully logged out!')
                    print('')
                    break

        else:
            print('Wrong card number or PIN!')
            print('')
            selected_item = 'wrong'
            return selected_item


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
        selected_item = view_account()
        if selected_item == 0 or selected_item == 4 or selected_item == 5:
            break
        else:
            answer = welcome()
print('Bye!')

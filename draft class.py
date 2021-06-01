import random

import sqlite3


class Account:
    all_accounts = []

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

    def outcome(self, transfer):
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
        
    



# def refer_to_database(query, account):
#    query = 'INSERT INTO card (number, pin, balance) VALUES (' + str(account.card_number) + ', ' + str(account.pin) + ', ' + str(account.balance) + ');'
#    cursor.execute(query)
#    conn.commit()


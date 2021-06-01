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
        cursor.execute('INSERT INTO card (number, pin, balance) VALUES (' + str(self.card_number) + ', ' + str(self.pin) + ', ' + str(self.balance) + ')')
        cursor = cursor = conn.cursor()
        conn.commit()


    def update(conn, replaceable_variable, var_replac_value, known_vapiable, var_known_value):
        cursor.execute('UPDATE card SET ' + str(replaceable_variable) + ' = ' + str(var_replac_value) + ' WHERE ' + str(known_vapiable) + ' = ' + str(var_known_value))
        conn.commit()
        
    



# def refer_to_database(query, account):
#    query = 'INSERT INTO card (number, pin, balance) VALUES (' + str(account.card_number) + ', ' + str(account.pin) + ', ' + str(account.balance) + ');'
#    cursor.execute(query)
#    conn.commit()


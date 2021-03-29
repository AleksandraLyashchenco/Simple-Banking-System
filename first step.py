import random


class Account:
    all_accounts = []
    account = []
    balance = 0

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0
        Account.all_accounts.append(self)


def create():
    Account.card_number = int('400000' + str(int(random.randint(1000000000, 9999999999))))
    Account.pin = random.randint(1111, 9999)
    Account.account = [Account.card_number, Account.pin, Account.balance]
    Account.all_accounts.append(Account.account)


n = 0
while n < 10:
    create()
    n += 1
print(Account.all_accounts)

for Account.account in Account.all_accounts:
    print(str(Account.account[0]) + ' = ' + str(Account.account[2]))

class Account:
    all_accounts = []

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

    def income(self):
        print('Введите сумму пополнения')
        income = int(input())
        self.balance = self.balance + income
        print(self.balance)
        return self.balance

    def output(self):
        print('Введите сумму перевода')
        transfer = int(input())
        self.balance = self.balance - transfer
        print(self.balance)
        return  self.balance

first = Account(123456, 1234)
second = Account(654321, 7654)

first.income()
first.income()

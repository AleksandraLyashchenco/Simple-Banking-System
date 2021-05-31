class Account:
    all_accounts = []

    def __init__(self, card_number, pin):
        self.card_number = card_number
        self.pin = pin
        self.balance = 0

    def income(self):
        income = int(input())
        self.balance = self.balance + income
        return self.balance

    def output(self):
        transfer = int(input())
        self.balance = self.balance - transfer
        return  self.balance

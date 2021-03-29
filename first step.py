import random 


class Account: 
    all_accounts = []
    

    def __init__(self, card_number, pin): 
        self.card_number = card_number 
        self.pin = pin
        self.balance = 0
        Account.all_accounts.append(account)

def create():
    card_number = int('400000' + str(int(random.randint(1000000000, 9999999999))))
    pin = random.randint(1111, 9999)
    account = Account(card_number, pin)
    


n = 0
while n < 10:
    create()
    n += 1
print(Account.all_accounts)

for account in Account.all_accounts:
    print(str(account.card_number) + ' = ' + str(account.pin))

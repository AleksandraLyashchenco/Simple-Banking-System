import random #импорт модуля "рандом"


class Account: # обьявляю класс (имя - "Аккаунт")
    all_accounts = []# обьявляю переменную, присваиваю значение - пустой список (атрибут)
    

    def __init__(self, card_number, pin): #конструктор инит
        self.card_number = card_number # личному "card_number" присваиваю значение "card_number"
        self.pin = pin#личному "card_number" присваиваю значение "card_number"
        self.balance = 0#личному "pin" присваиваю значение "pin"
     

def create():#обьявляю метод 
    card_number = int('400000' + str(int(random.randint(1000000000, 9999999999))))#присваиваю значение атрибуту card_number
    pin = random.randint(1111, 9999)#присваиваю значение атрибуту pin
    account = Account(card_number, pin)
    Account.all_accounts.append(account)#добавляю список account в список all_account


n = 0# переменная n, значение 0
while n < 10:# "пока n меньше 10":
    create()# вызывать функцию  create
    n += 1# шаг 1
print(Account.all_accounts)#печатать all_accounts

for Account.account in Account.all_accounts:#для каждого елемента account в списке all_accounts:
    print(str(Account.account.card_number) + ' = ' + str(Account.account.pin))# печатать " первый элемент = третий элемент"

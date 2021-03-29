import random #импорт модуля "рандом"


class Account: # обьявляю класс (имя - "Аккаунт")
    all_accounts = []# обьявляю переменную, присваиваю значение - пустой список (атрибут)
    balance = 0# обьявляю переменную, присваиваю значение - 0, (атрибут)

    def __init__(self, card_number, pin): #конструктор инит
        self.card_number = card_number # личному "card_number" присваиваю значение "card_number"
        self.pin = pin#личному "card_number" присваиваю значение "card_number"
        self.balance = 0#личному "pin" присваиваю значение "pin"
     

def create():#обьявляю метод 
    Account.card_number = int('400000' + str(int(random.randint(1000000000, 9999999999))))#присваиваю значение атрибуту card_number
    Account.pin = random.randint(1111, 9999)#присваиваю значение атрибуту pin
    Account.account = [Account.card_number, Account.pin, Account.balance]#обьявляю переменную и присваивааю ей значение
    Account.all_accounts.append(Account.account)#добавляю список account в список all_account


n = 0# переменная n, значение 0
while n < 10:# "пока n меньше 10":
    create()# вызывать функцию  create
    n += 1# шаг 1
print(Account.all_accounts)#печатать all_accounts

for Account.account in Account.all_accounts:#для каждого елемента account в списке all_accounts:
    print(str(Account.account[0]) + ' = ' + str(Account.account[2]))# печатать " первый элемент = третий элемент"

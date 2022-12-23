"""
Создайте класс банковского аккаунта по аналогии с примером из презентации.
 Сделайте атрибут name защищенным, аbalance и passport приватными.
Добавьте геттер-методы на pasport и balance.
Сделайте смену номера паспорта по поролю.
А изменение баланса на определенную сумму(сумма не может падать меньше 0,
так что сделайте проверку).
Создайте метод удаляющий паспортные данные с аккаунта(также по поролю).
"""


class Bank_account():
    def __init__(self, _name, __balance, __passport):
        self.name = _name
        self.balance = __balance
        self.passport = __passport

    def getpassport(self):
        return self.passport

    def getbalance(self):
        return self.balance

    def setPassport(self):
        password = input('Введите пароль:')
        while password != 'qwerty12345':
            if password == 'qwerty12345':
                self.passport = 1234_345678

            else:
                print('Попробуйте еще раз')
                password = input('Введите пароль:')
        print('Данные вашего паспорта изменены. \nНомер вашего паспорта:', self.passport)

    def setBalance(self):
        newBalance = ''
        while self.balance > 0 and newBalance != 0:
            print('Вам доступно:', self.balance)
            newBalance = int(input('Введите сумму которую хотите снять (или 0, если не хотите):'))
            if newBalance <= self.balance:
                self.balance -= newBalance
            else:
                print('У вас недостаточно денег, попробуйте больше работать')
            if self.balance == 0:
                print('У вас больше нет денег, найдите работу!')
        print('Спасибо, что пользуетесь услугами Яна банка!')
        return ''


    def delpassport(self):
        password = ''
        while password != 'qwerty12345':
            password = input('Введите пароль:')
            if password == 'qwerty12345':
                del self.passport
            else:
                print('Попробуйте еще раз')
        print('Ваш паспорт удален.')



ann = Bank_account('Ann', 10000, 1111_1111111)
print(ann.delpassport())
print(ann.getpassport())



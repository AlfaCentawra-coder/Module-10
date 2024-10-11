
from threading import Thread, Lock
from random import randint
from time import sleep

class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.lock = Lock()

    def deposit(self):
        top_up_transactions = 100
        for tran_on in range(top_up_transactions):
            i = randint(50, 500)
            with self.lock:
                self.balance += i
                sleep(0.5)
            print(f'Пополнение: {i}. Баланс: {self.balance}')

    def take(self):
        withdrawal_transactions = 100
        for tran_off in range(withdrawal_transactions):
            q = randint(50, 500)
            print(f'Запрос на {q}')
            with self.lock:
                if q <= self.balance:
                    self.balance -= q
                    sleep(0.5)
                    print(f'Снятие: {q}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонён. Недостаточно средств на счете')

bk = Bank(0)

th1 = Thread(target=bk.deposit)
th2 = Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


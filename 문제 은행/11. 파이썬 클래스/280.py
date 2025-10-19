import random

class Account:
    obj_count = 0

    def __init__(self, owner, remain_cost):
        self.owner = owner
        self.remain_cost = remain_cost
        self.bank_name = 'SC은행'
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = f'{num1}-{num2}-{num3}'
        Account.obj_count += 1
        self.deposit_count = 0
        self.deposit_history_list = []
        self.withdraw_history_list = []
    
    @classmethod
    def get_account_num(cls):
        print(cls.obj_count)

    def deposit(self, cost):
        if cost >= 1:
            self.remain_cost += cost
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.remain_cost *= 1.01

            self.deposit_history_list.append(cost)

    def withdraw(self, cost):
        if cost <= self.remain_cost:
            self.remain_cost -= cost

            self.withdraw_history_list.append(cost)

    def display_info(self):
        print(self.bank_name)
        print(self.owner)
        print(self.account_number)
        print(f'{self.remain_cost:,}')

    def deposit_history(self):
        for history in self.deposit_history_list:
            print(history)

    def withdraw_history(self):
        for history in self.withdraw_history_list:
            print(history)

account = Account('홍길동', 1000000)
account.deposit(100)
account.deposit(300)
account.deposit(800)
account.deposit_history()
account.withdraw(200)
account.withdraw(500)
account.withdraw(300)
account.withdraw_history()
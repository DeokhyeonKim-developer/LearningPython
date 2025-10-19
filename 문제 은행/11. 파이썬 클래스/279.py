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
    
    @classmethod
    def get_account_num(cls):
        print(cls.obj_count)

    def deposit(self, cost):
        if cost >= 1:
            self.remain_cost += cost
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.remain_cost *= 1.01


    def withdraw(self, cost):
        if cost <= self.remain_cost:
            self.remain_cost -= cost

    def display_info(self):
        print(self.bank_name)
        print(self.owner)
        print(self.account_number)
        print(f'{self.remain_cost:,}')

account = Account('홍길동', 2000000)
account2 = Account('김철수', 1000000)
account3 = Account('김영희', 700000)
account_list = []
account_list.append(account)
account_list.append(account2)
account_list.append(account3)

for account in account_list:
    if account.remain_cost >= 1000000:
        account.display_info()
        print()
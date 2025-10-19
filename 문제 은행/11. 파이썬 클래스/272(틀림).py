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

account = Account('홍길동', 100)
account2 = Account('김철수', 200)
print(Account.obj_count)
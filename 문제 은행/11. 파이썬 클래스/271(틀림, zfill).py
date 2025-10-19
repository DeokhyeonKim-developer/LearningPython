import random

class Account:
    def __init__(self, owner, remain_cost):
        self.owner = owner
        self.remain_cost = remain_cost
        self.bank_name = 'SC은행'
        num1 = str(random.randint(0, 999)).zfill(3)
        num2 = str(random.randint(0, 99)).zfill(2)
        num3 = str(random.randint(0, 999999)).zfill(6)
        self.account_number = f'{num1}-{num2}-{num3}'

account = Account('홍길동', 100)
print(account.owner)
print(account.account_number)
print(account.remain_cost)
print(account.bank_name)
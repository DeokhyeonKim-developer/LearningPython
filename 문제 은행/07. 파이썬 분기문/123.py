money = input('입력: ')
cash = float(money.split()[0])

if money.split()[1] == '달러':
    print(cash * 1167)
elif money.split()[1] == '엔':
    print(cash * 1096)
elif money.split()[1] == '유로':
    print(cash * 1268)
elif money.split()[1] == '위안':
    print(cash * 171)
else:
    print('변환할 수 없는 단위')
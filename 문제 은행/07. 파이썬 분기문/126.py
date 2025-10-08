address = input('우편번호: ')
address_center = int(address[2])

if 0 <= address_center <= 2:
    print('강북구')
elif 3 <= address_center <= 5:
    print('도봉구')
else:
    print('노원구')
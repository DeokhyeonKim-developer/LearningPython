num = input('주민등록번호: ')
num_region = int(num.split('-')[1][1:3])

if 0 <= num_region <= 8:
    print('서울 입니다.')
else:
    print('서울이 아닙니다.')
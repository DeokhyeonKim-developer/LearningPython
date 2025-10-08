string = input('주민등록번호: ')

# 1차 계산
total = int(string[0]) * 2 + int(string[1]) * 3 + int(string[2]) * 4 + int(string[3]) * 5 + int(string[4]) * 6 + int(string[5]) * 7 + \
    int(string[7]) * 8 + int(string[8]) * 9 + int(string[9]) * 2 + int(string[10]) * 3 + int(string[11]) * 4 + int(string[12]) * 5

total_remain = total % 11

# 2차 계산
result = 11 - total_remain

if result == int(string[-1]):
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')
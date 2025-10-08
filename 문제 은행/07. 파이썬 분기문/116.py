time = input('현재시간:')

if time.split(':')[1] == '00':
    print('정각 입니다.')
else:
    print('정각이 아닙니다.')
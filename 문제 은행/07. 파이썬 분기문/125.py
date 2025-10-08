phone_book = {'011': 'SKT', '016': 'KT', '019': 'LGU', '010': '알수없음'}
phone = input('휴대전화 번호 입력: ')
number = phone[:3]

if number == '011':
    print(f'당신은 {phone_book['011']} 사용자입니다.')
elif number == '016':
    print(f'당신은 {phone_book['016']} 사용자입니다.')
elif number == '019':
    print(f'당신은 {phone_book['019']} 사용자입니다.')
elif number == '010':
    print('알수없습니다.')
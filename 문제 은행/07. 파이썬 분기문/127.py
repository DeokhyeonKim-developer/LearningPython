num = input('주민등록번호: ')
num_split = num.split('-')[1][0]

if num_split == '1' or num_split == '3':
    print('남자')
elif num_split == '2' or num_split == '4':
    print('여자')
fruit = ["사과", "포도", "홍시"]
string = input('좋아하는 과일은?')

if string not in fruit:
    print('오답입니다.')
else:
    print('정답입니다.')
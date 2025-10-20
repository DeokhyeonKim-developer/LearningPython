with open('C:\\Users\\TheEx\\OneDrive\\Desktop\\매수종목2.txt', 'rt', encoding='utf-8') as f:
    lines = f.readlines()

종목_dict = {}
for line in lines:
    line = line.strip()
    종목_dict[line.split(' ')[0]] = line.split(' ')[1]

print(종목_dict)
with open('C:\\Users\\사용자명\\OneDrive\\Desktop\\매수종목1.txt', 'rt', encoding='utf-8') as f:
    종목리스트 = f.readlines()

최종리스트 = []
for line in 종목리스트:
    line = line.replace('\n', '')
    최종리스트.append(line)

print(최종리스트)
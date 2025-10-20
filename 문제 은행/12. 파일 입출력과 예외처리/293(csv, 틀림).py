import csv

with open('C:\\Users\\사용자명\\OneDrive\\Desktop\\매수종목2.csv', 'wt', encoding='cp949', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['종목명', '종목코드', 'PER'])
    writer.writerow(['삼성전자', '005930', '15.79'])
    writer.writerow(['NAVER', '035420', '55.82'])
import datetime

today = datetime.date.today()
for num in range(5, 0, -1):
    diff_days = datetime.timedelta(days=num)
    print(today - diff_days)
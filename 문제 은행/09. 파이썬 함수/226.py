def print_5xn(string):
    number_of_times = 0
    while number_of_times < len(string) // 5:
        print(string[number_of_times * 5 : (number_of_times + 1) * 5])
        number_of_times += 1

print_5xn('아이엠어보이유알어걸')
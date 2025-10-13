def printmxn(string, num):
    number_of_times = 0
    while number_of_times < len(string) / num:
        print(string[number_of_times * num : (number_of_times + 1) * num])
        number_of_times += 1

printmxn("아이엠어보이유알어걸", 3)
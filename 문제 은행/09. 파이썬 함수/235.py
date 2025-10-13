def convert_int(string):
    string = string.replace(',', '')
    return int(string)

num = convert_int('1,234,567')

print(num, type(num))
def make_list(string):
    letter_list = []
    for letter in string:
        letter_list.append(letter)
    return letter_list

letter_list = make_list('abcd')
print(letter_list)
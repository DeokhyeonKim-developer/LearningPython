def pickup_even(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

even_list = pickup_even([3, 4, 5, 6, 7, 8])

print(even_list)
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result = []

for row in data:
    temp_list = []
    for col in row:
        temp_list += [col + col * 0.00014]
    result.append(temp_list)
print(result)
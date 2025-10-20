per = ["10.31", "", "8.00"]

per_list = []
for i in per:
    try:
        per_list.append(float(i))
    except:
        per_list.append(0)

print(per_list)
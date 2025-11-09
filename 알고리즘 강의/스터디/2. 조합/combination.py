l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = 5
choose = []

def combination(index, level):
    # base case
    if level == r:
        print(choose)
        return
    
    # recursive case
    for i in range(index, len(l)):
        choose.append(l[i])
        combination(i + 1, level + 1)
        choose.pop()

combination(0, 0)
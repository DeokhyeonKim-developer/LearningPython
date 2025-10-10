def print_max(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)

a = int(input())
b = int(input())
c = int(input())

print_max(a, b, c)
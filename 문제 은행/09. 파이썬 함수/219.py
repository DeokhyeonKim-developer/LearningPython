def print_arithmetic_operation(a, b):
    print(a, '+', b, '=', a + b)
    print(a, '-', b, '=', a - b)
    print(a, '*', b, '=', a * b)
    print(a, '/', b, '=', a / b)

a = int(input())
b = int(input())
print_arithmetic_operation(a, b)
n = int(input())

def fibonacci_numbers(a, b, i, n):
    # base case
    if i >= n:
        print(a)
        return
    # recursive case
    return fibonacci_numbers(b, a + b, i + 1, n)

fibonacci_numbers(0, 1, 0, n)
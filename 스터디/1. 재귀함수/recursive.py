# 1부터 n까지 더하는 함수
def recursive(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return recursive(n-1) + n

print(recursive(10))
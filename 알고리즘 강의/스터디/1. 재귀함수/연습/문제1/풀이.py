def factorial(n):
    # base case
    if n == 0:
        return 1

    # recursive case
    return factorial(n-1) * n

# 테스트
print(f"5! = {factorial(5)}") # 예상 출력: 120
print(f"0! = {factorial(0)}") # 예상 출력: 1
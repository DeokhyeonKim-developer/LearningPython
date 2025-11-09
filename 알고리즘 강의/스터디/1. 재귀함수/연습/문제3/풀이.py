def fibonacci(n):
    # base case
    if n == 2 or n == 1:
        return 1
    elif n == 0:
        return 0

    # recursive case
    return fibonacci(n-1) + fibonacci(n-2)

# 테스트
print(f"피보나치 6번째 항 = {fibonacci(6)}") # 예상 출력: 8
print(f"피보나치 0번째 항 = {fibonacci(0)}") # 예상 출력: 0
print(f"피보나치 1번째 항 = {fibonacci(1)}") # 예상 출력: 1
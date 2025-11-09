def list_sum(nums):
    # base case
    if len(nums) == 0:
        return 0

    # recursive case
    last = nums.pop()
    return list_sum(nums) + last

# 테스트
print(f"[1, 2, 3, 4, 5]의 합 = {list_sum([1, 2, 3, 4, 5])}") # 예상 출력: 15
print(f"[]의 합 = {list_sum([])}") # 예상 출력: 0
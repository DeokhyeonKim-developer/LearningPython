'''
- n, m
- A, S
- S의 각 요소를 나머지 연산하여 S_mod를 만듦
- S_mod에서 값이 0인 개수를 세고, Count리스트에 각 원소의 값을 인덱스로 해서 개수 세기
- S_mod에서 원소의 값을 0~M-1까지로 돌면서 개수로 조합의 수를 구해 정답에 덧셈
'''

import sys
import math
input = sys.stdin.readline


n, m = map(int, input().split())
A = list(map(int, input().split()))

S = []
S.append(A[0]) # i == 0
for i in range(1, n): # i > 0
    S.append(S[i-1] + A[i])

S_mod = []
for i in S:
    S_mod.append(i % m)

C = [0] * m
result = 0
for i in S_mod:
    remainder = i % n
    C[remainder] += 1 # 중요
    if i == 0:
        result += 1

for i in range(m):
    result += math.comb(C[i], 2)

print(result)
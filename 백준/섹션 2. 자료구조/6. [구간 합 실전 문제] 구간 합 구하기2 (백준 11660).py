'''
- n, m
- n만큼 돌면서 원본 배열을 저장     # [n+1][n+1]임에 주의
- 합 배열 D 생성    # index 세팅을 1, 1부터 시작하게 됨에 주의
- m 만큼 돌면서 질의에 대해 합 배열 D를 이용해 해결
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n + 1)] # 0행 세팅
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + list(map(int, input().split()))
    A.append(A_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, (input().split()))
    answer = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]
    print(answer)
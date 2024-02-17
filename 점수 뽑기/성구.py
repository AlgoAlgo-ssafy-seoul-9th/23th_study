import sys
from collections import defaultdict
input = sys.stdin.readline


N, K = map(int, input().split())
klass = [tuple(map(int, input().split())) for _ in range(4)]

# 1, 2반 점수 합산 구해놓기
cand = defaultdict(int)

for i in range(N):
    for j in range(N):
        k12 = klass[0][i] + klass[1][j]
        if k12 < K:
            cand[k12] += 1

# 3, 4반 포함해서 돌리기
cnt = 0
for i in range(N):
    for j in range(N):
        # defaultdict 이기에 해당 점수가 없으면 0임
        cnt += cand[K-klass[2][i]-klass[3][j]]
print(cnt)
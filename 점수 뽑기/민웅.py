import sys
input = sys.stdin.readline

N, K = map(int, input().split())

C = []
cnt = 0
for _ in range(4):
    C.append(list(map(int, input().split())))

class_sum = [dict(), dict()]
for i in range(N):
    for j in range(N):
        t1 = C[0][i]+C[1][j]
        t2 = C[2][i]+C[3][j]

        if t1 in class_sum[0].keys():
            class_sum[0][t1] += 1
        else:
            class_sum[0][t1] = 1

        if t2 in class_sum[1].keys():
            class_sum[1][t2] += 1
        else:
            class_sum[1][t2] = 1

for s1 in class_sum[0].keys():
    tmp = K - s1
    if tmp in class_sum[1].keys():
        cnt += class_sum[0][s1]*class_sum[1][tmp]

print(cnt)
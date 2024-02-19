import sys
input = sys.stdin.readline

N, K = map(int, input().split())
score = []
for i in range(4):
    score.append(list(map(int, input().split())))
scoreA = {}
for i in score[0]:
    for j in score[1]:
        scoreA[i+j] = scoreA.get(i+j, 0) + 1
cnt = 0
for i in score[2]:
    for j in score[3]:
        if K-(i+j) in scoreA:
            cnt += scoreA[K-(i+j)]
print(cnt)
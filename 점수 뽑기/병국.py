n,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(4)]
# print(arr)

first = {}
second = {}


for i in range(n):
    tmp = arr[0][i]
    for j in range(n):
        tmp += arr[1][j]
        if tmp in first:
            first[tmp] += 1
        else:
            first[tmp] = 1
        tmp -= arr[1][j]

for i in range(n):
    tmp = arr[2][i]
    for j in range(n):
        tmp += arr[3][j]
        if tmp in second:
            second[tmp] += 1
        else:
            second[tmp] = 1
        tmp -= arr[3][j]
# print(first)
# print(second)
# 0
answer = 0
for i in first:
    tmp_answer = K - i
    if tmp_answer in second:
        answer += (first[i]*second[tmp_answer])
print(answer)
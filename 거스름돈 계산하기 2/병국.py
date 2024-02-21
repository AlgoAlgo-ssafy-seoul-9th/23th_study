N,S = map(int,input().split())
coins = []
for _ in range(N):
    V,A = map(int,input().split())
    coins.append((V,A))
dp = [float('inf')] * (S + 1)
dp[0] = 0

for value, count in coins:
    for i in range(S, value-1, -1):
        for j in range(1,count+1):
            if i - value * j >= 0:
                dp[i] = min(dp[i], dp[i-value * j] + j)
    # print(dp)
# print(dp)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
coins = []

for _ in range(N):
    v, a = map(int, input().split())
    coins.append([v, a])

coins.sort(key=lambda x: -x[0])

dp = [float('inf')] * (S + 1)
dp[0] = 0

for i in range(N):
    v = coins[i][0]
    a = coins[i][1]
    # 거스름돈의 범위까지 반복
    for j in range(S + 1):
        # 동전을 가지고 있는 개수만큼 확인
        for k in range(1, a + 1):
            if j + v * k <= S:
                # 원래 값, 현재동전값만큼 뺀 거스름돈 + 현재동전개수 중 작은값으로 계속 갱신
                dp[j + v * k] = min(dp[j + v * k], dp[j] + k)

if dp[S] == float('inf'):
    print(-1)
else:
    print(dp[S])

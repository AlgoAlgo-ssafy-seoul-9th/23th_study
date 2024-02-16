import sys
input = sys.stdin.readline

'''
dp
방문을 했었는가? -> yes -> coin 개수만큼 방문하고 있는 {값 + coin * 개수 } 위치 갱신
               -> no -> 다음 탐색

값이 0인 위치는 default로 0으로 초기화하여, coin의 개수만큼 값들을 넣어줄 수 있음

거스름돈의 값이 방문이 안됨 -> 거스름돈을 만들 수 없음

'''

N, S = map(int, input().split())
coins = [tuple(map(int, input().split())) for _ in range(N)]
dp = [5_001] * (S+1) 
dp[0] = 0

for v, a in coins:
    for i in range(S+1):
        if v + i > S:
            break
        if dp[i] != 5001:
            for j in range(1, a+1):
                if i + v*j <=S:
                    dp[i+v*j] = min(dp[i+v*j], dp[i]+j)
if dp[S] == 5001:
    print(-1)
else:
    print(dp[S])
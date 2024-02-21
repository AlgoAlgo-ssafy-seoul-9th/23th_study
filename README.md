# 23th_study

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [주사위 윷놀이](https://www.acmicpc.net/problem/17825)

### [민웅](./주사위%20윷놀이/민웅.py)

```py
# 17825_주사위 윷놀이_Dice-Yut
import sys
input = sys.stdin.readline

def bt(dice_idx, pieces_loc, score):
    global ans

    # 마지막 주사위까지 체크한 경우면 답 갱신
    if dice_idx == 10:
        if score > ans:
            ans = score
        return

    # 말 하나씩 확인
    for i in range(4):
        line, location = pieces_loc[i]
        # 방향꺾어야 하는 위치인지 확인
        if line == 0 and location in blue_path_dict.keys():
            line = blue_path_dict[location]
            location = 0
        # 도착점 도달한 말은 스킵
        if line == 6:
            continue

        move_point = dice_num[dice_idx]
        # 말들 이동
        while move_point:
            location += 1
            move_point -= 1
            if line in [1, 2, 3]:
                if location == len(dice_field[line])-1:
                    line = 4
                    location = 0
            if line == 4 or line == 0:
                if location == len(dice_field[line])-1:
                    line = 5
                    location = 0

        tmp_line, tmp_loc = pieces_loc[i]

        # 도착점에 도착한경우거나 이동하려는곳에 말이 없는경우 백트래킹 탐색
        if location > len(dice_field[line])-1:
            pieces_loc[i] = (6, 0)
            bt(dice_idx+1, pieces_loc,  score)

        elif (line, location) not in pieces_loc:
            pieces_loc[i] = (line, location)
            bt(dice_idx+1, pieces_loc, score+dice_field[line][location])

        # 이동한 말 백트래킹 위해서 원래 위치로 복구
        pieces_loc[i] = tmp_line, tmp_loc


dice_num = list(map(int, input().split()))

dice_field = [[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
              [10, 13, 16, 19, 25],
              [20, 22, 24, 25],
              [30, 28, 27, 26, 25],
              [25, 30, 35, 40],
              [40]]
# 방향꺽어야하는 위치
blue_path_dict = {
    5: 1,
    10: 2,
    15: 3,
    20: 5,
}

pieces = [(0, 0) for _ in range(4)]

ans = 0
bt(0, pieces, 0)

print(ans)

```

### [병국](./주사위%20윷놀이/병국.py)

```py


```

### [상미](./주사위%20윷놀이/상미.py)

```py
## 백준 17825_ 주사위 윷놀이
## 힌트 봄 ㅠ

import sys
input = sys.stdin.readline

graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

dice = list(map(int, input().split()))
answer = 0

def sol(depth, result, horses):
    global answer
    if depth == 10:
        answer = max(answer, result)
        return

    for i in range(4):
        # 현재 말 위치
        x = horses[i]

        # 현재 말 위치가 2갈래 갈 수 있는 위치(10, 20, 30)인지 체크
        if len(graph[x]) == 2:
            # 파란 길 한 칸 진입
            x = graph[x][1]
        else:
            # 빨간 길 한 칸 진입
            x = graph[x][0]

        # 나온 주사위 값 만큼 말 이동(위에서 1칸 이동했기 때문에 1 덜 이동함)
        for d in range(1, dice[depth]):
            x = graph[x][0]

        # 목적지에 도착했거나 or (아직 목적지가 아니고 and 거기에 말이 없다면)
        if x == 32 or (x < 32 and x not in horses):
            before = horses[i]  # 이전 말의 위치
            horses[i] = x  # 현재 말 위치 갱신

            sol(depth + 1, result + score[x], horses)

            horses[i] = before


sol(0, 0, [0, 0, 0, 0])
print(answer)


```

### [성구](./주사위%20윷놀이/성구.py)

```py

```

### [승우](./주사위%20윷놀이/승우.py)

```py


```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

## [점수 뽑기](https://www.codetree.ai/problems/picking-score/description)

### [민웅](./점수%20뽑기/민웅.py)

```py
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
```

### [병국](./점수%20뽑기/병국.py)

```py


```

### [상미](./점수%20뽑기/상미.py)

```py
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

```

### [성구](./점수%20뽑기/성구.py)

```py
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
```

### [승우](./점수%20뽑기/승우.py)

```py


```

## [최소 개수의 막대기](https://www.codetree.ai/problems/the-minimum-number-of-rods/description)

### [민웅](./최소%20개수의%20막대기/민웅.py)

```py
import sys
input = sys.stdin.readline
# 가로로 놓기, 세로로 놓기 중 선택
dxy = [(1, 0), (0, 1)]

# x,y 좌표값, 막대기수, 방문배열
def bt(x, y, cnt, visit):
    global ans

    # 마지막줄까지 체크 끝났으면 막대기수 정답갱신
    if x == N:
        if cnt < ans:
            ans = cnt
        return

    for i in range(y, M):
        # 그림자위치고, 아직 방문안한곳이면
        if trees[x][i] == '*' and not visit[x][i]:
            # 가로로 쭉 놓기, 세로로 쭉 놓기 한번씩 해봄
            for d in dxy:
                # 새로운 방문배열 채울 좌표리스트 만들어서 새로만든 방문배열위치 채우고 백트래킹
                new_stick_area = [[x, i]]
                tmp_visit = [[visit[a][b] for b in range(M)] for a in range(N)]
                nx = x + d[0]
                ny = i + d[1]
                # 가로 혹은 세로방향 쭉 더이상 그림자가 아닐때까지 놓기
                while True:
                    if 0 <= nx <= N-1 and 0 <= ny <= M-1:
                        if trees[nx][ny] == '*':
                            new_stick_area.append([nx, ny])
                            nx = nx + d[0]
                            ny = ny + d[1]
                        else:
                            break
                    else:
                        break

                for cordi in new_stick_area:
                    tmp_visit[cordi[0]][cordi[1]] = 1

                bt(x, i, cnt+1, tmp_visit)
            break
    else:
        bt(x+1, 0, cnt, visit)

N, M = map(int, input().split())

trees = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
ans = float('inf')

bt(0, 0, 0, visited)
print(ans)
```

### [병국](./최소%20개수의%20막대기/병국.py)

```py


```

### [상미](./최소%20개수의%20막대기/상미.py)

```py


```

### [성구](./최소%20개수의%20막대기/성구.py)

```py

```

### [승우](./최소%20개수의%20막대기/승우.py)

```py


```

## [거스름돈 계산하기 2](https://www.codetree.ai/problems/calculating-change2/description)

### [민웅](./거스름돈%20계산하기%202/민웅.py)

```py
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


```

### [병국](./거스름돈%20계산하기%202/병국.py)

```py


```

### [상미](./거스름돈%20계산하기%202/상미.py)

```py


```

### [성구](./거스름돈%20계산하기%202/성구.py)

```py
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
```

### [승우](./거스름돈%20계산하기%202/승우.py)

```py


```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>

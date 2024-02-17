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


```

### [병국](./점수%20뽑기/병국.py)

```py


```

### [상미](./점수%20뽑기/상미.py)

```py


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

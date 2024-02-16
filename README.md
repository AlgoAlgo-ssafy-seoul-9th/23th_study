# 23th_study

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [주사위 윷놀이](https://www.acmicpc.net/problem/17825)

### [민웅](./주사위%20윷놀이/민웅.py)

```py


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

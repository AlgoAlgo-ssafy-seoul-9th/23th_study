from copy import deepcopy
def play(n, score, horse):
    global max_score
    if n == 10: # 주사위 다썼으면
        if score > max_score:
            max_score = score
        return
    # 4개의 말 완전탐색
    for h in range(4):
        # 도착한거 체크를 -1로 할건데, 도착안했으면 움직여
        if horse[h][0] != -1:
            tmp = deepcopy(horse)
            tmp[h][0] += dice[n] #주사위만큼 이동

            # 파란칸인지 확인
            if tmp[h][1] == 0:
                if tmp[h][0] == 5: #점수가 10인 지점에
                    tmp[h][1] = 1
                    tmp[h][0] = 0
                elif tmp[h][0] == 10: #점수가 20인 지점에
                    tmp[h][1] = 2
                    tmp[h][0] = 0
                elif tmp[h][0] == 15: #점수가 30인 지점에
                    tmp[h][1] = 3
                    tmp[h][0] = 0
        # 도착했는지 체크
            if tmp[h][0] >= len(road[tmp[h][1]]):
                tmp[h][0] = -1
                play(n+1, score, tmp)
            else:
                # 이동하려는 곳에 말이 있다면 이동 XXXX
                flag = False
                # 지금 움직일 말이 있는 점수
                visit = road[tmp[h][1]][tmp[h][0]]
                for v in range(len(tmp)):
                    if tmp[v][0] == -1:
                        continue
                    if v != h and visit == road[tmp[v][1]][tmp[v][0]]:
                        if visit == 30: # 30의 경우 road에 여러개가 있기 때문에 같은 위치인지 확인해야함
                            if tmp[h] == [0,3] and tmp[v] == [0,3]:
                                flag = True
                                break
                            elif tmp[h] != [0,3] and tmp[v] != [0,3]:
                                flag = True
                                break
                        elif visit in [16, 22, 24, 26, 28]:
                            if tmp[h] == tmp[v]:
                                flag = True
                                break
                        else:
                            flag = True
                            break
                # 이동할 칸에 다른말 있다는 뜻
                if flag == True:
                    continue
                play(n+1, score+road[tmp[h][1]][tmp[h][0]],tmp)


road = [
    [i * 2 for i in range(21)],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]
]

max_score = 0

# 말의 위치
horse = [[0, 0] for _ in range(4)]

dice = list(map(int, input().split()))
play(0, 0, horse) # 모든 경우의 윷놀이를 진행할 함수
print(max_score)
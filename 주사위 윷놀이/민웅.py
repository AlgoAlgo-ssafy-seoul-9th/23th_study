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
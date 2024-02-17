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
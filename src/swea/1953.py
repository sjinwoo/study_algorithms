def check_connection(curr_path, next_tunnel):
    if curr_path % 2 == 0:
        return (curr_path + 1) in next_tunnel
    else:
        return (curr_path - 1) in next_tunnel

def validate_range(y, x):
    global N, M

    return 0 <= y < N and 0 <= x < M

def bfs(r, c):
    global TUNNEL, MOVE, UNDER_GROUND, N, M, L
 
    # 시작점 queue에 넣고 방문할 좌표가 없을 때 까지 반복
    visited = [[0] * M for _ in range(N)]
    result = 1
    
    visited[r][c] = 1
    queue = [(r, c)]
    
    while queue != []:
        if L == 1: break
        for _ in range(len(queue)):
            # 방문할 좌표 꺼내기
            curr_y, curr_x = queue.pop(0)
            
            # 현재 좌표에서 터널 유형에 따라 상, 하, 좌, 우 순회
            for m in TUNNEL[UNDER_GROUND[curr_y][curr_x]]:
                _X, _Y = MOVE[m]
                next_x = curr_x + _X
                next_y = curr_y + _Y

                # 유효하지 않은 범위나, 연결된 다음 터널이 없다면 pass
                if not validate_range(next_y, next_x) or UNDER_GROUND[next_y][next_x] == 0: 
                    continue
                
                # 방문한적 없고, 다음 좌표가 올바르게 연결된 터널이라면 Queue에 넣어서 다음에 방문. visited = 1
                if visited[next_y][next_x] == 0 and check_connection(m, TUNNEL[UNDER_GROUND[next_y][next_x]]):
                    visited[next_y][next_x] = 1
                    queue.append((next_y, next_x))
                    result += 1
        L -= 1

    return result

if __name__ == "__main__":
    TUNNEL = [
        (),
        (0, 1, 2, 3), 
        (0, 1), 
        (2, 3),
        (0, 3), 
        (1, 3), 
        (1, 2),
        (0, 2)
    ]
    #         상       하       좌      우
    MOVE = [(0, -1), (0, 1), (-1, 0), (1, 0)]


    T = int(input())

    result_list = []
    for idx in range(1, T+1):
        N, M, R, C, L = map(int, input().split())

        UNDER_GROUND = []
        for _ in range(N):
            UNDER_GROUND.append(list(map(int, input().split())))

        result = bfs(R, C)
        result_list.append(result)

    for idx, res in enumerate(result_list, start=1):
        print(f"#{idx} {res}")
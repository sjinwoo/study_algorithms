def validate_range(y, x) -> bool:
    global N

    return 0 <= y < N and 0 <= x < N

def find_max_height() -> int:
    global GROUND

    return max(map(max, GROUND))

def dfs(y, x):
    global X, Y, N, K, GROUND, VISITED, result, is_cut

    for i in range(4):
        next_y = y + Y[i]
        next_x = x + X[i]

        if not validate_range(next_y, next_x): 
            continue
        
        # 다음 값이 현재 값보다 작고, 방문한 적 없다면 -> DFS
        if  GROUND[next_y][next_x] < GROUND[y][x] and not VISITED[next_y][next_x]:
            VISITED[next_y][next_x] = VISITED[y][x] + 1
            dfs(next_y, next_x)
            if VISITED[next_y][next_x] > result:
                result = VISITED[next_y][next_x]
            VISITED[next_y][next_x] = 0

        # 다음 값이 현재 값보다 크거나 같고, 방문한 적이 없으며 자를 수 있다면
        elif GROUND[next_y][next_x] >= GROUND[y][x] and VISITED[next_y][next_x] == 0 and not is_cut:
            for k in range(1, K+1):
                cutted_height = GROUND[next_y][next_x] - k
                if cutted_height < GROUND[y][x]:
                    GROUND[next_y][next_x] = cutted_height
                    is_cut = True
                    VISITED[next_y][next_x] = VISITED[y][x] + 1
                    dfs(next_y, next_x)

                    # 최대값 갱신
                    if VISITED[next_y][next_x] > result:
                        result = VISITED[next_y][next_x]

                    # 방문 기록 및 깎은 것 원복
                    VISITED[next_y][next_x] = 0
                    is_cut = False
                    GROUND[next_y][next_x] += k
                    

if __name__ == "__main__":
    #    상, 하, 좌, 우
    X = (0, 0, -1, 1)
    Y = (-1, 1, 0, 0)

    T = int(input())

    result_list = []
    for idx in range(1, T+1):
        N, K = map(int, input().split())
        GROUND = []
        for _ in range(N):
            GROUND.append(list(map(int, input().split())))

        result = 0
        is_cut = False
        start_point = []
        max_h = find_max_height()

        for y in range(N):
            for x in range(N):
                if GROUND[y][x] == max_h:
                    start_point.append((y, x))

        for y, x in start_point:
            VISITED = [[0] * N for _ in range(N)]
            VISITED[y][x] = 1
            dfs(y, x)

        result_list.append(result)

    for idx, res in enumerate(result_list, start=1):
        print(f"#{idx} {res}")
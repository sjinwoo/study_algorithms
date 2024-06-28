import sys
import itertools
import copy

def validate_range(x, y):
    """좌표 값이 유효한 범위 내인지 확인"""
    global N
    return 0 < y <= N and 0 < x <= N

def check_near_max(ground, curr_x, curr_y):
    """현재 좌표에서 인접한 칸 중 가장 높은 값을 가진 좌표를 반환"""
    #   상  하  좌  우
    X = ( 0, 0, -1, 1)
    Y = (-1, 1,  0, 0)

    max_value = 0
    max_x = 0
    max_y = 0
    for dx, dy in zip(X, Y):
        next_x = curr_x + dx
        next_y = curr_y + dy
        if validate_range(next_x, next_y) and max_value < ground[next_x-1][next_y-1]:
            max_value = ground[next_x-1][next_y-1]
            max_x = next_x
            max_y = next_y

    ground[max_x-1][max_y-1] = 0
    return max_value, max_x, max_y

def harvest(ground, coord):
    result = 0

    # 1, 2, 3초에 수확
    for _ in range(3):
        for idx, (x, y) in enumerate(coord):
            next_value, next_x, next_y = check_near_max(ground, x, y)
            result += next_value
            coord[idx] = [next_x, next_y]

    return result

if __name__ == "__main__":
    # 길이가 N인 정사각형에 M명이 열매 수확
    N, M = map(int, sys.stdin.readline().split())

    GROUND = []
    for _ in range(N):
        GROUND.append(list(map(int, sys.stdin.readline().split())))

    # 초기 위치
    COORD = []
    for _ in range(M):
        COORD.append(list(map(int, sys.stdin.readline().split())))

    results = []
    for perm in list(itertools.permutations(COORD, M)):
        ground = copy.deepcopy(GROUND)
        # 0초에 수확
        _result = 0
        for x, y in perm:
            _result += ground[x-1][y-1]
            ground[x-1][y-1] = 0
        results.append(_result + harvest(GROUND, list(perm)))

    print(max(results))
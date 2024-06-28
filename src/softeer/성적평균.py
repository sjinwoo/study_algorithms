import sys

def calc_avg(idx, score):
    return round(sum(score[idx[0]-1: idx[1]]) / (idx[1] - idx[0] + 1), 2)


if __name__ == "__main__":
    IDX_SAMPLE = []

    N, K = map(int, sys.stdin.readline().split())
    SCORE = list(map(int, sys.stdin.readline().split()))
    for _ in range(K):
        IDX_SAMPLE.append(tuple(map(int, sys.stdin.readline().split())))
    
    for idxs in IDX_SAMPLE:
        _avg = calc_avg(idxs, SCORE)
        print(f"{_avg:.2f}")
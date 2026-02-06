# 0 왼쪽 / 1 오른쪽 / 2 위
dr = [0, 0, -1]
dc = [-1, 1, 0]

t = int(input())
for tc in range(1, 11):
    arr = [list(map(int, input().split())) for _ in range(100)]
    target = 2
    r = c = 0

    for i in range(100):
        for j in range(100):
            if arr[i][j] == target:
                r = i
                c = j

    while r > 0:
        if 0 < c < 99:
            if arr[r][c-1] == 0 and arr[r][c+1] == 0:
                r -= 1
            elif arr[r][c-1] == 1:
                c -= 1
            elif arr[r][c+1] == 1:
                c += 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail_number = [[0] * N for _ in range(N)]

    r = c = 0
    dir = 0

    for number in range(1, N*N+1):
        snail_number[r][c] = number

        # nr, nc = 임시 r, c
        nr = r+dr[dir]
        nc = c+dc[dir]
        # 숫자 검사를 위한 인덱싱 전에 인덱스에 대한 범위 검사 필요
        if nr < 0 or nr >= N or nc < 0 or nc >= N or snail_number[nr][nc] != 0:
            dir = (dir+1) % 4

        r += dr[dir]
        c += dc[dir]


    print(f'#{tc}')
    for i in range(N):
        print(*snail_number[i])    
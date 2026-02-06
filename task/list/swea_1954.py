# 0 오른쪽 / 1 아래 / 2 왼쪽 / 3 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    snail_number = [[0] * N for _ in range(N)]

    counts = [N]

    for i in range(N-1, 0, -1):
        counts.append(i)
        counts.append(i)

    r = c = 0
    dir = 0
    number = 1
    # count > 현재 방향으로 찍어줄 횟수
    for count in counts:

        # count만큼 이동하면서 숫자를 찍기
        for _ in range(count):
            # 1. 숫자 찍기
            snail_number[r][c] = number
            number += 1

            # 2. 이동
            r += dr[dir]
            c += dc[dir]

        r -= dr[dir]
        c -= dr[dir]

        dir = (dir + 1) % 4  # 대신
        # if dir <= 2:
        #     dir += 1
        # else:
        #     dir = 0

        r += dr[dir]
        r += dc[dir]
        
    print(f'#{tc}')
    for i in range(N):
        print(*snail_number)  # 대신
        # for j in range(N):
        #     print(snail_number[i][j], end = " ")
        # print()

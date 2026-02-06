T = 10

for tc in range(1, T+1):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    c = ladder[99].index(2)
    dir = 0

    while r > 0:

        # 1. 왼쪽이 뚫려있으면
        while c-1 >= 0 and ladder[r][c-1]:  # == 1 (True) 생략
            c -= 1
            dir = 1  # 이게 왜 필요했던건지 기억 안남
        if dir == 1:
            r -= 1  # 왼쪽이 막혀서 while에서 나왔을 때, 왔던 길을 다시 되돌아가는(오른쪽으로) 일을 막기 위함
            dir = 0
            continue


        # 2. 오른쪽이 뚫려있으면
        while c+1 < 100 and ladder[r][c+1]:
            c += 1
            dir = 2
        if dir == 2:
            r -= 1
            dir = 0
            continue

        # 3. 좌우가 막혀있으면
        r -= 1

    print(f'{tc} {c}')
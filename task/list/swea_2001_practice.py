T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0

    for r in range(0, N-M+1):
        for c in range(0, N-M+1):
            sum = 0
            for i in range(M):
                for j in range(M):
                    sum += arr[r+i][c+j]

                if sum > max_sum:
                    max_sum = sum

    print(f'#{tc} {max_sum}')
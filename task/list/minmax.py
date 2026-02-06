T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_num = 0
    min_num = 0

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    min_num = arr[0]
    max_num = arr[N-1]

    print(f'#{tc} {max_num - min_num}')
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for _ in range(N):
        max_num = float('-inf')
        min_num = float('inf')
        max_idx = 0
        min_idx = 0

        for i in range(100):
            if arr[i] > max_num:
                max_num = arr[i]
                max_idx = i
            if arr[i] < min_num:
                min_num = arr[i]
                min_idx = i
        if (max_num - min_num) >= 2:
            arr[max_idx] -= 1
            arr[min_idx] += 1
        else:
            break

    max_num = float('-inf')
    min_num = float('inf')
    for i in range(100):
        if arr[i] > max_num:
            max_num = arr[i]
        if arr[i] < min_num:
            min_num = arr[i]

    print(f'#{tc} {max_num - min_num}')
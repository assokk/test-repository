T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    count = [0] * 10
    max_count = 0

    for num in A:
        if num not in B:
            B.append(num)
        count[num] += 1
        
    for count_num in count:
        if count_num > max_count:
            max_count = count_num


    print(f'{tc} {max_count}')
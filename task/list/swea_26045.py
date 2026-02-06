T = int(input())

for tc in range(1, T+1):
    answer = 'NO'

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B_idx = 0

    # YES인 상황
    for number in A:
        if B[B_idx] == number:
            B_idx += 1 
            if B_idx >= M:  # idx가 증가할 때만 검사해주는게 효율적이니까 이 위치에 오는게 좋음
                break      
    
    if B_idx == M:
        answer = 'YES'

    print(f'{tc} {answer}')
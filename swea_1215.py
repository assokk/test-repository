for tc in range(1, 11):
    N = int(input())
    txt = [input() for _ in range(8)]
    count = 0

    for r in range(8):
        for c in range(8-N+1):
            total = 0
            for k in range(N//2):
                if txt[r][c+k] != txt[r][c+N-1-k]:
                    break
            else:
                total += 1

            if total == 1:
                count += 1
    
    for c in range(8):
        for r in range(8-N+1):
            total = 0
            for k in range(N//2):
                if txt[r+k][c] != txt[r+N-1-k][c]:
                    break
            else:
                total += 1

            if total == 1:
                count += 1

    print(f'#{tc} {count}')
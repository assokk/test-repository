T = int(input())

for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    result = 0
    a_count = 0
    b_count = 0

    def binary_search(p, s):
        start = 1
        end = p
        count = 0
        while start <= end:
            count += 1
            middle = (start + end) // 2
            if middle == s:
                return count
            elif middle > s:
                end = middle
            else:
                start = middle
        return count
    
    a_count = binary_search(P, A)
    b_count = binary_search(P, B)

    if a_count > b_count:
        result = 'B'
    elif a_count < b_count:
        result = 'A'

    print(f'#{tc} {result}')
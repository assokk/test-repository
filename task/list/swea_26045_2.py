T = int(input())

for tc in range(1, T+1):
    answer = 'YES'

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    for number in B:
        if number not in A:
            answer = 'NO'
            break
        
        # 여기까지 내려왔다는건 break에 안걸렸다는 뜻이므로 else를 작성하지 않아도 같은 의미를 가짐
        idx = A.index(number)
        A = A[idx+1:]

    print(f'{tc} {answer}')
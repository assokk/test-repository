# 3_String > pattern.py

def pattern_count(p, t):    # 패턴의 등장 횟수 리턴
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:  # 같으면        , else 생략 시 교재의 코드가 됨
            i += 1
            j += 1
        if j==M:     # 패턴을 찾은 경우
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt


T = int(input())
for tc in range(1, T+1):
    A, B = input().split()
    print(A, B)
    cnt = pattern_count(B, A)
    print(cnt)


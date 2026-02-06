# 34p
N = int(input())
text = [list(input()) for _ in range(N)]
ans = 'NO'

for i in range(N):
    for j in range(N):
        if text[i][j] == 'Z':
            ans = 'YES'
            break

print(ans)


# 35p
N = int(input())
arr = [list(input()) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if text[i][j] == '#':
            cnt += 1

print(cnt)


# 36p
N = int(input())
text = [input() for _ in range(N)]
pat = ['AB']['CD']
ans = 'NO'

for i in range(N-1):
    for j in range(N-1):
        cnt = 0
        for p in range(2):      # 패턴 내부 인덱스
            for q in range(2):
                if text[i+q][j+q] == pat[p][q]:
                    cnt += 1
        if cnt == 4:
            ans = 'YES'


# 37p


T = int(input())

for tc in range(1, T+1):
    tn, len = input().split()
    N = int(len)
    nums = list(input().split())

    print()
    print(f'#{tc}')

    count = 0
    nums_dict = {
        "ZRO": 0,
        "ONE": 0,
        "TWO": 0,
        "THR": 0,
        "FOR": 0,
        "FIV": 0,
        "SIX": 0,
        "SVN": 0,
        "EGT": 0,
        "NIN": 0
    }

    for num in nums:
        nums_dict[num] += 1

    result = []

    for key, value in nums_dict.items():
        for i in range(value):
            print(key, end=' ')
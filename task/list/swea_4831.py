T = int(input())

for tc in range(1, T+1):
    answer = 0
    K, N, M = map(int, input().split())
    bus_stops = [0] + list(map(int, input().split()))
    # 출발 위치가 0번이므로 더미 데이터 삽입

    cur_pos = stop_idx = 0  # current position

    # 반복 횟수를 알 수 없으므로 while문 사용
    while cur_pos + K < N:

        for i in range(M, stop_idx, -1):
            if bus_stops[i] <= cur_pos + K:
                stop_idx = i
                cur_pos = bus_stops[i]
                answer += 1
                break
        # 다음 충전소를 못 찾았을 때
        else:
            answer = 0
            break

    print(f'#{tc} {answer}')


    # while cur_pos < N:

    #     for i in range(M, stop_idx, -1):
    #         if bus_stops[i] <= cur_pos + K:
    #             stop_idx = i
    #             cur_pos = bus_stops[i]
    #             answer += 1
    #             break
    #     # 다음 충전소를 못 찾았을 때
    #     else:
    #         answer = 0
    #         break

    #     # 뛰었는데 종점 지났을 때
    #     if cur_pos + K >= N:
    #         break
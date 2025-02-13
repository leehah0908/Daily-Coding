N = int(input())
M = int(input())

vip_seat_array = []
for i in range(M):
    vip_seat_array.append(int(input()))

memo = {0:1, 1:1, 2:2}

def fibo(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    
    nth_fibo = fibo(n-1, fibo_memo) + fibo(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    cur_idx = 1
    result = 1

    for i in fixed_seat_array:
        prev_period = i - cur_idx
        result *= fibo(prev_period, memo)
        cur_idx = i + 1

    last_period = total_count - cur_idx + 1
    result *= fibo(last_period, memo)
    return result

print(get_all_ways_of_theater_seat(N, vip_seat_array))
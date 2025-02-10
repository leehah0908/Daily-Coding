import itertools

def solution(numbers, target):
    answer = 0
    plus_mius_list = list(itertools.product([False, True], repeat=len(numbers)))

    for i in plus_mius_list:
        cur_value = 0
        for j in range(len(i)):
            if i[j]:
                cur_value += numbers[j]
            else:
                cur_value -= numbers[j]
        if cur_value == target:
            answer += 1
    return answer
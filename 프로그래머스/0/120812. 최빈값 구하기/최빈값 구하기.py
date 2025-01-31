def solution(array):
    list = [0] * 1000
    
    for i in array:
        list[i] += 1
    
    max_count = max(list)
    
    count = 0
    max_value = -1
    for i in range(len(list)):
        if list[i] == max_count:
            count += 1
            max_value = i
    
    if count > 1:
        return -1
    else:
        return max_value
def solution(a, b):
    week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    sum = 0
    
    if a != 1:
        for i in range(1, a):
            if i in [1,3,5,7,8,10,12]:
                sum += 31
            elif i in [4,6,9,11]:
                sum += 30
            elif i == 2:
                sum += 29
    sum += b
    idx = sum % 7
    answer = week[idx]
    return answer

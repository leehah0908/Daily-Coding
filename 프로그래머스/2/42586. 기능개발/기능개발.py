from collections import deque

def solution(progresses, speeds):
    pr = deque(progresses)
    sp = deque(speeds)
    
    answer = []
    
    while pr:
        count = 0
        if pr[0] < 100:
            for i in range(len(sp)):
                pr[i] += sp[i]
        else:
            while pr and pr[0] >= 100:
                count += 1
                pr.popleft()
                sp.popleft()
            answer.append(count)
        
    return answer
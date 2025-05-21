def solution(participant, completion):
    part_dict = {}
    
    for i in participant:
        if i not in part_dict:
            part_dict[i] = 1
        else:
            part_dict[i] += 1
            
    for j in completion:
        part_dict[j] -= 1
            
    for key, value in part_dict.items():
        if value == 1:
            return key
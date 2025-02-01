S = list(map(int, input()))

check_num = S[0]
count = 0
for idx in range(1, len(S)):
    if S[idx] != check_num:
        if S[idx] != S[0]:
            check_num = S[idx]
            count += 1
        else:
            check_num = S[idx]
        
print(count)
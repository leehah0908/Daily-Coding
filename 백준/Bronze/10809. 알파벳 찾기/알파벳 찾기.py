S = list(input())

alphabet_list = [-1] * 26

for idx in range(len(S)):
    if alphabet_list[ord(S[idx]) - ord('a')] == -1:
        alphabet_list[ord(S[idx]) - ord('a')] = idx

for i in alphabet_list:
    print(i, end = " ")

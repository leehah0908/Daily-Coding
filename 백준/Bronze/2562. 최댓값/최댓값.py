import sys
input = lambda: sys.stdin.readline().rstrip()
list = []

for i in range(9):
    list.append(int(input()))

max_value = 0
max_idx = 0

for idx in range(len(list)):
    if list[idx] > max_value:
        max_value = list[idx]
        max_idx = idx

print(max_value)
print(max_idx + 1)

n, k = map(int, input().split())

result = "<"
list = [i for i in range(1, n+1)]
delete_idx = k-1
    
while list:
    delete = list.pop(delete_idx)
    result = result + str(delete) + ", "

    if len(list) != 0:
        delete_idx = (delete_idx + (k - 1)) % len(list)

print(result[:-1][:-1] + ">" )
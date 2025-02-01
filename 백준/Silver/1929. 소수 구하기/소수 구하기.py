M, N = map(int, input().split())

prime = [True] * (N + 1)
prime[0], prime[1] = False, False

p = 2
while p * p <= N:
    if prime[p] == True:
        for i in range(p * p, N + 1, p):
            prime[i] = False
    p += 1

for number in range(M, N + 1):
    if prime[number]:
        print(number)
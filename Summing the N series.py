T = int(input())

for i in range(T):
    n = int(input())
    S = n**2
    print(S%(10**9 + 7))

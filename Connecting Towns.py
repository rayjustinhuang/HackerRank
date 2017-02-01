from functools import reduce

T = int(input())

for i in range(T):
    N = int(input())
    Ni = str(input()).split()
    Ni = [int(j) for j in Ni]
    print(reduce(lambda x, y: x*y, Ni)%1234567)
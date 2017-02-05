params = input().split(" ")
L, S1, S2 = [float(x) for x in params]

Q = int(input())

for i in range(Q):
    initialdistance = L*2**0.5
    q = float(input())
    finaldistance = q**0.5*2**0.5
    speed = abs(S2 - S1)
    time = (initialdistance - finaldistance)/speed
    print(time)
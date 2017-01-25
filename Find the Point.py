numberoflines = input()
datalist = [i for i in range(int(numberoflines))]

for i in range(int(numberoflines)):
    datalist[i] = input().split(" ")

# print(datalist)

for i in range(int(numberoflines)):
    x1, y1, x2, y2 = datalist[i]
    p = [int(x1), int(y1)]
    q = [int(x2), int(y2)]
    r = [str(2*j - i) for j, i in zip(q, p)]
    print(r[0] + " " + r[1])

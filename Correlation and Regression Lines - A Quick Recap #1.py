PhysicsScores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
HistoryScores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
XY = [x*y for x,y in zip(PhysicsScores, HistoryScores)]
X2 = [x**2 for x in PhysicsScores]
Y2 = [y**2 for y in HistoryScores]

sumX = sum(PhysicsScores)
sumY = sum(HistoryScores)
sumXY = sum(XY)
sumX2 = sum(X2)
sumY2 = sum(Y2)
n = len(PhysicsScores)

r = (n*sumXY - sumX*sumY)/(((n*sumX2-sumX**2)**0.5)*(n*sumY2-sumY**2)**0.5)
print(r)
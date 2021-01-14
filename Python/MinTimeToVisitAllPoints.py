def minTimeToVisitAllPoints(points):
    steps = 0
    for i in range(0, len(points)-1, 1):
        current = points[i]
        des = points[i + 1]
        while current != des:
            if current[0] != des[0] and current[1] != des[1]:
                if current[0] > des[0] and current[1] > des[1]:
                    current[0] -= 1
                    current[1] -= 1
                    steps += 1
                if current[0] < des[0] and current[1] < des[1]:
                    current[0] += 1
                    current[1] += 1
                    steps += 1
            elif current[0] == des[0] and current[1] != des[1]:
                if current[1] > des[1]:
                    current[1] -= 1
                    steps += 1
                if current[1] < des[1]:
                    current[1] += 1
                    steps += 1
            elif current[0] != des[0] and current[1] == des[1]:
                if current[0] > des[0]:
                    current[0] -= 1
                    steps += 1
                if current[0] < des[0]:
                    current[0] += 1
                    steps += 1
    return steps


points = [[1,1],[3,4],[-1,0]]
out = minTimeToVisitAllPoints(points)
print(out)

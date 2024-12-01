lines = open("input/day1.txt").readlines()

left = []
right = []
for x in lines:
    components = x.split()
    left.append(int(components[0]))
    right.append(int(components[1]))

left.sort()
right.sort()
partOne = 0
partTwo = 0
for i in range(len(left)):
    partOne += abs(right[i] - left[i])
    partTwo += left[i] * right.count(left[i])

print("Part One:", partOne)
print("Part Two:", partTwo)
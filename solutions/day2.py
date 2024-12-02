# We could do more complicated things to workout *exactly* which is at fault, but we can just brute force it with the 4 possible fault points.
# This is because the input is small enough that it doesn't matter.
# Cases to consider include the broken index and the one following this. As well as the first index since this can be used to define the initial order. (Last index is accounted for already in the +1 part)
def reRunAppropriateValidations(values, i):
    return isLineValid(values[0:i] + values[i+1:len(values)]) or isLineValid(values[0:i+1] + values[i+2:len(values)]) or isLineValid(values[1:])

def isLineValid(values, partTwo=False):
    decrease = values[0] - values[1] > 0
    for i in range(0, len(values) - 1):
        diff = values[i] - values[i + 1]
        if (diff > 0 and decrease == False) or (diff < 0 and decrease == True):
            return reRunAppropriateValidations(values, i) if partTwo else False
        if abs(diff) < 1 or abs(diff) > 3:
            return reRunAppropriateValidations(values, i) if partTwo else False
    return True

lines = open("input/day2.txt").readlines()
partOne = 0
partTwo = 0
for line in lines:
    values = list(map(int, line.split()))
    if isLineValid(values):
        partOne += 1
        partTwo += 1
    elif isLineValid(values, True):
        partTwo += 1

print("Part One:", partOne)
print("Part Two:", partTwo)
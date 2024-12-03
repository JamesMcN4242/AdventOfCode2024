import re

def runFunction(cont, output):
    found = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", cont)
    found = list(map(lambda x: x.replace("mul(", "").replace(")", "").split(","), found))
    print(output, sum(map(lambda x: int(x[0]) * int(x[1]), found)))

fileContents = open("input/day3.txt").read()
runFunction(fileContents, "Part One:")

brokenDownSections = fileContents.split("don't()")
partTwoInput = brokenDownSections[0]
for section in brokenDownSections[1:]:
    doIndex = section.find("do()")
    if doIndex != -1:
        partTwoInput += section[doIndex + 4:]

runFunction(partTwoInput, "Part Two:")
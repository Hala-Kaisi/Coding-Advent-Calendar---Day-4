lines = open("D4_Input.txt").readlines()
sharedSections = 0


for line in lines:
    strippedLine = line.strip()
    pairs = strippedLine.split(',')
    firstSection = pairs[0].split('-')
    secondSection = pairs[1].split('-')
    firstSet = set()
    secondSet = set()
    for i in range(int(firstSection[0]), int(firstSection[1])+1):
        firstSet.add(i)
    for i in range(int(secondSection[0]), int(secondSection[1])+1):
        secondSet.add(i)
    Intersection = firstSet.intersection(secondSet)
    print(firstSection)
    print(secondSection)
    print(Intersection)
    if len(list(Intersection)) > 0:
        sharedSections += 1
    print('\n')
    

print('Shared Assignments: ' + str(sharedSections))
    
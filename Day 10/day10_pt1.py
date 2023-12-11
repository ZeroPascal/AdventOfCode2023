import time
startTime = time.time()
input = open("input.txt", "r").readlines()

cleanInput = []
for line in input:
    line =line.strip()
    l = []
    for c in line:
        l.append(c)
    cleanInput.append(l)

print(cleanInput[0])

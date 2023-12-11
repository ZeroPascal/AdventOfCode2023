import time
startTime = time.time()
input = open("input.txt", "r").readlines()


values=[]
#Process and clean input
for line in input:
    l=[]
    for i in line.strip().split(' '):
        l.append(int(i))
    values.append(l)



def findNextValue(value):
    nextArray=[]
    isZeros= True
    for i in range(len(value)-1):
        nextValue=value[i+1]-value[i]
        if(nextValue !=0):
            isZeros= False
        nextArray.append(nextValue)
    if isZeros:
        return None
    return nextArray

def processLine(line):
    calculatedLines=[]
    while line:
        calculatedLines.append(line)
        line = findNextValue(line)
        
    return calculatedLines

def findLineAnswer(calculatedLines:[]):
    calculatedLines.reverse()
  #  print(calculatedLines[0])
    nextValue=calculatedLines[0][len(calculatedLines[0])-1]
    for line in calculatedLines[1:]:
        nextValue = line[len(line)-1]+nextValue     
    return nextValue

total=0
for lines in values:
   calculatedLines= processLine(lines) 
   total+=findLineAnswer(calculatedLines)
    
print(total)
#print(findLineAnswer(processLine(values[0])))
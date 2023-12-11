import time
startTime = time.time()
input = open("input.txt", "r").readlines()

steps = input[0].strip()
nodes = {}

currentNodes=[]
for line in input[2:]:
    line=line.split('=')
    node = line[0].strip()
    lr= line[1].strip().split(',')
    lr[0]=lr[0].replace('(','').strip()
    lr[1]=lr[1].replace(')','').strip()
    nodes[node]={'L':lr[0],'R':lr[1]}
    if(node[2]=='A'):
        currentNodes.append(node)

def checkCurrentNodes(startingNodes):
    for n in startingNodes:
        if(n[2]!='Z'):
            return False
    return True

#Single Brute
totalStepsPerNode=[]
endNodes =[]
for node in currentNodes:
    totalSteps=0
    step = 0
    while not checkCurrentNodes([node]) and step < len(steps):
        totalSteps+=1
        node= nodes[node][steps[step]]
        if(step+1==len(steps)):
            step=0
        else:
            step+=1
 
    endNodes.append(node)
    totalStepsPerNode.append(totalSteps)

       
sum=None

for step in totalStepsPerNode:
    if not sum:
        sum=step
    else:
        sum*=step/len(steps)
 
print(round(sum))
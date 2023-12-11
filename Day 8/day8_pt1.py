import time
startTime = time.time()
input = open("input.txt", "r").readlines()

steps = input[0].strip()

nodes = {}

currentNode= None
for line in input[2:]:
    line=line.split('=')
    node = line[0].strip()
    lr= line[1].strip().split(',')
    lr[0]=lr[0].replace('(','').strip()
    lr[1]=lr[1].replace(')','').strip()
    nodes[node]={'L':lr[0],'R':lr[1]}
   
currentNode='AAA'

step = 0
totalSteps= 0
while currentNode != 'ZZZ' and step < len(steps):
    totalSteps+=1
    currentNode= nodes[currentNode][steps[step]]
    if(step+1==len(steps)):
        step=0
       
    else:
        step+=1

print(totalSteps)


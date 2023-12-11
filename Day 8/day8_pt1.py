import time
startTime = time.time()
input = open("input.txt", "r").readlines()

steps = input[0].strip()

print(steps)
nodes = {}

currentNode= None
for line in input[2:]:
    line=line.split('=')
    node = line[0].strip()
    lr= line[1].strip().split(',')
    lr[0]=lr[0].replace('(','').strip()
    lr[1]=lr[1].replace(')','').strip()
    nodes[node]={'L':lr[0],'R':lr[1]}
    if(not currentNode):
        currentNode=node

def nextNode(node,direction):
    print(node,direction[0])
    return node[direction]

#print('Steps',steps)
#print('Nodes',nodes)
print('Current Node',currentNode)
#for node in nodes:
   # print(nextNode(node,'L'))
 #   node['LL']=nodes[nextNode(nodes[nextNode(node,'L')],'L')]

print(nodes)
step = 0
totalSteps= 0
while currentNode != 'ZZZ' and step < len(steps):
    totalSteps+=1
   # print('..',currentNode,'->',steps[step],nodes[currentNode][steps[step]])
 #   print(nodes[currentNode])
    currentNode= nodes[currentNode][steps[step]]#nextNode(nodes[currentNode],[steps[step]])
    if(step+1==len(steps)):
        step=0
        print(currentNode,totalSteps)
    else:
        step+=1

print(totalSteps,currentNode)


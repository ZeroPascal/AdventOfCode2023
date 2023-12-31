import time
startTime = time.time()
input = open("input.txt", "r").readlines()

cleanInput = []
for line in input:
    line =line.strip()
    l = []
    for c in line:
        l.append({'c':c,'nC':0})
    cleanInput.append(l)

#checks to see if surrounding symbol is appropraite.
def checkNorth(c):
    return c['c'] in ['7','F','|','S']
def checkSouth(c):
    return c['c'] in ['L','J','|','S']
def checkEast(c):
    return c['c'] in ['J','7','-','S']
def checkWest(c):
    return c['c'] in ['F','L','-','S']

start=[]
#Map intinal connections
for i in range(len(cleanInput)):
    line = cleanInput[i]
    for n in range(len(line)):
        connections=0
    
        match line[n]['c']:
            case '|':
                if(i>0 and checkNorth(cleanInput[i-1][n])):
                    connections+=1
                if(i<len(cleanInput)-1 and checkSouth(cleanInput[i+1][n])):
                    connections+=1
            case '-':
                if(n<len(line)-1 and checkEast(line[n+1])):
                    connections+=1
                if(n>0 and checkWest(line[n-1])):
                    connections+=1
            case 'L':
                if(i>0 and checkNorth(cleanInput[i-1][n])):
                    connections+=1
                if(n<len(line)-1 and checkEast(line[n+1])):
                    connections+=1
            case 'J':
                if(i>0 and checkNorth(cleanInput[i-1][n])):
                    connections+=1
                if(n>0 and checkWest(line[n-1])):
                    connections+=1
            case '7':
                if(i<len(cleanInput)-1 and checkSouth(cleanInput[i+1][n])):
                    connections+=1
                if(n>0 and checkWest(line[n-1])):
                    connections+=1
            case 'F':
                if(i<len(cleanInput)-1 and checkSouth(cleanInput[i+1][n])):
                    connections+=1
                if(n<len(line)-1 and checkEast(line[n+1])):
                    connections+=1
            case 'S':
                if(i<len(cleanInput)-1 and checkSouth(cleanInput[i+1][n])):
                    connections+=1
                if(n>0 and checkWest(line[n-1])):
                    connections+=1
                if(i>0 and checkNorth(cleanInput[i-1][n])):
                    connections+=1
                if(n<len(line)-1 and checkEast(line[n+1])):
                    connections+=1
                start=[i,n]


        cleanInput[i][n]['nC']=connections
                        
def plotConnections(lines):                    
    a=''
    for line in lines:
        for l in line:
            a+=str(l['nC'])
        print(a)
        a=''

def plotChars(lines):
    a=''
    for line in lines:
        for l in line:
            a+=str(l['c'])
        print(a)
        a=''

#plotConnections(cleanInput)
#print(start, list(cleanInput[start[0]])[start[1]])
startY= start[0]
startX = start[1]

path= []
path.append(start)
firstLoop= True 
lastWent='' #Keeps the trace from going backwards
while (start[1]!= startX or start[0] != startY) or firstLoop:
   
    firstLoop= False
    currentChar = cleanInput[startY][startX]['c']
  
    #North
    if(lastWent !='South' and startY>0 and currentChar in ['S','|','J','L'] and checkNorth(cleanInput[startY-1][startX]) and cleanInput[startY-1][startX]['nC']==2):
            startY=startY-1
            lastWent='North'
            path.append([startY,startX])
    #South
    elif(lastWent !='North' and startY<len(cleanInput)-1 and currentChar in ['S','|','F','7'] and checkSouth(cleanInput[startY+1][startX]) and cleanInput[startY+1][startX]['nC']==2):
            lastWent='South'
            startY=startY+1
            path.append([startY,startX])
    #West
    elif(lastWent !='East' and startX>0 and currentChar in ['S','-','7','J'] and checkWest(cleanInput[startY][startX-1]) and cleanInput[startY][startX-1]['nC']==2):
            startX=startX-1
            lastWent='West'
            path.append([startY,startX])

    elif(lastWent !='West' and startX<len(cleanInput[0])-1 and currentChar in ['S','-','F','L'] and checkEast(cleanInput[startY][startX+1]) and cleanInput[startY][startX+1]['nC']==2):
            startX=startX+1
            lastWent='East'
            path.append([startY,startX])
    else:
        print('Bad Path')
        break

def plotPath(path, mainMap):
    grid=[]
    for i in range(len(mainMap)):
        l = []
        for n in range(len(mainMap[0])):
            l.append(".")
        grid.append(l)
    for p in path:
       # print('p',p)
        grid[p[0]][p[1]]=mainMap[p[0]][p[1]]['c']
    a=''
    for line in grid:
        for l in line:
            a+=l
        print(a)
        a=''

#plotPath(path, cleanInput)
#print(len(path))

#-2 Removes both instances of start, odd even because math hard.
if(len(path)%2==0):
    print((len(path)-2)//2)
else:
    print((len(path)-2)//2+1)
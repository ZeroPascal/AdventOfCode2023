import time
startTime = time.time()
input = open("inputTest.txt", "r").readlines()

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

def updateMap(path, mainMap):
    grid=[]
    for i in range(len(mainMap)):
        l = []
        for n in range(len(mainMap[0])):
            l.append(".")
        grid.append(l)
    for p in path:
       # print('p',p)
        grid[p[0]][p[1]]=mainMap[p[0]][p[1]]['c']
    return grid

#plotPath(path, cleanInput)
#print(len(path))

updatedGrid = updateMap(path,cleanInput)

def checkSides(y,x,grid):

    if (grid[y][x] in ['X','Z','<','>','^','V','*','S']):
            if(grid[y][x] not in ['>','<']):
                if(y>0 and grid[y-1][x] in ['.']):
                    grid[y-1][x]='X'
                    grid= checkSides(y-1,x,grid)
                
                if(y<len(grid)-1 and grid[y+1][x] in ['.']):
                    grid[y+1][x]='X'
                    grid =checkSides(y+1,x,grid)

            if(grid[y][x] not in ['V','^']):
                if(x>0 and grid[y][x-1] in ['.']):
                    grid[y][x-1]='X'
                    grid = checkSides(y,x-1,grid)
                
                if(x<len(grid[0])-1 and grid[y][x+1] in ['.']):
                    grid[y][x+1]='X'
                    grid = checkSides(y,x+1,grid)
          
            vertColsLeft = ['L','F','|'] 
            vertColsRight= ['J','7','|'] 
            oY=y
            while(y<len(grid)-1):
                y+=1
                if(x>1 and (grid[y][x] in vertColsLeft and grid[y][x-1] in vertColsRight) ):
                        grid[y][x]='V'
                        grid[y][x-1]='V'
                    
                if(x<len(grid[0])-1 and grid[y][x] in vertColsRight and grid[y][x+1] in  vertColsLeft ):
                        grid[y+1][x]='V'
                        grid[y+1][x+1]='V'
            y= oY        #    grid=checkSides(y+1,x,grid,)
            while(y>0):
                y-=1    
                if(x>1 and (grid[y][x] in vertColsLeft and grid[y][x-1] in vertColsRight) ):
                        grid[y][x]='^'
                        grid[y][x-1]='^'
                     #   grid=checkSides(y-1,x,grid)

                if(x<len(grid[0])-1 and (grid[y][x] in vertColsRight and grid[y][x+1] in vertColsLeft) ):
                        grid[y][x]='^'
                        grid[y][x+1]='^'
                        grid=checkSides(y,x,grid)
            y=oY
            horzColTop= ['7','F','-']
            horzColBottom=['J','L','-'] 
            oX=x
            while(x<len(grid[0])-2):
                x+=1
                if(y>1 and (grid[y][x] in horzColBottom and grid[y-1][x] in horzColTop) ):
                        grid[y][x]='>'
                        grid[y-1][x]='>'
                       # grid=checkSides(y-1,x+1,grid)
    
                if(y<len(grid)-1 and grid[y][x] in horzColTop and grid[y+1][x] in  horzColBottom ):
                        grid[y][x]='>'
                        grid[y+1][x]='>'
                    #    grid=checkSides(y+1,x,grid)
            x=oX
            while(x>0):
                x-=1
                if(y>0 and (grid[y][x] in horzColBottom and grid[y-1][x] in horzColTop) ):
                        grid[y-1][x]='>'
                        grid[y-1][x]='>'
                  #      grid=checkSides(y-1,x-1,grid)
 
                if(y<len(grid)-1 and grid[y][x-1] in horzColTop and grid[y+1][x] in  horzColBottom ):
                        grid[y+1][x]='>'
                        grid[y+1][x]='>'
                      #  grid=checkSides(y+1,x-1,grid)
    else:
         print('nope')
      
           

        
    return grid

def plotGrid(grid):
    a=''
    for line in grid:
        for l in line:
            a+=l
        print(a)
        a=''
    print()

def tranceGrid(x,y,grid):
        if(y<1 or y==len(grid)-1 or x<1 or x==len(grid[0])-1):   
            if(grid[y][x] in ['X','.','*','<','>','^','V']):
                grid[y][x]='X'
                grid =checkSides(y,x,grid)
                time.sleep(.1)
                plotGrid(grid)

        return grid
 
for y in range(len(updatedGrid)):
    line = updatedGrid[y]
    for x in range(len(line)):
      #  if(line[x] and line[x] in ['.','X']):
            updatedGrid=tranceGrid(x,y,updatedGrid)

sum=0
a=''
for line in updatedGrid:
    for l in line:
        if(l=='.'):
             sum+=1
        a+=l
    print(a)
    a=''

print(sum)

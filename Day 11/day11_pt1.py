import time
startTime = time.time()
input = open("inputTest.txt", "r").readlines()

cleanInput = []

def printGrid(grid):
    a=''
    for line in grid:
        for l in line:
            a+=l
        print(a)
        a=''

#process input, add rows
for line in input:
    line =line.strip()
    i=[]
    for l in line:
        i.append(l)
    cleanInput.append(i)
    if '#' not in i:
        cleanInput.append(i.copy())

#process input add colomns
blankCols=[]
for col in range(len(cleanInput[0])):
    hasGal=False
    for row in range(len(cleanInput)):
        if(cleanInput[row][col]=='#'):
            hasGal=True
            break
    if(not hasGal):
        blankCols.append(col)
        
for col in range(len(blankCols)):
   # print(blankCols[col])
    for row in range(len(cleanInput)):
        cleanInput[row].insert(blankCols[col]+col,'.')

       
startNumber=1
stars=[]
for line in range(len(cleanInput)):
    for s in range(len(cleanInput[line])):
        if(cleanInput[line][s]=='#'):
            cleanInput[line][s]=str(startNumber)
            stars.append({'N':startNumber,'y':line,'x':s})
            startNumber+=1

def findPath(star,pairStar,galaxy):
    if(star['y']==pairStar['y']):
        return abs(star['x']-pairStar['x'])
    if(star['x']==pairStar['x']):
        return abs(star['y']-pairStar['y'])
    
    return abs(star['y']-pairStar['y'])+abs(star['x']-pairStar['x'])
 
paths={}
for star in stars:
    for pairStar in stars:
        if star != pairStar:
            sN=str(star['N'])
            pN=str(pairStar['N'])
            path=sN+'-'+pN
            if(pN<sN):
                path=pN+'-'+sN
            try:
                paths[path]={'count':findPath(star,pairStar,cleanInput)}
            except:
                print('bad')
                pass
                


sum=0
for p in paths:
    sum+=paths[p]['count']
print(str(sum))




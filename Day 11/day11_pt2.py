import time
startTime = time.time()
input = open("input.txt", "r").readlines()

cleanInput = []

def printGrid(grid):
    a=''
    for line in grid:
        for l in line:
            a+=l
        print(a)
        a=''

#process input, add rows
bigRows=[]
n=0
for line in input:
    line =line.strip()
    i=[]
    for l in line:
        i.append(l)
        
    if '#' not in i:
        i=[]
        for l in line.replace('.','*'):
            i.append(l)
        bigRows.append(n)
       
    n+=1
    cleanInput.append(i)

#process input add colomns
bigCols=[]
for col in range(len(cleanInput[0])):
    hasGal=False
    for row in range(len(cleanInput)):
        if(cleanInput[row][col]=='#'):
            hasGal=True
            break
    if(not hasGal):
        bigCols.append(col)


bigCount=1000000
#Number Stars   
startNumber=1
stars=[]

for line in range(len(cleanInput)):
    for s in range(len(cleanInput[line])):
        if(cleanInput[line][s]=='#'):
            cleanInput[line][s]=str(startNumber)
            bigY=0
            bigX=0
            for y in bigRows:
                if(y<=line):
                    bigY+=1
            for x in bigCols:
                if(x<=s):
                    bigX+=1
            stars.append({'N':startNumber,'y':line+(bigY*(bigCount-1)),'x':s+(bigX*(bigCount-1))})
            startNumber+=1

def findPath(star,pairStar):
    if(star['y']==pairStar['y']):
        return abs(star['x']-pairStar['x'])
    if(star['x']==pairStar['x']):
        return  abs(star['y']-pairStar['y'])
   
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
                paths[path]={'count':findPath(star,pairStar)}
            except:
                print('bad')
                pass
                

#print(stars)
sum=0
for p in paths:
    sum+=paths[p]['count']

print(str(sum))



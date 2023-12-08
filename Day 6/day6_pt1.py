import time
startTime = time.time()
input = open("input.txt", "r").readlines()
#input = open("inputTest.txt", "r").readlines()

def cleanLine(line:str):
    a=[]
    for part in line.split(' '):
        try:
            a.append(int(part.strip()))
        except:
            pass

    return a

races = []
times = cleanLine(input[0])
bests= cleanLine(input[1])

if(len(times)==len(bests)):
    for i in range(len(times)):
        races.append({'time':times[i],'best':bests[i]})   

#print(races)

def findRange(race):
    time=race['time']
    best=race['best']
  # print(best%time)
    low = round(best/time)+1
    while best>=low*(time-low):
        low+=1
   # print('Low (',low,') Sec for ',low*(time-low))
    high = time-low
   # print('High (',high,') Sec for ',high*(time-high))
    return abs(low-high)+1

sum=0
for race in races:
    if(sum==0):
        sum=findRange(race)
    else:
        sum*=findRange(race)

print(sum)
print (time.time()-startTime)
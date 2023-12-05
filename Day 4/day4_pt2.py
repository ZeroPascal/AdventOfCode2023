import time
startTime = time.time()
input = open("input.txt", "r")
sum=0
firstResults=[]
finalResults=[]
for line in input.readlines():
    finalResults.append(0)
    game=int(line[line.index(' ')+1:line.index(':')])
    winningNumbers=[]
    cardNumbers=[]
    for n in line[line.index(':')+1:].split('|')[0].strip().split(' '):
        try:
            winningNumbers.append(int(n))
        except:
            pass
    
    for i in line[line.index(':')+1:].split('|')[1].strip().split(' '):
        try:   
            cardNumbers.append(int(i))
        except:
            pass
    cardScore= 0
  
    for winningNumber in winningNumbers:
            
            if(cardNumbers.count(int(winningNumber))>0):  
                cardScore+=1

    firstResults.append(cardScore)

    
for game in range(len(firstResults)):
    finalResults[game]+=1
    for gameResult in range(firstResults[game]):
       finalResults[game+gameResult+1]+=1*finalResults[game]
    sum+=finalResults[game]

print(sum)
print (time.time()-startTime)
import time
startTime = time.time()
input = open("input.txt", "r")
sum=0
for line in input.readlines():
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
   # cardNumbers = line[line.index(':')+1:].split('|')[1].strip().split(' ')
    cardScore= 0
  
   # print(game,winningNumbers,cardNumbers)
    for winningNumber in winningNumbers:
            if(cardNumbers.count(int(winningNumber))>0):  
                if(cardScore<1): 
                    cardScore=1
                else:
                    cardScore=cardScore*2
       
  
    sum+=cardScore

print(sum)
print (time.time()-startTime)
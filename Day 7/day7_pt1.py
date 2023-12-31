import time
startTime = time.time()
input = open("input.txt", "r").readlines()

def processGame(hand,bet):
   # print(hand,bet)
    
    maxCount=0
    cardTypes={}

    for card in hand:
        try:
           cardTypes[card]+=1
        except:
           cardTypes[card]=1
        if(cardTypes[card]>maxCount):
            maxCount=cardTypes[card]

    #Hand Values) 1- Single, 2- Double, 3 -2 Pair, 4- Tripple, 5- Full, 6- 4of, 7- 5of      
    #Handle 2 Pair
    if(maxCount==2 and len(cardTypes)==3):
        maxCount=3
    #Handle Full House
    elif(maxCount==3 and len(cardTypes)==2):
        maxCount=5
    #Offset Hands above Full house 4 of and 5 of 
    elif(maxCount>3):
        maxCount+=2
    #Offset Hands above One Pair, 3, 4 ,5 of
    elif(maxCount>2):
        maxCount+=1
   # print(hand,cardTypes,maxCount)
    return {'hand':str(maxCount)+hand,'bet':bet}


def mergeSort(game,games):
  #  print('Merging',game,'into',games, len(games))
    if len(games) <1:
      #  print('Bottom',game,games)
        return [game]
    if len(games) == 1:
       # print(games[0])
        if isWinningGame(game,games[0]):
          #  print(' Better')
            return [games[0],game]
        else:
         #   print(' Less')
            return [game,games[0]]

    mid = round(len(games) /2 )
   # print('mid',mid)

    #If game is higher sort to right.
    if(isWinningGame(game,games[mid])):
     #   print(' Recursive Right')
        return games[:mid]+mergeSort(game,games[mid:])
    else:
     #   print(' Recursive Left')
        return mergeSort(game,games[:mid])+games[mid:]
 
def isWinningGame(game1,game2):
    i=0
    game1=game1['hand']
    game2=game2['hand']
   # print('Winning Game Check',game1,game2)
    while i < len(game1):
        if(game1[i].__eq__(game2[i])):
            i+=1
        else:
            match game1[i]:
                case 'A':
                    return True
                case 'K':
                    return not game2[i] in ['A']
                case 'Q':
                    return not game2[i] in ['A','K']
                case 'J':
                    return not game2[i] in ['A','K','Q']
                case 'T':
                    return not game2[i] in ['A','K','Q','J']
            try:
                return int(game1[i])>int(game2[i])
            except:
                return False
    print('Tie!',game1,game2)
    return False
      

results=[]
for line in input:
    game= line.split(' ')
    results=mergeSort(processGame(game[0].strip(),game[1].strip()),results)

print('Good input',len(input),len(results))

sum=-1
for i in range(len(results)):
    if sum==-1:
        sum=int(results[i]['bet'])
    else:
        sum+=int(results[i]['bet'])*(i+1)



#print(results)
print(sum)
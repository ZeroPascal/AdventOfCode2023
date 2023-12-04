import time


def checkRound(round_Results):
    max_Red= 12
    max_Green= 13
    max_Blue= 14
    for color_Result in round_Results.split(','):
            color_Result= color_Result.strip().lower()
            color= str(color_Result[color_Result.index(' '):])
            colorCount = int(color_Result[:color_Result.index(' ')])
            if(color.find('red')>-1 and max_Red<colorCount):
              #  print('Bad',color,colorCount)
                return False
            if(color.find('green')>-1 and max_Green<colorCount):
              #  print('Bad',color,colorCount)
                return False
            if(color.find('blue'))>-1 and max_Blue<colorCount:
              #  print('Bad',color,colorCount)
                return False
    return True

startTime = time.time()

input = open("input.txt", "r")

sum = 0

for line in input.readlines():
    game=int(line[line.index(' ')+1:line.index(':')])
    gameResults = line[line.index(':')+1:]

    goodRound=True
    for round_Results in gameResults.split(';'):
        if(not checkRound(round_Results)):
              goodRound=False
              break
    if(goodRound):
        sum+=game
        
        
print(sum)
print (time.time()-startTime)




           
            
           

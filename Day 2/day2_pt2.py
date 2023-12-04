import time


def checkRound(round_Results,max_Colors):
    
    for color_Result in round_Results.split(','):
            color_Result= color_Result.strip().lower()
            color= str(color_Result[color_Result.index(' '):])
            colorCount = int(color_Result[:color_Result.index(' ')])
            if(color.find('red')>-1 and colorCount>max_Colors['red']):
                max_Colors['red']= colorCount
            if(color.find('green')>-1 and colorCount>max_Colors['green']):
                max_Colors['green']=colorCount
            if(color.find('blue')>-1 and colorCount>max_Colors['blue']):
                max_Colors['blue']=colorCount

    return max_Colors

startTime = time.time()

input = open("input.txt", "r")

sum = 0

for line in input.readlines():
    game=int(line[line.index(' ')+1:line.index(':')])
    gameResults = line[line.index(':')+1:]

    goodRound=True
    max_Colors={'red':0,'blue':0,'green':0}

    for round_Results in gameResults.split(';'):
        
        max_Colors = checkRound(round_Results,max_Colors)
       # print(max_Colors)
    
    sum+= max_Colors['red']*max_Colors['green']*max_Colors['blue']

        
print(sum)
print (time.time()-startTime)




           
            
           

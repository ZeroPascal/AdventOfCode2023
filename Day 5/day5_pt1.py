import time
startTime = time.time()
input = open("inputTest.txt", "r")
input = open("input.txt", "r")
seeds = []
current =''
seedToSoil =[]
soilToFertilizer =[]
fertilizerToWater=[]
waterToLight=[]
lightToTemp=[]
tempToHumidity=[]
humidityToLocation=[]
#Process Input
def processLine(line:str):
    line =line.strip()
    parse = line.split(' ')
    if(len(parse)==3):
        return{
            'dRange': int(parse[0]),
            'sRange': int(parse[1]),
            'len': int(parse[2])
        }
for line in input.readlines():
    if(line.find('seeds:')>-1):
        seeds = line.split(':')[1].strip().split(' ')
    
    match current:
        case 'seed-to-soil':
            seedToSoil.append(processLine(line))
        case 'soil-to-fertilizer':
            soilToFertilizer.append(processLine(line))
        case 'fertilizer-to-water':
            fertilizerToWater.append(processLine(line))
        case 'water-to-light':
            waterToLight.append(processLine(line))
        case 'light-to-temperature':
            lightToTemp.append(processLine(line))
        case 'temperature-to-humidity':
            tempToHumidity.append(processLine(line))
        case 'humidity-to-location':
            humidityToLocation.append(processLine(line))

    match line.strip():
        case 'seed-to-soil map:':
            current='seed-to-soil'
        case 'soil-to-fertilizer map:':
            current='soil-to-fertilizer'
        case 'fertilizer-to-water map:':
            current='fertilizer-to-water'
        case 'water-to-light map:':
            current='water-to-light'
        case 'light-to-temperature map:':
            current='light-to-temperature'
        case 'temperature-to-humidity map:':
            current='temperature-to-humidity'
        case 'humidity-to-location map:':
            current='humidity-to-location'

#Clean Input
def sortMap(e):
    return e['sRange']
def cleanItem(map=[]):
    r=[]
    r.sort()
    try:
        while True:
            map.remove(None)     
    except:
        pass
    map.sort(key=sortMap)
    return map

seedToSoil=cleanItem(seedToSoil)
soilToFertilizer = cleanItem(soilToFertilizer)
fertilizerToWater=cleanItem(fertilizerToWater)
waterToLight=cleanItem(waterToLight)
lightToTemp=cleanItem(lightToTemp)
tempToHumidity=cleanItem(tempToHumidity)
humidityToLocation=cleanItem(humidityToLocation)

def findIndex(seed:int,map:[]):
  
    for m in map:
        if(m['sRange']<=seed and m['sRange']+m['len']-1>=seed):
         #  print(m)
           return m['dRange']-m['sRange']+seed
    return seed


def findSeedLocation(seed):
    oldSeed = seed
    seed=findIndex(seed,seedToSoil)
   # print(oldSeed,'->',seed )
    oldSeed=seed
    seed=findIndex(seed,soilToFertilizer)
   # print(oldSeed,'->',seed )
    oldSeed=seed
    seed=findIndex(seed,fertilizerToWater)
   # print(oldSeed,'->',seed )
    oldSeed=seed
    seed=findIndex(seed,waterToLight)
    #print(oldSeed,'->',seed )
    oldSeed=seed
    seed=findIndex(seed,lightToTemp)
    #print(oldSeed,'->',seed )
    oldSeed=seed
    seed=findIndex(seed,tempToHumidity)
    #print(oldSeed,'->',seed )
    oldSeed=seed
    seed=findIndex(seed,humidityToLocation)
    #print(oldSeed,' == ',seed )

    return seed
minSeed = -1

for seed in seeds:
    r=findSeedLocation(int(seed))
    if(minSeed==-1 or minSeed>r):
        minSeed=r

print(minSeed)


print (time.time()-startTime)
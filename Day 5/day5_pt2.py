import time

startTime = time.time()
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

def findIndex(seeds:[], map:[],mapName=''):
   
    newSeeds = []
    for seed in seeds:
       # print('Processing',mapName,seed)
        seedStart=seed['start']
        seedEnd=seed['end']
        modSeeds=[]
        for m in map:
            mapMax = m['sRange']+m['len']-1
            mapMin= m['sRange']
            
            #Totally within map
            if(seedStart>=mapMin and seedEnd<=mapMax):
                #Return Converted
         #       print('...Inbounds',mapMin,'(',seedStart,'-',seedEnd,')',mapMax,m)
                modSeeds.append({'start':m['dRange']-mapMin+seedStart,'end':m['dRange']-mapMin+seedEnd})
        
            #Starts within map and excedes 
            elif(seedStart<mapMax and mapMin<=seedStart and  seedEnd>mapMax):
                #Look to next seed
           #     print('...Outbounds',mapMin,'(',seedStart,')',mapMax,seedEnd,m)
                modSeeds.append({'start':m['dRange']-mapMin+seedStart,'end':m['dRange']+m['len']})
           #     print('     Adding',modSeeds)
                modSeeds+=findIndex([{'start':mapMax+1,'end':seedEnd}],map)
        #Handle Uniques
        if(len(modSeeds)==0):
            newSeeds.append(seed)
        else:
            newSeeds+=modSeeds

    return newSeeds

def findSeedLocation(seed):

    seed=findIndex(seed, seedToSoil,'Seed To Soil')
    seed=findIndex(seed, soilToFertilizer, 'Soil to Fertilizer')
    seed=findIndex(seed,fertilizerToWater, 'Fertilizer to Water')
    seed=findIndex(seed, waterToLight,'Water to Light')
    seed=findIndex(seed,lightToTemp,' Light to Temp')
    seed=findIndex(seed, tempToHumidity,'Temp to Humidity')
    seed=findIndex(seed, humidityToLocation,'Humidity to Location')

    return seed

#Made Seeds with Range
seedRanges =[]
for i in range(len(seeds)):
    if (i%2<1 or i==0) and i<len(seeds)-1:
        seedRanges.append({'start':int(seeds[i]),'end':int(seeds[i+1])+int(seeds[i])-1}) #int(seeds[i])+int(seeds[i+1])})



f=[]
for seed in seedRanges:
    f+=findSeedLocation([seed])

#Cheap Sort...
def sortSeed(x):
    return x['start']

f.sort(key=sortSeed)
print(f[0]['start'])


print (time.time()-startTime)
import time
startTime = time.time()
input = open("input.txt", "r")

schematic =[]
sum = 0
for line in input.readlines():
    line_Array=[]
    for char in line.strip():
        line_Array.append(char)
    schematic.append(line_Array)

def find_Number(line, lineIndex):
    start=-1
    end=-1
    number =''
    numbers= []
    for x in range(len(line)+1):
        try:
            number+=str(int(line[x]))
            if(start<0):
                start=x
            end=x
        except:
            if(start>=0 and end>=0):
                numbers.append({'number':int(number),'start':start,'end':end,'line':lineIndex})
            start=-1
            end=-1
            number=''

    return(numbers)
numbers=[]
for lineNumber in range(len(schematic)):
    numbers+=find_Number(schematic[lineNumber],lineNumber)

def check_char(char):
     return (char != '.' and (char <'0' or char>'9'))
def check_line(line):
    start = number['start']
    if(start>0):
        start-=1
    end= number['end']
    if(end<len(line)-1):
            end+=2
    lineSplit= line[start:end]
    for char in lineSplit:
            if(check_char(char)):
                return True
    return False

def check_top(number):
    if(number['line']>0):
        return check_line(schematic[number['line']-1])
    return False

def check_bottom(number):
    if(number['line']<len(schematic)-1):
        return check_line(schematic[number['line']+1])
    return False

def check_left(number):
     if(number['start']>0):
        return check_char(schematic[number['line']][number['start']-1])
     return False

def check_right(number):
     if(number['end']<len(schematic[number['line']])):
          return check_char(schematic[number['line']][number['end']+1])
     return False
            
def check_number(number):
    return ( check_top(number) or check_bottom(number) or check_left(number) or check_right(number))

for number in numbers:
 
    if(check_number(number)):
         sum+=number['number']

print(sum)
print (time.time()-startTime)

import time
startTime = time.time()
input = open("input.txt", "r")

sum = 0

intergers = ['zero', 'one', 'two','three','four','five','six','seven','eight','nine']
for line in input.readlines():
    line= line.lower()
    integerIndex=[]
    first_word_index = -1
    first_word_value = 0
    last_word_index = -1
    last_word_value = 0
    for integer in range(len(intergers)):
        try:
            index =line.index(intergers[integer])
            if(first_word_index == -1 or index < first_word_index ):
                first_word_index=index
                first_word_value=integer
            while last_word_index <len(line):
                try:
                    index =line.index(intergers[integer],last_word_index+1)
                    if(index >= last_word_index ):
                        last_word_index=index
                        last_word_value=integer
                except:
                     break
        except:
            pass
    #Parse for Number Numbers
    first_digit_index =0
    last_digit_index = len(line)-2

    while first_digit_index < len(line):
        try:
            int(line[first_digit_index])
            break
        except:
            first_digit_index+=1
    while last_digit_index>first_digit_index:
        try:
            int(line[last_digit_index])
            break
        except:
            last_digit_index-=1

    #Determine Number Word vs Number Number Index
    first_digit =-1
    try:
        first_digit=int(line[first_digit_index])
    
        if first_word_index<first_digit_index and first_word_index != -1:
                first_digit=first_word_value
    except:
        if first_word_index !=-1:
              first_digit=first_word_value
             
    last_digit= -1
    try:
        last_digit= line[last_digit_index]
        if last_word_index>last_digit_index:
                last_digit=last_word_value
    except:
         if last_word_index !=-1:
              last_digit=last_word_value

    try:
        if(int(first_digit) >0):
            try:
                if(int(last_digit) >0):
                    sum+=int(str(first_digit)+str(last_digit))
            except:
                sum+=int(str(first_digit)+str(first_digit))
    except:
        pass

print(sum)
print (time.time()-startTime)
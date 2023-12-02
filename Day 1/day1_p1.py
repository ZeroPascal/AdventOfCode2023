input = open("input.txt", "r")

sum = 0

for line in input.readlines():
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
    sum += int(line[first_digit_index]+''+line[last_digit_index])

print(str(sum))
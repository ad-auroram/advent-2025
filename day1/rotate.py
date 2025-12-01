# go through file line by line, adjust the index accordingly
# R= +index L= -index
# every time index == 0, add to count
# print counts

def readPassword():
    index = 50
    count = 0
    input = open("day1/input1.txt")
    for line in input:
        line = line.strip()
        val = int(line[1:])
        direction = line[0]
        for i in range(val):
            if direction == "R": index +=1
            else: index -=1
            if index > 99: index = 0
            if index < 0: index = 99
            # in the for loop for p2, out for p1
            if index == 0: count +=1
    print(count)

readPassword()

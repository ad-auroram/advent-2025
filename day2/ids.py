# divide the line by commas
# divide by dash, look through range of lower to upper
# check if first half of the digit matches last half
# if invalid id, add to total

def findIDs():
    total = 0
    input = open("day2/input.txt").readline().strip().split(",")
    for id in input:
        ids = id.split("-")
        lower = int(ids[0])
        upper = int(ids[1])+1
        for i in range(lower, upper):
            i = str(i)
            midpoint = len(i) // 2
            first_half = i[:midpoint]
            second_half = i[midpoint:]
            if first_half == second_half:
                total+= int(i)
    print(total)

findIDs()
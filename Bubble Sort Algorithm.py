list = [50,40,30,20,10]
sorted = False
x = 0
y = 0
end = len(list) - 1
Pass = 1
try:
    while sorted == False:
        while x != end:
            if list[x] < list[x+1]:
                pass
            elif list[x] > list[x+1]:
                tempvar = list[x]
                list[x] = list[x+1]
                list[x+1] = tempvar
                print(list)
            x = x + 1
        while y != end:
            if list[y] > list[y+1]:
                x = 0
                print("Pass " + str(Pass) + " is over" )
                Pass = Pass + 1
                break
            elif list[y] < list[y+1]:
                y = y + 1
except KeyboardInterrupt:
    pass
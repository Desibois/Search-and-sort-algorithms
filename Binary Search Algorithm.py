list1 = [10, 20, 30, 40, 50, 60]
item = int(input("Input item: "))
start = 0
loop = 1
end = len(list1)-1
while start <= end:
    midp = (start + end) / 2
    midp = int(midp)
    if list1[midp] == item:
        print("Item found at index " + str(midp) + " in " + str(loop) + " many loops.")
        break
    else:
        if item > list1[midp]:
            start = midp + 1
        else:
            end = midp - 1
    loop = loop + 1

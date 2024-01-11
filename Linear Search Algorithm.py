list = [10, 20, 30, 40, 50, 70, 80, 90]
item = int(input("Input the item you are looking for: "))
found = False
end = len(list) - 1
i = 0
while found == False and i <= end:
    if item == list[i]:
        found = True
        print("Item was found at index " + str(i))
        break
    else:
        i = i + 1
else:
    print("Item was not found")

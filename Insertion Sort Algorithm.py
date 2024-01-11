list1 = [50,40,30,20,10]
list2 = []
for i in range(len(list1)):
    current = list1[i]
    position = i
    list2.append(list1[position])

    while position > 0 and list2[position-1] > current:
        list2[position] = list2[position-1]
        position = position - 1

        list2[position] = current
    print(list2)

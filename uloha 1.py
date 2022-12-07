# DU6: BubbleSort

def bub(list):
    for x in range (0,len(list)):
        for a in range (0,len(list)-x-1):
            if list[a] > list[a+1]:
                list[a],list[a+1]=list[a+1],list[a]
                print(list)
    return list

print(bub([3,8,4,2,5]))

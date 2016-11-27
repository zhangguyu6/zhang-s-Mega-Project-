#Bubble sort
def Bubble_sort(l):
    sort=False
    while not sort:
        sort=True
        for i in range(len(l)-1):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
                sort = False
    return l

print(Bubble_sort([1,3,2,4,51,11,63,2,5]))













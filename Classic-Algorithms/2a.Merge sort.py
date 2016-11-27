#Merge sort
def merge_sort(l):
    if len(l)==1:
        return l
    elif len(l)>1:
        final=[]
        l1=merge_sort(l[:int(len(l)/2)])
        l2=merge_sort(l[int(len(l) / 2):])
        while l1 or l2:
            if not l1:
                final=final+l2
                break
            elif not l2:
                final=final+l1
                break
            elif l1[0]<l2[0]:
                final.append(l1[0])
                l1=l1[1:]
            elif l2[0]<l1[0]:
                  final.append(l2[0])
                  l2=l2[1:]
            elif l1[0]==l2[0]:
                  final.append(l1[0])
                  l1 = l1[1:]
                  l2 = l2[1:]
        return final

print(merge_sort([1,3,2,43,6]))













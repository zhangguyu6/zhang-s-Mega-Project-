#Closest pair problem,使用了分治算法
import math
def closest_pair(l):
    l=sorted(l,key=lambda x:x[0])
    if len(l)==2:#两个元素，直接求值
        distance=math.sqrt((l[0][0]-l[1][0])**2+(l[0][1]-l[1][1])**2)
        return distance
    elif len(l)>2:
        l1=l[:int(len(l)/2)+1]
        l2=l[int(len(l)/2):]
        mindistance=min(closest_pair(l1),closest_pair(l2))
        if len(l)==3:#三个元素，分成两列后求值，避免循环
            return mindistance
        else:
            l3 = [i for i in l1 if i[0] > l2[0][0] - mindistance] + [i for i in l2[1:] if i[0] < l1[-1][0] + mindistance]#多个元素的情况下，探讨中间值以mindistance为半径的区间
            if len(l3)==1:#默认区间至少有3个元素
                l3=l1[:-2]+[l2[2]]
            return min(closest_pair(l3), mindistance)



l=([[1,3],[2,4],[3,6],[4,7],[1,4]])
print(closest_pair(l))









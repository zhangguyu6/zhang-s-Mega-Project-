#Happy Numbers
def findhappy_numbers(rangeofnum,limit):
    listofhappy=[]
    for i in range(1,rangeofnum+1):
        itertime=0
        k=i
        while itertime<=limit:
            if sum_of_alldigits(k)==1:
                listofhappy.append(i)
                break
            else:
                itertime+=1
                k=sum_of_alldigits(k)
    return listofhappy

def sum_of_alldigits(n):
    return sum([int(i)*int(i) for i in str(n)])

print(findhappy_numbers(100,6))#happy nums less than 100
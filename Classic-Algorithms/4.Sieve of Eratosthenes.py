#Sieve of Eratosthenes，埃拉托色尼筛选法
import math
def sieve(limit):#寻找所有小于limit的素数
    prime=[True]*limit
    result=[2]
    prime[::2]=[False]*len(prime[::2])
    for i in range(3,(int (math.sqrt(limit)+1))):
        if prime[i]:
            result.append(i)
            prime[i*i::2*i]=[False]*len(prime[i*i::2*i])
    for i in range((int(math.sqrt(limit) + 1)),limit):
        if prime[i]:
            result.append(i)
    return result


print(sieve(100))




